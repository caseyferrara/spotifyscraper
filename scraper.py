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

# Fetch tracks for each genre and store their details
for genre in genre_seeds['genres']:
    recommendations = sp.recommendations(seed_genres=[genre], limit=100) # Limit of tracks per genre
    for track in recommendations['tracks']:
        track_info = {
            'genre': genre,
            'track_name': track['name'],
            'artist_name': track['artists'][0]['name'],
            'album_name': track['album']['name'],
            'release_date': track['album']['release_date'],
            'track_duration_ms': track['duration_ms'],
            'popularity': track['popularity'],
            'explicit': track['explicit'],
            'spotify_uri': track['uri'],
        }
        tracks_data.append(track_info)

# Writing to a CSV file
csv_file = "spotify_tracks.csv"
csv_columns = ['genre', 'track_name', 'artist_name', 'album_name', 'release_date', 
               'track_duration_ms', 'popularity', 'explicit', 'spotify_uri']

try:
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in tracks_data:
            writer.writerow(data)
except IOError:
    print("I/O error")