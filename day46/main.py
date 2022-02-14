import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup

# BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
SPOTIFY_CID = os.getenv("SPOTIFY_CID")
SPOTIFY_PWD = os.getenv("SPOTIFY_PWD")
#
# travel_date = input("Which year do you want to travel to? type the date in this format YYYY-MM-DD")
# print(travel_date)
#
# res = requests.get(url=BILLBOARD_URL+travel_date)
# soup = BeautifulSoup(res.text, "html.parser")
# song_list = [title.text.replace("\n", "") for title in soup.select(selector=".o-chart-results-list__item > h3")]
# print(song_list)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CID,
                                               client_secret=SPOTIFY_PWD,
                                               redirect_uri="http://example.com",
                                               scope="user-library-read"))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])