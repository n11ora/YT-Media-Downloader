from tkinter import *
from yt_dlp import YoutubeDL
import os


if not os.path.exists('downloads'):
    os.makedirs('downloads')

def high_quality():
    try:
        url = entry.get()
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'downloads/%(title)s.%(ext)s'
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"Error downloading: {e}")


def low_quality():
    try:
        url = entry.get()
        ydl_opts = {
            'format': 'worst',
            'outtmpl': 'downloads/%(title)s.%(ext)s'
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"Error downloading: {e}")


def get_audio():
    try:
        url = entry.get()
        ydl_opts = {
            'format': 'bestaudio',
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"Error downloading: {e}")



window = Tk()
window.title("YouTube Downloader")
window.geometry("600x400")
window.configure(bg="pink")

label = Label(window, text="Add Your YouTube Link Here", font="bold", bg="pink")
label.place(x=225, y=30)

entry = Entry(window, width=55)
entry.place(x=153, y=70)

button1 = Button(window, text="High Quality", command=high_quality, font="bold", activeforeground="cornflowerblue", bg="#FF69b4")
button1.place(x=153, y=180)

button2 = Button(window, text="Low Quality", command=low_quality, font="bold", activeforeground="cornflowerblue", bg="#c8a2c8")
button2.place(x=400, y=180)

button3 = Button(window, text="Get Audio", command=get_audio, font="bold", activeforeground="cornflowerblue", bg="#dcae96")
button3.place(x=290, y=260)

window.mainloop()
