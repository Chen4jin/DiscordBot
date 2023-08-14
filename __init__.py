import os

from dotenv import load_dotenv
import discord

load_dotenv(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".env"))
token = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
client = discord.Client(intents=intents)
