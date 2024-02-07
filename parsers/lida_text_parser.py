import requests

import config
from yandex_music import Client

TOKEN = config.YANDEX_MUSIC_TOKEN

client = Client(TOKEN).init()

tracks = client.artists_tracks('7714432')

for track_id in [track['id'] for track in tracks]:
    text_download_url = client.tracks_lyrics(track_id, format='TEXT')['download_url']
    if text_download_url:
        text = requests.get(text_download_url).text
        with open(f'../texts/{track_id}.txt', 'w', encoding='utf-8') as file:
            file.write(text)
