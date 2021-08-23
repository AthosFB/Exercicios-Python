import pygame
pygame.mixer.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.03)
while(pygame.mixer.music.get_busy()): pass
