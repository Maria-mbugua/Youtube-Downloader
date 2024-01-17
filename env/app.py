# import customtkinter
import customtkinter as ctk

# this is for creating a combo box
from tkinter import ttk

# this is for connecting youtube to get the url and to download the video
from pytube import YouTube

# this is for navigating the downloaded video into a specific path under the project folder
import os

# create download video function
def download_video():
#     print('Clicked')
    url = entry_url.get()
    # print(url)
    resolution = resolutions_var.get()

    progress_label.pack(pady=(int("10"), int("5")))
    progress_bar.pack(pady=(int("10"), int("5")))
    status_label.pack(pady=(int("10"), int("5")))

# create youtube object open the url and supply the url to it
    try:
        # yt = YouTube(url)
        yt = YouTube(url, on_progress_callback=on_progress)
        stream = yt.streams.filter(res=resolutions).first()
        # print(yt.title)

        # download the video into a specific directory
        os.path.join("downloads", f"(yt.title).mp4")
        stream.download(output_path="downloads")

        status_label.configure(text="Downloaded", text_color ="white", fg_color ="green")

        # stream.download()
    except Exception as e:
        # print()
        status_label.configure(text=f"error{str(e)}", text_color ="white", fg_color ="red")

# function to provide stream, chunk and bytes
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_comleted = bytes_downloaded / total_size * 100
    # print(percentage_comleted)

    # update label and progress bar
    progress_label.configure(text= str(int(percentage_comleted)) + "%")
    progress_label.update()

    progress_bar.set(float(percentage_comleted / 100))

# create a root window
root = ctk.CTk()
ctk.set_appearance_mode('System') # set appearance mode
ctk.set_default_color_theme("blue") # set color

# title of the window
root.title("YouTube Downloader!")

# set min and max length of the width and the height
root.geometry("720x480")
root.minsize(720,480)
root.maxsize(1080,720)

# create a frame to hold the content
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

# create a label and the entry widget for the url
url_label = ctk.CTkLabel(content_frame, text="Enter the youtube url here : ")
entry_url = ctk.CTkEntry(content_frame, width=400, height=40)
url_label.pack(pady=(int("10"), int("5")))
entry_url.pack(pady=(int("10"), int("5")))

# create a download button
download_button = ctk.CTkButton(content_frame, text="Download", command=download_video)
download_button.pack(pady=(int("10"), int("5")))

# create a resultions combobox
resolutions = (int("720"), int("360"),int("240"))
resolutions_var = ctk.StringVar() 
resultion_combobox = ttk.Combobox(content_frame, values= resolutions, textvariable=resolutions_var)
resultion_combobox.pack(pady=(int("10"), int("5")))
resultion_combobox.set(int("720"))

# create a label and the progress bar to dispaly the download progress
progress_label= ctk.CTkLabel(content_frame, text="100%")
# progress_label.pack(pady=(int("10"), int("5")))

progress_bar= ctk.CTkProgressBar(content_frame, width=400)
# progress_bar.set(0.6)
progress_bar.set(1)
# progress_bar.pack(pady=(int("10"), int("5")))

# create the status label
# status_label= ctk.CTkLabel(content_frame, text="Downloaded")
status_label= ctk.CTkLabel(content_frame, text="")
# status_label.pack(pady=(int("10"), int("5")))

# to start the app
root.mainloop()

