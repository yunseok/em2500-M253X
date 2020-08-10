import urllib.request
import discord
import json

from discord.ext import commands
from utils import default

class Btc(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.config = default.get("config.json")

	@commands.command(aliases=["bitcoin", "tbc"])
	async def btc(self, ctx):
		""" Affiche la valeur du bitcoin """

		btc_api = "https://api.coindesk.com/v1/bpi/currentprice.json"
		req = urllib.request.Request(btc_api)

		btcData = urllib.request.urlopen(req).read()
		x = json.loads(btcData.decode('utf-8'))

		await ctx.send("La valeur du bitcoin est de **" + x["bpi"]["EUR"]["rate"] + "**€")
		

def setup(bot):
	bot.add_cog(Btc(bot))