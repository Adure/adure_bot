from auth import spotify_refresh_token, spotify_client_id, spotify_client_secret
from twitchio.ext import commands
import aiohttp
import asyncio
import logging
import json

logger = logging.getLogger(__name__)


async def get_currently_playing():
    logger.debug("Retrieving currently playing song...")
    with open('spotify.json', 'r') as spotify_file:
        contents = json.load(spotify_file)
        spotify_token = contents['access_token']

    async def fetch(session, url):
        async with session.get(url, headers = {"Authorization": spotify_token}) as response:
            try:
                return await response.json()
            except:
                return None

    async def main():
        async with aiohttp.ClientSession() as session:
            r = await fetch(session, f'https://api.spotify.com/v1/me/player/currently-playing')
            return r

    return await main()

async def refresh_auth_token():
    while True:
        with open('spotify.json', 'r+') as spotify_file:
            contents = json.load(spotify_file)
            refresh_token = spotify_refresh_token

            async def fetch(session, url):
                async with session.post(url, headers = {'Content-Type': 'application/x-www-form-urlencoded'},
                                                data = {"client_id": spotify_client_id,
                                                        "client_secret": spotify_client_secret,
                                                        "grant_type": "refresh_token",
                                                        "refresh_token": refresh_token}) as response:
                    return await response.json()

            async def main():
                async with aiohttp.ClientSession() as session:
                    r = await fetch(session, 'https://accounts.spotify.com/api/token')
                    return r

            response = await main()

            auth_dict = {"access_token": f"Bearer {response['access_token']}"}
            spotify_file.seek(0)
            json.dump(auth_dict, spotify_file, separators=(',', ': '), indent=4)
            spotify_file.truncate()

        await asyncio.sleep(3500)


@commands.cog()
class Spotify():
    def __init__(self, bot):
        self.bot = bot
        logger.debug("Module Spotify loaded...")
        self.bot.loop.create_task(refresh_auth_token())

    @commands.command(aliases=['song'])
    async def song_command(self, message):
        song = await get_currently_playing()

        if song == None:
            await message.channel.send("Spotify not open.")
            return

        if bool(song['is_playing']) != True:
            await message.channel.send("No song playing.")
            return

        form_message = f"{song['item']['name']} - {song['item']['artists'][0]['name']}"
        await message.channel.send(form_message)
