import datetime
import logging
import constants
from discord import Color, Embed
from discord.ext import commands


LEVEL_COLORS = {
    logging.CRITICAL: Color.red(),
    logging.ERROR: Color.red(),
    logging.WARNING: Color.gold(),
    logging.INFO: Color.blurple()
}
class DiscordHandler(logging.Handler):
    """
    Implement logging.Handler methods to send logs to discord channel
    """
    def __init__(self,bot: commands.Bot, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.client = bot
        self.log_channel = self.client.get_channel(constants.LOG_CHANNEL)

    def _level_to_color(self,level_number:int):
        return LEVEL_COLORS.get(level_number)

    def emit(self, record):
        if not self.client.loop.is_running():
            # The event loop is not running (discord is not connected)
            return

        # Create an embed with a title like "Info" or "Error" and a color
        # relating to the level of the log message
        embed = Embed(title=record.levelname.title(), color=self._level_to_color(record.levelno))

        embed.timestamp = datetime.datetime.utcnow()

        embed.add_field(name="Message", value=record.msg, inline=False)
        embed.add_field(name="Function", value=f"`{record.funcName}`", inline=True)
        embed.add_field(name="File name", value=f"`{record.filename}`", inline=True)
        embed.add_field(name="Line number", value=record.lineno, inline=True)

        if "discord_info" in record.__dict__:
            for field, value in record.__dict__["discord_info"].items():
                embed.add_field(name=field, value=value, inline=True)

        if self.log_channel is None:
            self.log_channel = self.client.get_channel(constants.LOG_CHANNEL)

        # Create a task in the event loop to send the logging embed
        self.client.loop.create_task(self.log_channel.send(embed=embed))
