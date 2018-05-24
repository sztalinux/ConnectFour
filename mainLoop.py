import sys

from Graphic.Drawing import *
from Graphic.Window import *


class mainLoop:
    def __init__(self):
        self._window = Drawing()
    def loop(self):



        while True:


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            colour = colours["PERU"]
            self._window.drawBackground(colour)
            self._window._startButton.draw()
            self._window.whoseTurn()
            for i in range(ColumnCount):
                button = self._window._buttons[i]
                button.draw()
                for j in range(RowCount):
                    state = self._window._game.getField(j, i).getState()
                    self._window.drawingCoin(state, j, i)
            self._window.checkWinner()

            pygame.display.flip()

