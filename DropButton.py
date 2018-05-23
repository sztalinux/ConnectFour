import pygame

from Button import Button
from Graphic.Window import *

class DropButton(Button):
    def __init__(self, window, x, y, width, height, normalColour, highligtedColour, column, action=None):
        super().__init__(window, x, y, width, height, normalColour, highligtedColour, lambda: action(column)) #lambda

