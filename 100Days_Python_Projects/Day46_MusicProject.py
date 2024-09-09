from bs4 import BeautifulSoup
import requests

date = input("Type date in the format YYYY-MM-DD: ")
print(date)

music = requests.get('https://www.billboard.com/charts/hot-100/' + date)
music_web = music.text

soup = BeautifulSoup(music_web, 'html.parser')
song_names_spans = soup.select("li ul li h3")

titles = [song.getText().strip() for song in song_names_spans]
print(titles)

with open('music_playlist.txt', 'w') as music_playlist:
    for music in titles:
        music_playlist.write(f"{music}\n")

import random 
print(random.choice(titles))