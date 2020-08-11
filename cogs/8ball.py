import discord
import random

from discord.ext import commands
from utils import default

class EightBall(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, question: commands.clean_content):
        """ Pose une question à la boule magique """

        ball_response = [
            'Oui', 'Non', 'Tu veux pas essayer de deviner ?', 'Très douteux',
            'Bien sûr', 'Sans aucun doute', 'Probable...', "C'est possible",
            'Non... (╯°□°）╯︵ ┻━┻',
        ]

        answer = random.choice(ball_response)
        await ctx.send(f"🎱 **Question:** {question}\n**Answer:** {answer}")

def setup(bot):
    bot.add_cog(EightBall(bot))