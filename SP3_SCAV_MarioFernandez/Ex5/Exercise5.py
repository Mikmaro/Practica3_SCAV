# Mario Fernández
# Exercise 5

"""
Ejercicio extra para hacer el menú.
Para los ejercicios 3 y 4 se debería tener una segunda terminal abierta
para poder ejecutar la comanda de ffplay

Hay que tener en cuenta que si se ejecuta la primera ocpión (tecla [1]) se
hace también la conversión a AV1 (a parte de las otras tres), donde la conversión
a AV1 suele tardar muchísimo tiempo.
"""

import os
import wget


# ex1
def convert_BBB720p():
    url4 = 'https://drive.google.com/uc?export=download&id=1WvUX1LIPwwsmfaVCdA0mhYzxPTUv9BWk'

    wget.download(url4)  # Vídeo descargado --> BBB720p.mp4

    cmd0 = 'ffmpeg -i BBB720p.mp4 -c:v libvpx -b:v 1M -c:a libvorbis vp8_BBB720p.webm'
    os.system(cmd0)  # convertir a VP8

    cmd1 = 'ffmpeg -i BBB720p.mp4 -c:v libvpx-vp9 -b:v 2M vp9_BBB720p.webm'
    os.system(cmd1)  # convertir a VP9

    cmd2 = 'ffmpeg -i BBB720p.mp4 -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k h265_BBB720p.mp4'
    os.system(cmd2)  # convertir a h265

    cmd3 = 'ffmpeg -i BBB720p.mp4 -c:v libaom-av1 -crf 30 -b:v 0 av1_BBB720p.mkv'
    os.system(cmd3)  # convertir a AV1


# ex2
def comparison_BBB720p():
    url4 = 'https://drive.google.com/uc?export=download&id=1WvUX1LIPwwsmfaVCdA0mhYzxPTUv9BWk'

    wget.download(url4)  # Vídeo descargado --> BBB720p.mp4

    cmd0 = 'ffmpeg -i BBB720p.mp4 -c:v libvpx -b:v 1M -c:a libvorbis vp8_BBB720p.webm'
    os.system(cmd0)  # convertir a VP8

    cmd1 = 'ffmpeg -i BBB720p.mp4 -c:v libvpx-vp9 -b:v 2M vp9_BBB720p.webm'
    os.system(cmd1)  # convertir a VP9

    cmd2 = 'ffmpeg -i vp8_BBB720p.webm -i vp9_BBB720p.webm -filter_complex hstack comparison.webm'
    os.system(cmd2)


# ex3
def create_streaming():
    url = 'https://drive.google.com/uc?export=download&id=1Q_2GU4RXvqo7OnLe41Tc0WvYzOwiafYI'

    wget.download(url)  # Vídeo descargado --> cut_video_12_seconds.mp4

    cmd = 'ffmpeg -i cut_video_12_seconds.mp4 -preset ultrafast -vcodec libx264 -tune zerolatency -b 900k -f ' \
          'mpegts udp://@10.1.0.102:1234'
    os.system(cmd)


# ex4
def choose_ip(ip_stream):
    url = 'https://drive.google.com/uc?export=download&id=1Q_2GU4RXvqo7OnLe41Tc0WvYzOwiafYI'

    wget.download(url)  # Vídeo descargado --> cut_video_12_seconds.mp4

    cmd = 'ffmpeg -i cut_video_12_seconds.mp4 -preset ultrafast -vcodec libx264 -tune zerolatency -b 900k -f ' \
          'mpegts udp://@10.1.0.102:'+ip_stream
    os.system(cmd)


# ex5
def menu():
    os.system('clear')

    print("Selecciona una opción con las teclas [1][2][3][4], o [5] para salir:")

    print("\t[1] - Conversión del vídeo 720p en los formatos VP8, VP9, h265 y AV1")

    print("\t[2] - Comparación de VP8-VP9")

    print("\t[3] - Hacer streaming")

    print("\t[4] - Escoger IP de streaming")

    print("\t[5] - Salir")


if __name__ == '__main__':
    while True:
        menu()
        ejercicio_escogido = input("Selecciona ejercicio: ")

        if ejercicio_escogido == "1":
            convert_BBB720p()

        elif ejercicio_escogido == "2":

            comparison_BBB720p()

        elif ejercicio_escogido == "3":

            create_streaming()

        elif ejercicio_escogido == "4":

            ip_stream = str(input("Escoga la IP: "))
            choose_ip(ip_stream)

        elif ejercicio_escogido == "5":
            break

        else:
            input("Ese ejercicio no existe. Escoge de nuevo: ")
