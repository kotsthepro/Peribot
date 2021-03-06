import discord
from discord.ext import commands

class JC(commands.Cog):
    """Commands for the Peribot Creator!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def source(self, ctx):
        """
        Returns the github link to Peribot
        """
        embed = discord.Embed(title="jcsumlin/Peribot", color=0x24292E,url="https://github.com/jcsumlin/Peribot")
        embed.set_thumbnail(url="https://github.com/jcsumlin.png")
        embed.add_field(name='Repository',
                        value='https://github.com/jcsumlin/Peribot', inline = True)
        embed.set_footer(text="Please support Peribot on my Patreon! www.patreon.com/botboi")
        await ctx.send(embed=embed)

    @commands.command()
    async def botboi(self, ctx):
        """
        Returns the Patreon link for J_C bot boi!
        """
        embed = discord.Embed(
            title="J_C is creating Bots (Discord, Reddit, Twitch, Life Automation?)",
            url="http://www.patreon.com/botboi", color=0xFA7664)
        embed.set_thumbnail(
            url="https://c10.patreonusercontent.com/3/eyJ3IjoyMDB9/patreon-media/p/user/13355013/9c2f890a5a464c81bac95dab78511700/2?token-time=2145916800&token-hash=_ly1tGurxqCXoLF2sJ_Qo1HHy8nvlC9ynqEuTbuKtD8%3D")
        embed.add_field(name="Patreon", value="Interested in helping me develop my bot army? Check out my Patreon for a full desciption of what you can get out of it and how it helps me! Of course this is by no means required to use Peribot but any support is always appreciated :heart:", inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(JC(bot))
