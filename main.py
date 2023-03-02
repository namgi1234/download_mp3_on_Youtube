from pytube import YouTube
import os

#Youtube video link to download mp3 file
urls = []

#download Music with input url
def downloadMusic (url):
    yt = YouTube(url)
    
    # extract only audio
    video = yt.streams.filter(only_audio=True).first()

    # download the file
    out_file = video.download()
    
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    
    # result of success
    print(yt.title + " has been successfully downloaded.")

for i in urls :
    downloadMusic(i)
