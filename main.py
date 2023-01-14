import tkinter
import customtkinter
from pytube import YouTube

# Download function
def start_download():
    try:
        yt_link = link.get()
        yt_object = YouTube(yt_link, on_progress_callback=on_progress)
        video = yt_object.streams.get_highest_resolution()
        video.download()
        title.configure(text=yt_object.title, text_color="white")
        finishLabel.configure(text="Downloaded!")

    except:
        print("Youtube link is invalid")
        finishLabel.configure(text="Invalid link or Download error!", text_color="red")

# System settings
customtkinter.set_appearance_mode("System") # Setting the dark or light mode from the system
customtkinter.set_default_color_theme("blue")

# Adding progress bar
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(percentage_of_completion)
    per = str(int(percentage_of_completion))
    p_percentage.configure(text=per + '%')
    p_percentage.update()


# Update progress bar
progress_bar.set(float(percentage_of_completion))

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

# Progress percentage
p_percentage = customtkinter.CTkLabel(app, text="0%")
p_percentage.pack()

progress_bar = customtkinter.CTkProgressBar(app, 400)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

# Download button
download = customtkinter.CTkButton(app, text="Download", command=start_download) # Run function
download.pack(padx=10, pady=10) # .pack is used to make elements show up on the screen

# Run app
app.mainloop()