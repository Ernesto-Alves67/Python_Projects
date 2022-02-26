from moviepy.editor import *
import os
import re

pasta = r'D:\Playlist 10g\Yoshua E.m'

def rename_file(file):
    fname, fext = os.path.splitext(file)
    return fname, fext


def file_lop(root, dirs, files):
    for file in files:
        fi2 = rename_file(file)
        if '.mp3' in fi2:
            continue
        elif '.py' in fi2:
            continue
        mp4_file = f'{fi2[0]}.mp4'
        #
        mp3_file = f'{fi2[0]}.mp3'
        musV1 = VideoFileClip(mp4_file)

        audio1 = musV1.audio

        audio1.write_audiofile(mp3_file)
        musV1.close()
        audio1.close()

def main_loop():
    for root, dirs, files in os.walk(pasta):
        file_lop(root, dirs, files)


if __name__ == '__main__':
    main_loop()





# mp4_file = 'Oroboro and Yoshua.mp4'
#
# mp3_file = 'Oroboro and Yoshua.mp3'
#
#
