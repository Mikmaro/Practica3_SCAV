# Mario Fernández
# Exercise 4

import os
import wget

"""
Solo será necesario poner el número de puerto como input para poder
obtener la IP de broadcast. Hay algunos que quizás no lleguen a
funcionar (algunos ya están reservados por ejemplo)
"""


def choose_ip(ip_stream):
    url = 'https://drive.google.com/uc?export=download&id=1Q_2GU4RXvqo7OnLe41Tc0WvYzOwiafYI'

    wget.download(url)  # Vídeo descargado --> cut_video_12_seconds.mp4

    # El hecho de utilizar '' + ip_stream  permite introducir la variable de
    # input dentro de la comanda, para luego que sea leída desde la terminal de Ubuntu
    cmd = 'ffmpeg -i cut_video_12_seconds.mp4 -preset ultrafast -vcodec libx264 -tune zerolatency -b 900k -f ' \
          'mpegts udp://@10.1.0.102:'+ip_stream
    os.system(cmd)


if __name__ == '__main__':
    ip_stream = str(input("Escoga la IP: "))
    choose_ip(ip_stream)
