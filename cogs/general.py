import random
import discord
import urllib
import secrets
import asyncio
import aiohttp
import re

from io import BytesIO
from discord.ext import commands
from utils import lists, default


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    """
    @commands.command(aliases=['aide', 'list'])
    async def help(self, ctx):
        Voir la liste de commandes

        await ctx.send(f"")
    """

    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, question: commands.clean_content):
        """ Une boule magique répond à toutes vos questions """
        answer = random.choice(lists.ballresponse)
        await ctx.send(f"🎱\n**Question :** {question}\n**Réponse :** {answer}")

    @commands.command(aliases=['pileouface', 'flip', 'coin'])
    async def pileface(self, ctx):
        """ Pile ou Face ? """
        coinsides = ['Pile', 'Face']
        await ctx.send(f"**{ctx.author.name}** a lancé une pièce et a obtenu **{random.choice(coinsides)}**!")

    @commands.command()
    async def mdp(self, ctx, nbytes: int = 18):
        """ Génére un mot de passe aléatoire """
        if nbytes not in range(3, 1401):
            return await ctx.send("Veuillez choisir un nombre entre 3-1400.")
        if hasattr(ctx, 'guild') and ctx.guild is not None:
            await ctx.send(f"Je vous ai envoyé un message privé avec votre mot de passe **{ctx.author.name}**")
        await ctx.author.send(f"🎁 **Voici votre mot de passe :**\n{secrets.token_urlsafe(nbytes)}")

    @commands.command()
    async def note(self, ctx, *, thing: commands.clean_content):
        """ Notez ce que vous voulez """
        rate_amount = random.uniform(0.0, 100.0)
        await ctx.send(f"I'd rate `{thing}` a **{round(rate_amount, 4)} / 100**")

    @commands.command(aliases=['hotcalc', 'hot'])
    async def bg(self, ctx, *, user: discord.Member = None):
        """ Calcule la beauté d'un utilisateur """
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

        await ctx.send(f"**{user.name}** est **{hot:.2f}%** hot {emoji}")

    """
    COMMAND TO REWORK
    @commands.command()
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def bet(self, ctx):
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

        lostMessages = [
            "Perdu 😢",
            "T'es nul",
            "Perdu, veuillez re-essayer."
        ]

        if (a == b == c):
            await ctx.send(f"{slotmachine} Parfait ! 🎉\n Vous avez gagné (money) bucks !")
        elif (a == b) or (a == c) or (b == c):
            await ctx.send(f"{slotmachine} 2 à la suite ! 🎉 \n Vous avez gagné (money) bucks !")
        else:
            await ctx.send(f"{slotmachine} {random.choice(lostMessages)}")
    """


def setup(bot):
    bot.add_cog(General(bot))
