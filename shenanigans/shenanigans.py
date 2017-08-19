from discord.ext import commands

class Shenanigans:
    """Shenanigans - silly stuff for your bot"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def boop(self, ctx):
        """boooooop"""
        await self.bot.say('https://i.imgur.com/PLwj35n.jpg')

    @commands.command(pass_context=True)
    async def double(self, ctx, number: int):
        """doubles what you give me"""
        await self.bot.say(number*2)
        pass

    @commands.command(pass_context=True, no_pm=True)
    async def add(self, ctx, a: int, b: int):
        
        """add 2 numbers"""
        a = 5
        b = 4
        ctx = a + b
        await self.bot.say(ctx )
        pass

    @commands.command(pass_context=True)
    async def sort(self, ctx, *items):
        """sorts the list of items you give me"""
        pass

    @commands.command(pass_context=True)
    async def pose(self, ctx):
        """strikes a random pose!"""
        pass

def setup(bot):
    bot.add_cog(Shenanigans(bot))
