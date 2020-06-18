from pytube import YouTube
import bs4
import requests

playlist = []
url = input("Enter Youtube Playlist URL: ")
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text,'html.parser')

for links in soup.find_all('a'):
    link = links.get('href')
    