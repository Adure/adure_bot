from twitchio.ext import commands
import aiohttp
import logging

logger = logging.getLogger(__name__)


async def get_apex_profile(user):
    logger.debug("Retrieving Apex Legends profile...")

    async def fetch(session, url):
        async with session.get(url, headers={"TRN-Api-Key": trn_token}) as response:
            return await response.json()

    async def main():
        async with aiohttp.ClientSession() as session:
            r = await fetch(session, f'https://public-api.tracker.gg/apex/v1/standard/profile/5/{user}')
            return r

    return await main()


@commands.cog()
class Apex():
    def __init__(self, bot):
        self.bot = bot

    # ---------------- Kills ---------------- #
    @commands.command(aliases=['kills'])
    async def kills_command(self, message, user):
        await message.channel.send("Retrieving profile...")
        profile = await get_apex_profile(user)
        try:
            kills = profile['data']['stats'][1]['value']
            await message.channel.send(f'{int(kills)} kills')
        except KeyError:
            await message.channel.send('Profile not found.')

    # --------------- Damage ---------------- #
    @commands.command(aliases=['damage'])
    async def damage_command(self, message, user):
        await message.channel.send("Retrieving profile...")
        profile = await get_apex_profile(user)
        try:
            damage = profile['data']['stats'][2]['value']
            await message.channel.send(f'{int(damage)} damage')
        except KeyError:
            await message.channel.send('Profile not found.')
