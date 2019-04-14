from twitchio.ext import commands
from requests import get as _get
import aiohttp
import sys
import os
import json
import logging
import traceback
import logger as _logger
from auth import access_token, token, api_token, client_id, trn_token

twitch_channel = _get('https://api.twitch.tv/kraken/channel', headers={
    'Content-Type': 'application/vnd.twitchtv.v5+json',
    'Client-ID': client_id,
    'Authorization': access_token
})
channel_id = twitch_channel.json()['_id']

logger = logging.getLogger()
_logger.setup_logger(logger)


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


with open('./channels.json', 'r+') as channels_file:
    channels = json.load(channels_file)
    channels = channels['channels']


class Botto(commands.Bot):
    def __init__(self):
        super().__init__(prefix=['!', '?'], irc_token=token, api_token=api_token,
                         client_id=channel_id, nick='adure_bot', initial_channels=channels)

    # ON READY EVENT
    async def event_ready(self):
        logger.info(f"Logged in as {self.nick}")
        logger.info(f"Connected to channels...  {', '.join(self.initial_channels)}")
        modules = ['modules.overwatch', 'modules.apex', 'modules.spotify']
        logger.debug(f"Loading modules...   {', '.join([module.replace('modules.', '') for module in modules])}")
        for module in modules:
            self.load_module(module)

    # ON MESSAGE EVENT
    async def event_message(self, message):
        logger.log(5, f"{message.author.name}: {message.content}")
        await self.handle_commands(message)

    # ON COMMAND ERROR
    async def event_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            pass
        else:
            logger.error(f"[{ctx.channel.name}] {error}")
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


bot = Botto()
bot.run()
