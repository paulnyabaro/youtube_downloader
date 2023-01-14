import tkinter
import customtkinter
from pytube import YouTube

# Download function
def start_download():
    try:
        yt_link = link.get()
        yt_object = YouTube(yt_link)
        video = yt_object.streams.get_highest_resolution()
        video.download()
    except:
        print("Youtube link is invalid")
        finishLabel.configure(text="Download error!")

    finishLabel.configure(text="Downloaded!")

# System settings
customtkinter.set_appearance_mode("System") # Setting the dark or light mode from the system
customtkinter.set_default_color_theme("blue")


# Our app frame
app = customtkinter.CTk() # Initializing the app
app.geometry("720x480") # Setting the app size
app.title("Youtube Downloader")


# Adding UI elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=10, pady=10) # Padding for x and y

# Link input
url_var = tkinter.StringVar() # Getting the value of the link input
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var) # app is where to place it -> inside the app
link.pack()

# Finished downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Download button
download = customtkinter.CTkButton(app, text="Download", command=start_download) # Run function
download.pack(padx=10, pady=10) # .pack is used to make elements show up on the screen

# Run app
app.mainloop()