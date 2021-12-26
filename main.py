import pygame.display

from player import Player
from move import Movement
from background import Background
from button import Button
from modules import *


class Main:
    def __init__(self):
        pygame.init()
        running = True
        screen = pygame.display.set_mode([ 500, 500])
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()


window = Main()