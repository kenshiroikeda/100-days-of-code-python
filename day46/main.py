import os

import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import requests
from bs4 import BeautifulSoup

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
SPOTIFY_CID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIFY_PWD = os.getenv("SPOTIPY_CLIENT_SECRET")
SCOPE = 'user-library-read user-read-playback-state playlist-read-private user-read-recently-played playlist-read-collaborative playlist-modify-public playlist-modify-private'

travel_date = input("Which year do you want to travel to? type the date in this format YYYY-MM-DD")

res = requests.get(url=BILLBOARD_URL+travel_date)
soup = BeautifulSoup(res.text, "html.parser")
song_list = [title.text.replace("\n", "") for title in soup.select(selector=".o-chart-results-list__item > h3")]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CID,
                                               client_secret=SPOTIFY_PWD,
                                               redirect_uri="http://example.com",
                                               scope=SCOPE,
                                               cache_path="token.txt"))

uri_list = []

for song in song_list:
    results = sp.search(q=f'track:{song} year:{travel_date[0:4]}', type='track')
    items = results['tracks']['items']
    if len(items) > 0:
        album = items[0]
        uri_list.append(album['uri'])

playlist_title = f"{travel_date} Billboard 100"

user_id = sp.current_user()['id']

sp.user_playlist_create(user_id, playlist_title)
sp.playlist_add_items(playlist_id=sp.current_user_playlists()['items'][0]['id'], items = uri_list)