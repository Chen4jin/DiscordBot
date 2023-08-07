import os
import subprocess

from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from pydub import AudioSegment
from pydub.playback import play 


class SpotifyUtil:
    
    def __init__(self) -> None:
        self.spotify_connector = Spotify(client_credentials_manager=SpotifyClientCredentials())
        self.output_dir = "./TrackVault/"
    
    def get_track(self, track_name: str) -> dict:
        return self.spotify_connector.search(track_name, type="track", limit=1)
    
    def download_track(self, track_name: str) -> None:
        track_info = self.get_track(track_name=track_name)
        
        try:
            items = track_info.get("tracks", {}).get("items", [])[0]
            url = items.get("external_urls").get("spotify")
            print(url)
            subprocess.check_call(f"spotify_dl -V -l {url} -o {self.output_dir}", shell=True)
            """ for file_info in os.walk(f"{self.output_dir}"):
                if file_info[2] and ".mp3" in file_info[2][0]:
                    track_path = os.path.join(file_info[0].replace("/", "\\"), file_info[2][0])
                    track = AudioSegment.from_file(track_path, "mp3")
                    play(track)"""

        except Exception as e:
            raise e
