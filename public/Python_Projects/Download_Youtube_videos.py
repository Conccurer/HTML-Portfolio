from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)
yd = yt.streams.get_highest_resolution()
print("Title: ",yt.title)
print("Views: ",yt.views)
print("Length: ",yt.length)
s = yt.length // 1000000
print("Download Size: ",s)
yd.download(r'C:\Users\aniru\OneDrive\Code\PYTHON\Games\Image')