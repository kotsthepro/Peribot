import random

from discord.ext import commands

from .utils.dataIO import dataIO


class EightBall(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.choices = dataIO.load_json("data/8ball/8ball.json")['choices']


    @commands.command(name='8b')
    async def eightball(self, ctx):
        """
        Check the fates on your question
        :return:
        """
        await ctx.send(f'```{random.choice(self.choices)}```')

def setup(bot):
    n = EightBall(bot)
    bot.add_cog(n)
