import discord
import random

from discord.ext import commands
from utils import default

class Hot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    @commands.command(aliases=["bg"])
    async def hot(self, ctx, *, user: discord.Member = None):
        """ Calcule a quel point un utilisateur est bg """
        user = user or ctx.author

        random.seed(user.id)
        r = random.randint(1, 100)
        hot = r / 1.17

        emoji = "💔"
        if hot > 25:
            emoji = "❤"
        if hot > 50:
            emoji = "💖"
        if hot > 75:
            emoji = "💞"

        # todos: check if user exists
        await ctx.send(f"{emoji} **{user.name}** est **{ round(hot) }%** bg {emoji}")

def setup(bot):
    bot.add_cog(Hot(bot))