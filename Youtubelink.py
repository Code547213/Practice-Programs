from pytube import YouTube
import os
from pathlib import Path


link=input("enter the youtube link: ")
choice=input("Enter 'a' for audio / 'v' for video:")
while(choice!="a" and choice!="v"):
    print("Enter correct choice!")
    choice=input("Enter 'a' for audio / 'v' for video:")


if choice=="a":
    audio=YouTube(link)
    print("Please Wait for minutes.......")
    downloads_path = str(Path.home() / "Downloads")
    # download the video and store it in a folder called "YoutubeAudios" inside the downloads folder
    audio.streams.get_audio_only().download(output_path=os.path.join(downloads_path, 'YoutubeAudios'))
    print("Open Downloads and Under YoutubeAudios, You will find the audio")
    

 # download the video and store it in a folder called "YoutubeVideos" inside the downloads folder
if choice=="v":
    video=YouTube(link)
    downloads_path = str(Path.home() / "Downloads")
    print("Please Wait for minutes.......")
    video.streams.get_by_resolution("720p").download(output_path=os.path.join(downloads_path, 'YoutubeVideos'))
    print("Open Downloads and Under YoutubeVideos, You will find the video")
