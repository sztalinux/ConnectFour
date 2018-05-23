import pygame
from Graphic.Colours import *

class Window:
    def __init__(self):
        pygame.init()
        self._windowWidth = 1280
        self._windowHeight = 720
        self._name = 'Connect Four'
        self._window = pygame.display.set_mode((self._windowWidth, self._windowHeight))
        pygame.display.set_caption(self._name)
        self._window.fill((colours["BLACK"]))
        #pygame.display.toggle_fullscreen

