#Imports

import pytube as pt
from pytube import YouTube
import tkinter as tk
from tkinter import messagebox, simpledialog

#Initializing the window
root = tk.Tk()
root.withdraw()

try:
    #Link of the YouTube Video.
    link=simpledialog.askstring("Youtube Downloader","Enter the link of the video:")

    #Downloading the video.
    yt=YouTube(link)

    stream=yt.streams.get_highest_resolution()

    messagebox.showinfo("Youtube Downloader",f"Downloading {yt.title}")

    stream.download()

    messagebox.showinfo("Youtube Downloader","Download Completed")

except Exception as e:
    messagebox.showerror("Youtube Downloader",f"Sorry an error occured:\n{e}")
