import pytubefix
from pytubefix.cli import on_progress
import pytubefix
#input("enter video url:")
path=r"C:\Users\ERDİNÇ\Desktop\python ile indirilen videolar"

url=input("enter video's url:")
 
yt = YouTube(url, on_progress_callback = on_progress)
print(yt.title)
 
ys = yt.streams.get_lowest_resolution(url)
ys.download(path)