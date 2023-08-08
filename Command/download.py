import os

import discord

from MusicBot import client
from ..SpotifyModule.spotify_util import SpotifyUtil

@client.tree.command()
async def download(interaction: discord.Interaction, song_name: str):
    """Download the song"""
    try:
        spotify_util = SpotifyUtil()
        await interaction.response.defer(thinking=True)
        track_path = spotify_util.download_track(song_name)
        
        with open(track_path, "rb") as f:
            print("test", os.path.basename(track_path))
            discord_file = discord.file.File(f)
            discord_file.filename = os.path.basename(track_path)
            await interaction.followup.send(file=discord_file)
    except Exception as e:
        raise e
