import pygame

from Button import Button
from Graphic.Window import *

class DropButton(Button):
    def __init__(self, window, x, y, width, height, normalColour, highligtedColour, text, column, action=None):
        super().__init__(window, x, y, width, height, normalColour, highligtedColour, text, lambda: action(column)) #lambda

