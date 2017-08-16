import discord
from discord.ext import commands

class Shenanigans:
    """shenanigans - silly stuff for your bot"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def eyy(self, ctx):
        """lmao"""
        await self.bot.say('lmao')

    @commands.command(pass_context=True)
    async def boop(self, ctx):
        """'w'"""
        await self.bot.say('https://i.imgur.com/PLwj35n.jpg')

def setup(bot):
    n = Shenanigans(bot)
    bot.add_cog(n)
