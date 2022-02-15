import os
from pprint import pprint

import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import requests
from bs4 import BeautifulSoup

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
SPOTIFY_CID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIFY_PWD = os.getenv("SPOTIPY_CLIENT_SECRET")

travel_date = input("Which year do you want to travel to? type the date in this format YYYY-MM-DD")

res = requests.get(url=BILLBOARD_URL+travel_date)
soup = BeautifulSoup(res.text, "html.parser")
song_list = [title.text.replace("\n", "") for title in soup.select(selector=".o-chart-results-list__item > h3")]

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

uri_list = []

for song in song_list:
    results = spotify.search(q=f'track:{song} year:{travel_date[0:4]}', type='track')
    items = results['tracks']['items']
    if len(items) > 0:
        album = items[0]
        uri_list.append(album['uri'])

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CID,
#                                                client_secret=SPOTIFY_PWD,
#                                                redirect_uri="http://example.com",
#                                                scope="user-library-read"))
#
# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])