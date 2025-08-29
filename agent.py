import os # lets us access environment variables
import spotipy  # wrapper for the Spotify Web API
from spotipy.oauth2 import SpotifyClientCredentials  # will let us authenticate
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env file

# get credentials from env and create a spotipy client that is powered by the auth manager
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")
))

# helper function to extract relevant track information
def get_track_info(track):
    return {
        "name": track.get("name", "Unknown Track"),
        "artist": track["artists"][0]["name"] if track.get("artists") else "Unknown Artist",
        "album": track["album"]["name"] if "album" in track else "Unknown Album",
        "url": track["external_urls"]["spotify"],
        "album_art_url": track["album"]["images"][0]["url"] if track.get("album") and track["album"].get("images") else None

    }

# function that returns relevant tracks based on a search query
def track_search(query, limit=5):
    results = sp.search(q=query, limit=limit, type="track")
    tracks = []
    for song in results["tracks"]["items"]:
        tracks.append(get_track_info(song))
    return tracks
