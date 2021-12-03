# Mario Fernández
# Exercise 2

"""
RESULTADO:
Debido a que el resultado es un .webm, la comparativa que encontramos es que no
hay claras diferencias entre los vídeos. Comentaría alguna diferencia, pero
viendo el vídeo varias veces no encuentro nada destacable que se diferencie entre
uno u otro, por el hecho del formato que se ha comentado anteriormente.
"""

import os
import wget


def comparison_BBB720p():
    # Primero he descargado el video 720p y he convertido el vídeo en
    # VP8 y VP9
    url4 = 'https://drive.google.com/uc?export=download&id=1WvUX1LIPwwsmfaVCdA0mhYzxPTUv9BWk'

    wget.download(url4)  # Vídeo descargado --> BBB720p.mp4

    cmd0 = 'ffmpeg -i BBB720p.mp4 -c:v libvpx -b:v 1M -c:a libvorbis vp8_BBB720p.webm'
    os.system(cmd0)  # convertir a VP8

    cmd1 = 'ffmpeg -i BBB720p.mp4 -c:v libvpx-vp9 -b:v 2M vp9_BBB720p.webm'
    os.system(cmd1)  # convertir a VP9

    # esta comanda permite visualizar a la vez dos vídeos (uno a la derecha y otro a la izquierda)
    cmd2 = 'ffmpeg -i vp8_BBB720p.webm -i vp9_BBB720p.webm -filter_complex hstack comparison.webm'
    os.system(cmd2)
    # vídeo izquierdo es el VP8 y el vídeo derecho es el VP9
    # El vídeo resultante es comparison.webm


if __name__ == '__main__':
    comparison_BBB720p()
