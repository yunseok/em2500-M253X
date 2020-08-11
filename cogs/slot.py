import discord
import random

from discord.ext import commands
from utils import default

class Slot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    @commands.command(aliases=['bet'])
    @commands.cooldown(rate=1, per=3.0)
    async def slot(self, ctx):
        """ ??? """
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

        # todos:
        # add economy

        if (a == b == c):
            await ctx.send(f"{slotmachine} GG 🎉")
        elif (a == b) or (a == c) or (b == c):
            await ctx.send(f"{slotmachine} 2 à la suite ! 🎉")
        else:
            await ctx.send(f"{slotmachine} GAME OVER")

def setup(bot):
    bot.add_cog(Slot(bot))