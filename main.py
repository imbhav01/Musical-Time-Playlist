from autoscraper import AutoScraper
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

url = "https://www.billboard.com/charts/hot-100/" + date

wanted_list = ["Last Night"]

scraper = AutoScraper()
scraper.build(url, wanted_list)
result = scraper.get_result_similar(url=url)
print(result)
print(len(result))

client_id = "701e8acc51ce48bcaa505516d2bfc831"
client_secret = "c9cd54b399e2433587d1502f7c35c06e"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


song_urls = []
for song_name in result:
    result = sp.search(q=song_name, limit=1, type='track')
    track = result['tracks']['items'][0]
    song_urls.append(track['external_urls']['spotify'])
print(song_urls)

playlist_name = f"{date} Billboard 100"

playlist = sp.user_playlist_create(user='31wc6cbrhklzmu6dlemx3dzjzvka', name=playlist_name, public=False)
playlist_id = playlist['id']

track_ids = [url.split('/')[-1] for url in song_urls]

sp.user_playlist_add_tracks(user='31wc6cbrhklzmu6dlemx3dzjzvka', playlist_id=playlist_id, tracks=track_ids)
