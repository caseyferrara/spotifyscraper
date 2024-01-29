# Import necessary modules
from dotenv import load_dotenv
import os
import csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Load environment variables from the .env file
load_dotenv()

# Retrieve Spotify API credentials from environment variables
client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=credentials)

# Fetch the list of available genre seeds
genre_seeds = sp.recommendation_genre_seeds()

# Data structure to hold track information
tracks_data = []