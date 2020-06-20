from pytube import YouTube
import bs4
import requests

playlist = []
url = input("Enter Youtube Playlist URL: ")
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text,'html.parser')

for links in soup.find_all('a'):
    link = links.get('href')
    if(link[0:6]=="/watch" and link[0]!="#"):
        link="https://www.youtube.com"+link
        link = str(link)
        playlist.append(link)

#print(playlist)