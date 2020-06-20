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
        #print(link)
        playlist.append(link)

playlist = list(dict.fromkeys(playlist))
print(len(playlist))

video_quality = input("Enter the video quality to download (1080p,720p,360p,240p,144p): ")
for link in playlist:
    yt = YouTube(link)
    videos = yt.streams.filter(mime_type="video/mp4", res=video_quality)
    video = videos[0]
    video.download("Desktop")
    print(yt.title + "has been downloaded.")
