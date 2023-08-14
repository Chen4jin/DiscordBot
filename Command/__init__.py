from .download import *


@client.event
async def on_ready():
    """_summary_
    Check bot succussfully started
    """
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')
