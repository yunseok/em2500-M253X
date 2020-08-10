import platform
import logging
import discord
import os

from configparser import ConfigParser
from discord.ext.commands import AutoShardedBot

class Bot(AutoShardedBot):
	def __init__(self, *args, prefix=None, **kwargs):
		super().__init__(*args, **kwargs)

		on_ready_message = "EM2500-M253X IS READY!"
		
		print(f"Python version: { platform.python_version() }")
		print(f"discord.py API version: { discord.__version__ }")
		print(on_ready_message)
		
		logging.info(f"Python version: { platform.python_version() }")
		logging.info(f"discord.py API version: { discord.__version__ }")
		logging.info(on_ready_message)

	async def on_message(self, msg):
		if not self.is_ready() or msg.author.bot:
			return

		tine = "tine"
		words_list = msg.content.split()

		for i in words_list:
			if tine in i:
				converted_word = "pain au " + i[:-3]
				await msg.channel.send("C'est " + i + ", pas " + converted_word + ".")

		await self.process_commands(msg)