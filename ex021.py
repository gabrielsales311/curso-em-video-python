'''import pygame

pygame.init()
pygame.mixer.music.play('ex021.mp3')
pygame.event.music.wait()'''

from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
input()

