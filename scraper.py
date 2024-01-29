# Import necessary modules
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Load environment variables from the .env file
load_dotenv()

# Retrieve Spotify API credentials from environment variables
client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

# Set up authentication credentials for Spotify
credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

# Initialize the Spotipy client with our credentials
sp = spotipy.Spotify(client_credentials_manager=credentials)

# Search for tracks by the Beatles and limit results to 20
results = sp.search(q='Beatles', limit=20)

# Iterate through the search results and print the track names
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])