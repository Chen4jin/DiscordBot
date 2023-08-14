import os

import discord

from DiscordBot import client
from ..SpotifyModule.spotify_util import SpotifyUtil

@client.tree.command()
async def download(interaction: discord.Interaction, song_name: str):
    """Download the song"""
    try:
        spotify_util = SpotifyUtil()
        await interaction.response.defer(thinking=True)
        track_path = spotify_util.download_track(song_name)
        
        with open(track_path, "rb") as f:
            discord_file = discord.file.File(f)
            discord_file.filename = os.path.basename(track_path)
            await interaction.followup.send(content=discord_file.filename, ephemeral=True, file=discord_file)
    except Exception as e:
        raise e
