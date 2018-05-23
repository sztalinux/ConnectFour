import sys

from Graphic.Drawing import *
from Graphic.Window import *


class mainLoop:
    def __init__(self):
        self._window = Window()

    def loop(self):

        window = Drawing()

        while True:


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            window.drawingBoard()
            pygame.display.flip()

