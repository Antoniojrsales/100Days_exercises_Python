# Crie um programa que abra e reproduza o audio de um arquivo mp3

import pygame as py

py.init()
py.mixer.music.load('music.mp3')
py.mixer.music.play()
py.event.wait()

