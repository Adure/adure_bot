from twitchio.ext import commands
import aiohttp
import logging

logger = logging.getLogger(__name__)


async def get_overwatch_profile(user):
    logger.debug("Retrieving Overwatch profile...")

    async def fetch(session, url):
        async with session.get(url) as response:
            return await response.json()

    async def main():
        async with aiohttp.ClientSession() as session:
            r = await fetch(session, f'https://ovrstat.com/stats/pc/us/{user}')
            return r

    return await main()

async def form_stats_message(profile, hero):
    try:
        stats = profile['competitiveStats']['topHeroes'][hero]
    except KeyError:
        return 'Hero data not found.'
    msg = f"""
    Time played: {stats['timePlayed']} |
    Games won: {stats['gamesWon']} |
    Win percentage: {stats['winPercentage']}% |
    Accuracy: {stats['weaponAccuracy']}% |
    Eliminations per life: {stats['eliminationsPerLife']}
    """
    return msg


@commands.cog()
class Overwatch():
    def __init__(self, bot):
        self.bot = bot

    # --------- Competitive Rating ---------- #
    @commands.command(aliases=['sr'])
    async def sr_command(self, message, name='TheBigOCE-1503'):
        await message.channel.send("Retrieving profile...")
        name = name.replace('#', '-')
        profile = await get_overwatch_profile(name)
        try:
            sr = profile['rating']
        except KeyError:
            sr = profile['message']
        await message.channel.send(sr)

    # ------------- Win Percent ------------- #
    @commands.command(aliases=['winp'])
    async def winp_command(self, message):
        await message.channel.send("Retrieving profile...")
        profile = await get_overwatch_profile('TheBigOCE-1503')
        compstats = profile['competitiveStats']['careerStats']['allHeroes']['game']
        winp = int(compstats['gamesWon']) / int(compstats['gamesPlayed']) * 100
        await message.channel.send(f"Win ratio: {winp:.2f}% ({compstats['gamesPlayed']} games played)")

    # ---------- Kill Death Ratio ----------- #
    @commands.command(aliases=['kdr'])
    async def kdr_command(self, message):
        await message.channel.send("Retrieving profile...")
        profile = await get_overwatch_profile('TheBigOCE-1503')
        compstats = profile['competitiveStats']['careerStats']['allHeroes']['combat']
        kdr = int(compstats['eliminations']) / int(compstats['deaths'])
        await message.channel.send(f"Kill death ratio: {kdr:.2f} ({compstats['eliminations']} eliminations)")

    # ---------------- Ana ----------------- #
    @commands.command(aliases=['ana'])
    async def ana_command(self, message):
        await message.channel.send("Retrieving profile...")
        profile = await get_overwatch_profile('TheBigOCE-1503')
        ana = await form_stats_message(profile, 'ana')
        await message.channel.send(ana)

    # ---------------- Ashe ----------------- #
    @commands.command(aliases=['ashe'])
    async def ashe_command(self, message):
        await message.channel.send("Retrieving profile...")
        profile = await get_overwatch_profile('TheBigOCE-1503')
        ashe = await form_stats_message(profile, 'ashe')
        await message.channel.send(ashe)

    # -------------- Bastion --------------- #
    @commands.command(aliases=['bastion'])
    async def bastion_command(self, message):
        await message.channel.send("Retrieving profile...")
        profile = await get_overwatch_profile('TheBigOCE-1503')
        bastion = await form_stats_message(profile, 'bastion')
        await message.channel.send(bastion)

    # -------------- Brigitte --------------- #
    @commands.command(aliases=['brigitte'])
    async def brigitte_command(self, message):
        await message.channel.send("Retrieving profile...")
        profile = await get_overwatch_profile('TheBigOCE-1503')
        brigitte = await form_stats_message(profile, 'brigitte')
        await message.channel.send(brigitte)

    # -------------- D.Va --------------- #
    @commands.command(aliases=['dva'])
    async def dva_command(self, message):
        await message.channel.send("Retrieving profile...")
        profile = await get_overwatch_profile('TheBigOCE-1503')
        dva = await form_stats_message(profile, 'dVa')
        await message.channel.send(dva)

    # -------------- Genji --------------- #
    @commands.command(aliases=['genji'])
    async def genji_command(self, message):
        await message.channel.send("Retrieving profile...")
        profile = await get_overwatch_profile('TheBigOCE-1503')
        genji = await form_stats_message(profile, 'genji')
        await message.channel.send(genji)

    # -------------- Hanzo --------------- #
    @commands.command(aliases=['hanzo'])
    async def hanzo_command(self, message):
        await message.channel.send("Retrieving profile...")
        profile = await get_overwatch_profile('TheBigOCE-1503')
        hanzo = await form_stats_message(profile, 'hanzo')
        await message.channel.send(hanzo)

    # -------------- Junkrat --------------- #
    @commands.command(aliases=['junkrat'])
    async def junkrat_command(self, message):
        await message.channel.send("Retrieving profile...")
        profile = await get_overwatch_profile('TheBigOCE-1503')
        junkrat = await form_stats_message(profile, 'junkrat')
        await message.channel.send(junkrat)

    # -------------- Lucio --------------- #
    @commands.command(aliases=['lucio'])
    async def lucio_command(self, message):
        await message.channel.send("Retrieving profile...")
        profile = await get_overwatch_profile('TheBigOCE-1503')
        lucio = await form_stats_message(profile, 'lucio')
        await message.channel.send(lucio)

    # -------------- McCree --------------- #
    @commands.command(aliases=['mccree'])
    async def mccree_command(self, message):
        await message.channel.send("Retrieving profile...")
        profile = await get_overwatch_profile('TheBigOCE-1503')
        mccree = await form_stats_message(profile, 'mccree')
        await message.channel.send(mccree)

    # -------------- Mei --------------- #
    @commands.command(aliases=['mei'])
    async def mei_command(self, message):
        await message.channel.send("Retrieving profile...")
        profile = await get_overwatch_profile('TheBigOCE-1503')
        mei = await form_stats_message(profile, 'mei')
        await message.channel.send(mei)

    # -------------- Mercy --------------- #
    @commands.command(aliases=['mercy'])
    async def mercy_command(self, message):
        await message.channel.send("Retrieving profile...")
        profile = await get_overwatch_profile('TheBigOCE-1503')
        mercy = await form_stats_message(profile, 'mercy')
        await message.channel.send(mercy)

    # -------------- Orisa --------------- #
    @commands.command(aliases=['orisa'])
    async def orisa_command(self, message):
        await message.channel.send("Retrieving profile...")
        profile = await get_overwatch_profile('TheBigOCE-1503')
        orisa = await form_stats_message(profile, 'orisa')
        await message.channel.send(orisa)

    # -------------- Reaper --------------- #
    @commands.command(aliases=['reaper'])
    async def reaper_command(self, message):
        await message.channel.send("Retrieving profile...")
        profile = await get_overwatch_profile('TheBigOCE-1503')
        reaper = await form_stats_message(profile, 'reaper')
        await message.channel.send(reaper)

    # -------------- Reinhardt --------------- #
    @commands.command(aliases=['reinhardt', 'rein'])
    async def reinhardt_command(self, message):
        await message.channel.send("Retrieving profile...")
        profile = await get_overwatch_profile('TheBigOCE-1503')
        reinhardt = await form_stats_message(profile, 'reinhardt')
        await message.channel.send(reinhardt)

    # -------------- Roadhog --------------- #
    @commands.command(aliases=['roadhog'])
    async def roadhog_command(self, message):
        await message.channel.send("Retrieving profile...")
        profile = await get_overwatch_profile('TheBigOCE-1503')
        roadhog = await form_stats_message(profile, 'roadhog')
        await message.channel.send(roadhog)

    # -------------- Soldier 76 --------------- #
    @commands.command(aliases=['soldier76', 'soldier'])
    async def soldier76_command(self, message):
        await message.channel.send("Retrieving profile...")
        profile = await get_overwatch_profile('TheBigOCE-1503')
        soldier76 = await form_stats_message(profile, 'soldier76')
        await message.channel.send(soldier76)

    # -------------- Sombra --------------- #
    @commands.command(aliases=['sombra'])
    async def sombra_command(self, message):
        await message.channel.send("Retrieving profile...")
        profile = await get_overwatch_profile('TheBigOCE-1503')
        sombra = await form_stats_message(profile, 'sombra')
        await message.channel.send(sombra)

    # -------------- Torbjorn --------------- #
    @commands.command(aliases=['torbjorn', 'torb'])
    async def torbjorn_command(self, message):
        await message.channel.send("Retrieving profile...")
        profile = await get_overwatch_profile('TheBigOCE-1503')
        torbjorn = await form_stats_message(profile, 'torbjorn')
        await message.channel.send(torbjorn)

    # -------------- Tracer --------------- #
    @commands.command(aliases=['tracer'])
    async def tracer_command(self, message):
        await message.channel.send("Retrieving profile...")
        profile = await get_overwatch_profile('TheBigOCE-1503')
        tracer = await form_stats_message(profile, 'tracer')
        await message.channel.send(tracer)

    # -------------- Widowmaker --------------- #
    @commands.command(aliases=['widowmaker', 'widow'])
    async def widowmaker_command(self, message):
        await message.channel.send("Retrieving profile...")
        profile = await get_overwatch_profile('TheBigOCE-1503')
        widowmaker = await form_stats_message(profile, 'widowmaker')
        await message.channel.send(widowmaker)

    # -------------- Winston --------------- #
    @commands.command(aliases=['winston'])
    async def winston_command(self, message):
        await message.channel.send("Retrieving profile...")
        profile = await get_overwatch_profile('TheBigOCE-1503')
        winston = await form_stats_message(profile, 'winston')
        await message.channel.send(winston)
    # -------------- Hammond --------------- #
    @commands.command(aliases=['hammond', 'wreckingball'])
    async def hammond_command(self, message):
        await message.channel.send("Retrieving profile...")
        profile = await get_overwatch_profile('TheBigOCE-1503')
        hammond = await form_stats_message(profile, 'wreckingBall')
        await message.channel.send(hammond)

    # -------------- Zarya --------------- #
    @commands.command(aliases=['zarya'])
    async def zarya_command(self, message):
        await message.channel.send("Retrieving profile...")
        profile = await get_overwatch_profile('TheBigOCE-1503')
        zarya = await form_stats_message(profile, 'zarya')
        await message.channel.send(zarya)

    # -------------- Zenyatta --------------- #
    @commands.command(aliases=['zenyatta', 'zen'])
    async def zenyatta_command(self, message):
        await message.channel.send("Retrieving profile...")
        profile = await get_overwatch_profile('TheBigOCE-1503')
        zenyatta = await form_stats_message(profile, 'zenyatta')
        await message.channel.send(zenyatta)
