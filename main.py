import tkinter
import customtkinter
from pytube import YouTube


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

# Run app
app.mainloop()