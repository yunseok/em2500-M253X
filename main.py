import logging
import discord
import os

from configparser import ConfigParser
from utils import default
from utils.data import Bot

config = default.get("config.json")

logging.basicConfig(
    filename="latest.log",
    level=logging.DEBUG,
    filemode="w",
    format="[ %(asctime)s: ] %(levelname)s: %(message)s",
    datefmt="%d/%m/%Y %I:%M:%S %p"
)

bot = Bot(
    command_prefix=config.prefix,
    prefix=config.prefix
)

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")

bot.run(config.token)