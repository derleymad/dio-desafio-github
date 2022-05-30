#Importando bibliotecas
from pytube import YouTube

#Entrada do usuário
link = str(input("Digite o link do video:"))

#Baixando video
youtube = YouTube(link)
youtube.streams.get_highest_resolution().download()
