import os
import subprocess

from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyUtil:
    def __init__(self) -> None:
        self.spotify_connector = Spotify(client_credentials_manager=SpotifyClientCredentials())
        self.output_dir = "./TrackVault/"
    
    def get_track(self, track_name: str) -> dict:
        return self.spotify_connector.search(track_name)
    
    def download_track(self, track_name: str) -> str:
        track_info = self.get_track(track_name=track_name)
        items = track_info.get("tracks", {}).get("items", [])[0]
        url = items.get("external_urls").get("spotify")
        items_name = items.get("name", "")
    
        try:
            subprocess.check_call(f"spotify_dl -l {url} -o {self.output_dir}", shell=True)
        except Exception as exception:
            raise exception
        
        file_name = os.listdir(os.path.join(self.output_dir, items_name))[0]
        file_path = os.path.join(self.output_dir, items_name, file_name)
        return file_path
