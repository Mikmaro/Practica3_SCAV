# Mario Fernández
# Exercise 3

"""
Previamente se debería abrir un terminal para poder hacer la comanda

ffplay -i (IP)

En mi caso, he probado con el numero de IP udp://10.1.0.102:1234

He intentado hacer con VLC pero no ha habido manera, ya que en todo
momento se veía la pantalla en negro. Por eso he buscado la alternativa
de usar ffplay en una segunda terminal
"""

import os
import wget


def create_streaming():
    url = 'https://drive.google.com/uc?export=download&id=1Q_2GU4RXvqo7OnLe41Tc0WvYzOwiafYI'

    wget.download(url)  # Vídeo descargado --> cut_video_12_seconds.mp4

    cmd = 'ffmpeg -i cut_video_12_seconds.mp4 -preset ultrafast -vcodec libx264 -tune zerolatency -b 900k -f ' \
          'mpegts udp://@10.1.0.102:1234'
    # ejemplo de puerto que encontré en la documentación de ffmpeg. A parte también he añadido el @ para
    # que funcione correctamente
    os.system(cmd)


if __name__ == '__main__':
    create_streaming()
