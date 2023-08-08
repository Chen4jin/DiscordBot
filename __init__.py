import os

from dotenv import load_dotenv
import discord

load_dotenv(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".env"))
token = os.getenv("DISCORD_TOKEN")
server_id = os.getenv("SERVER_ID")

MY_GUILD = discord.Object(id=server_id)


intents = discord.Intents.default()
intents.members = True
intents.message_content = True


class MyClient(discord.Client):
    """_summary_

    Args:
        discord (_type_): discord client
    """
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = discord.app_commands.CommandTree(self)

    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


client = MyClient(intents=intents)
