from ..auth import spotify_token
from twitchio.ext import commands
import aiohttp
import logging

logger = logging.getLogger(__name__)


async def get_currently_playing():
    logger.debug("Retrieving currently playing song...")

    async def fetch(session, url):
        async with session.get(url, headers = {"Authorization": spotify_token}) as response:
            return await response.json()

    async def main():
        async with aiohttp.ClientSession() as session:
            r = await fetch(session, f'https://api.spotify.com/v1/me/player/currently-playing')
            return r

    return await main()

async def refresh_auth_token(refresh_token):
    while True:
        # TODO: do this...
        print('need to refresh token')

        await asyncio.sleep(3500)


@commands.cog()
class Spotify():
    def __init__(self, bot):
        self.bot = bot
        self.bot.loop.create_task(refresh_auth_token())

    @commands.command(aliases=['song'])
    async def song_command(self, message):
        song = await get_currently_playing()

        if bool(song['is_playing']) != True:
            await message.channel.send("No song playing.")
            return

        form_message = f"{song['item']['name']} - {song['item']['artists'][0]['name']}"
        await message.channel.send(form_message)
