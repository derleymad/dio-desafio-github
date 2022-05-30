from pytube import YouTube

link = str(input("Digite o link do video:"))
youtube = YouTube(link)
youtube.streams.get_highest_resolution().download()
