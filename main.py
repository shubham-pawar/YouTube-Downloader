import tkinter
import customtkinter
from pytube import YouTube

# High Resolution Video download function
def startDownloadVideo():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color='white')
        finishLabel.configure(text='')
        video.download()
        finishLabel.configure(text='High Resolution Video Downloaded')
    except:
        finishLabel.configure(text='Download error', text_color='red')

# download audio file
def startDownloadAudio():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytObject.streams.get_audio_only()

        title.configure(text=ytObject.title, text_color='white')
        finishLabel.configure(text='')
        video.download()
        finishLabel.configure(text='Audio Downloaded')
    except:
        finishLabel.configure(text='Download error', text_color='red')

# High Resolution Video download function
def startDownloadSDVideo():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytObject.streams.get_lowest_resolution()

        title.configure(text=ytObject.title, text_color='white')
        finishLabel.configure(text='')
        video.download()
        finishLabel.configure(text='Standard Resolution Video Downloaded')
    except:
        finishLabel.configure(text='Download error', text_color='red')

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    # update progress bar
    progressBar.set(float(percentage_of_completion)/100)

# system settings
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('dark-blue')

# our app frame
app = customtkinter.CTk()
app.geometry('720x400')
app.title('YouTube Downloder')

# adding UI elements
title = customtkinter.CTkLabel(app, text='Paste a youtube link below', font=("Proxima Nova", 30))
title.pack(padx=15, pady=15)

# add app icon
# app.wm_iconbitmap('yt.ico')

# link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=360, height=40, textvariable=url_var)
link.pack()

# finish downloading
finishLabel = customtkinter.CTkLabel(app, text='')
finishLabel.pack()

# progress bar
pPercentage = customtkinter.CTkLabel(app, text='0%')
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=360)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# download button
download = customtkinter.CTkButton(app, text='Download HD Video', command=startDownloadVideo, fg_color="#c20e0e", hover_color='#b50b0b', corner_radius=11, height=40)
download.pack(padx=10, pady=10)

# download button
download = customtkinter.CTkButton(app, text='Download Audio', command=startDownloadAudio, fg_color='#c20e0e', hover_color='#b50b0b', corner_radius=11, height=40)
download.pack(padx=10, pady=10)

# download button
download = customtkinter.CTkButton(app, text='Download SD Video', command=startDownloadSDVideo, fg_color="#c20e0e", hover_color='#b50b0b', corner_radius=11, height=40)
download.pack(padx=10, pady=10)

# run app
app.mainloop()
