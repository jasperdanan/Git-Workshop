import discord
from discord.ext import commands

class Shenanigans:
    """shenanigans - silly stuff for your bot"""

    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    n = Shenanigans(bot)
    bot.add_cog(n)
