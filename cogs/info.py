import discord
import psutil
import time
import os

from datetime import datetime
from discord.ext import commands
from utils import default

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")
        self.process = psutil.Process(os.getpid())

    @commands.command(aliases=["stats", "about"])
    async def info(self, ctx):
        """ DEBUG COMMAND """
        ramUsage = self.process.memory_full_info().rss / 1024**2
        avgmembers = round(len(self.bot.users) / len(self.bot.guilds))

        embedColour = discord.Embed.Empty

        embed = discord.Embed(colour=embedColour)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.add_field(name="Library", value="discord.py", inline=True)
        embed.add_field(name="Servers", value=f"{len(ctx.bot.guilds)} ( avg: {avgmembers} users/server )", inline=True)
        embed.add_field(name="Commandes", value=len([x.name for x in self.bot.commands]), inline=True)
        embed.add_field(name="RAM", value=f"{ramUsage:.2f} MB", inline=True)

        await ctx.send(content=f"ℹ About **{ctx.bot.user}** | **{self.config.version}**", embed=embed)

    @commands.command(aliases=["src"])
    async def source(self, ctx):
        """ src """
        await ctx.send(f"https://github.com/yunseok/em2500-M253X")

def setup(bot):
    bot.add_cog(Info(bot))