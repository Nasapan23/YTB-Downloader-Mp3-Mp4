import os
import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

class YouTubeDownloader:
    def __init__(self, master):
        self.master = master
        master.title("YouTube Downloader")

        self.link_label = tk.Label(master, text="Enter YouTube link:")
        self.link_label.pack()

        self.link_entry = tk.Entry(master, width=50)
        self.link_entry.pack()

        self.mp4_button = tk.Button(master, text="Download MP4", command=self.download_mp4)
        self.mp4_button.pack()

        self.mp3_button = tk.Button(master, text="Download MP3", command=self.download_mp3)
        self.mp3_button.pack()

        self.folder_button = tk.Button(master, text="Choose Folder", command=self.choose_folder)
        self.folder_button.pack()

        self.status_label = tk.Label(master, text="")
        self.status_label.pack()

    def download_mp4(self):
        link = self.link_entry.get()
        path = self.folder_path

        if link and path:
            try:
                yt = YouTube(link)
                stream = yt.streams.filter(file_extension='mp4').first()
                stream.download(path)
                self.status_label.config(text="MP4 Download Complete")
            except Exception as e:
                self.status_label.config(text="Error: " + str(e))
        else:
            self.status_label.config(text="Please enter a link and choose a folder")

    def download_mp3(self):
        link = self.link_entry.get()
        path = self.folder_path

        if link and path:
            try:
                yt = YouTube(link)
                stream = yt.streams.filter(only_audio=True).first()
                stream.download(output_path=path, filename_prefix='audio')
                mp4_filename = stream.default_filename
                mp3_filename = mp4_filename.replace('.mp4', '.mp3')
                os.rename(os.path.join(path, mp4_filename), os.path.join(path, mp3_filename))
                self.status_label.config(text="MP3 Download Complete")
            except Exception as e:
                self.status_label.config(text="Error: " + str(e))
        else:
            self.status_label.config(text="Please enter a link and choose a folder")

    def choose_folder(self):
        self.folder_path = filedialog.askdirectory()
        self.status_label.config(text="Selected Folder: " + self.folder_path)

if __name__ == '__main__':
    root = tk.Tk()
    downloader = YouTubeDownloader(root)
    root.mainloop()
