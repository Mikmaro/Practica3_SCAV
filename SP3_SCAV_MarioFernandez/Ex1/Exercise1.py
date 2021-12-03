# Mario Fernández
# Exercise 1

"""
He utilizado el mismo mecanismo del wget para que no tengas que descargar nignún vídeo,
solo compilando el script se descargan y se crean los vídeos deseados
"""

import os
import wget


class exercise1:  # Esta será la clase para este ejercicio
    def convert_BBB160_120(self):
        url1 = 'https://drive.google.com/uc?export=download&id=1479CloANhLCHJlw7zW12VKPIaO9jKed2'

        wget.download(url1)  # Vídeo descargado --> BBB160_120.mp4

        cmd0 = 'ffmpeg -i BBB160_120.mp4 -c:v libvpx -b:v 1M -c:a libvorbis vp8_BBB160_120.webm'
        os.system(cmd0)  # convertir a VP8

        cmd1 = 'ffmpeg -i BBB160_120.mp4 -c:v libvpx-vp9 -b:v 2M vp9_BBB160_120.webm'
        os.system(cmd1)  # convertir a VP9

        cmd2 = 'ffmpeg -i BBB160_120.mp4 -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k h265_BBB160_120.mp4'
        os.system(cmd2)  # convertir a h265

        cmd3 = 'ffmpeg -i BBB160_120.mp4 -c:v libaom-av1 -crf 30 -b:v 0 av1_BBB160_120.mkv'
        os.system(cmd3)  # convertir a AV1

    def convert_BBB360_240(self):
        url2 = 'https://drive.google.com/uc?export=download&id=1nq005wqEWG9HILbXvbc2IuAuRyhH6Kpa'

        wget.download(url2)  # Vídeo descargado --> BBB360_240.mp4

        cmd0 = 'ffmpeg -i BBB360_240.mp4 -c:v libvpx -b:v 1M -c:a libvorbis vp8_BBB360_240.webm'
        os.system(cmd0)  # convertir a VP8

        cmd1 = 'ffmpeg -i BBB360_240.mp4 -c:v libvpx-vp9 -b:v 2M vp9_BBB360_240.webm'
        os.system(cmd1)  # convertir a VP9

        cmd2 = 'ffmpeg -i BBB360_240.mp4 -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k h265_BBB360_240.mp4'
        os.system(cmd2)  # convertir a h265

        cmd3 = 'ffmpeg -i BBB360_240.mp4 -c:v libaom-av1 -crf 30 -b:v 0 av1_BBB360_240.mkv'
        os.system(cmd3)  # convertir a AV1

    def convert_BBB480p(self):
        url3 = 'https://drive.google.com/uc?export=download&id=1V5JDd_U7eErNmr056JwxwF-XQ5I0laBU'

        wget.download(url3)  # Vídeo descargado --> BBB480p.mp4

        cmd0 = 'ffmpeg -i BBB480p.mp4 -c:v libvpx -b:v 1M -c:a libvorbis vp8_BBB480p.webm'
        os.system(cmd0)  # convertir a VP8

        cmd1 = 'ffmpeg -i BBB480p.mp4 -c:v libvpx-vp9 -b:v 2M vp9_BBB480p.webm'
        os.system(cmd1)  # convertir a VP9

        cmd2 = 'ffmpeg -i BBB480p.mp4 -c:v libx265 -crf 26 -preset fast -c:a aac -b:a 128k h265_BBB480p.mp4'
        os.system(cmd2)  # convertir a h265

        cmd3 = 'ffmpeg -i BBB480p.mp4 -c:v libaom-av1 -crf 30 -b:v 0 av1_BBB480p.mkv'
        os.system(cmd3)  # convertir a AV1

    def convert_BBB720p(self):
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


if __name__ == '__main__':
    ex1 = exercise1()  # crear nueva instancia de la clase para utilizar las siguientes funciones
    ex1.convert_BBB160_120()
    ex1.convert_BBB360_240()
    ex1.convert_BBB480p()
    ex1.convert_BBB720p()
    # se crearan 4 vídeos de cada función, por lo que al final resultarán 16 vídeos
