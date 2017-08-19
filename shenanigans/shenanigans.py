from discord.ext import commands
from random import *

class Shenanigans:
    """Shenanigans - silly stuff for your bot
    Git Workshop"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def boop(self, ctx):
        """boooooop"""
        await self.bot.say('https://i.imgur.com/PLwj35n.jpg')

    @commands.command(pass_context=True) #@command means that this is the command 
    async def double(self, ctx, number: int):
        """doubles what you give me"""
        await self.bot.say(number*2)


    @commands.command(pass_context=True, no_pm=True)
    async def add(self, ctx, a: int, b: int):
        """add 2 numbers"""
        await self.bot.say(a+b)
        pass

    @commands.command(pass_context=True)
    async def sort(self, ctx, *items):
        """sorts the list of items you give me """
        await self.bot.say(items.sort())
        pass

    @commands.command(pass_context=True)
    async def pose(self, ctx):
        """strikes a random pose!"""

        poses = [":SeemsMarco:", ":MarcoSalt:", ":MarcoSaltier:"]
        await self.bot.say(poses[randrange(1, 4)])
        
    @commands.command(pass_context=True)
    async def king(self, ctx):
        """Crowns you King of Code Camp"""
        await self.bot.say('I declare Preator to be King of Code Camp!')


def setup(bot):
    bot.add_cog(Shenanigans(bot))
