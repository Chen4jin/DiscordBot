import discord
from MusicBot import client
from ..SpotifyModule.SpotifyUtil import SpotifyUtil

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')


@client.tree.command()
async def download(interaction: discord.Interaction, song_name: str):
    """Download the song"""
    try:
        spotify_util = SpotifyUtil()
        await interaction.response.defer(thinking=True)
        spotify_util.download_track(song_name)
        
        with open("TrackVault\星辰大海\黄霄雲 - 星辰大海.mp3", "rb") as f:
            discord_file = discord.file.File(f)
            await interaction.followup.send(file=discord_file)
    except Exception as e:
        raise e

