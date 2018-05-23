from Button import *
from DropButton import DropButton
from Functionality.Board import *
from Functionality.Game import *

RowCount = 6
ColumnCount = 7


class Drawing(Window):

    def __init__(self):
        super().__init__()
        self._coinRadius = 45
        self._gap = 5
        self._boardWidth = ColumnCount * 2 * (self._coinRadius + self._gap)
        self._boardHeight = RowCount * 2 * (self._coinRadius + self._gap)
        self._boardCornerX = 100
        self._boardCornerY = 100
        self._game = Game()
        self._startButton = self.createStartButton()
        self._buttons = self.createButtons()
        self._rulesButton = self.createRulesButtons()

    def drawingBoard(self):

        colour = colours["MUSTARD"]
        self.drawBackground(colour)

        self._startButton.draw()
        for i in range(ColumnCount):
            button = self._buttons[i]
            button.draw()
            for j in range(RowCount):
                state = self._game.getField(j, i).getState()
                self.drawingCoin(state, j, i)
        self.checkWinner()

    def createStartButton(self):
        textColour = colours["BLACK"]
        buttonWidth = 200
        buttonHeight = 50
        buttonX = self._boardCornerX + self._boardWidth + (
                self._windowWidth - self._boardCornerX - self._boardWidth) / 2 - (buttonWidth / 2)
        buttonY = 100
        return Button(self._window, buttonX, buttonY, buttonWidth, buttonHeight, colours["BRIGHT GREEN"],
                      colours["GREEN"], ("START/RESET", 40, textColour), self.startGame)

    def startGame(self):
        self.setButtonsState(True)
        self._game.startGame(Player1)


    def setButtonsState(self, enabled):
        for i in range(ColumnCount):
            self._buttons[i].setEnabled(enabled)

    def createButtons(self):
        buttons = [None for i in range(7)]  # List Comprehensions
        textColour = colours["BLACK"]
        for i in range(ColumnCount):
            clickAction = lambda x: self.setCoin(x)  # lambda
            button = DropButton(self._window, self._boardCornerX + self._gap + i * 2 * (self._coinRadius + self._gap),
                                10,
                                2 * self._coinRadius, 2 * self._coinRadius, colours["BRIGHT GREEN"],
                                colours["GREEN"], (str(i + 1), 50, textColour), i, clickAction)
            button.setEnabled(False)
            buttons[i] = button
        return buttons

    def setCoin(self, column):
        self._game.dropToColumn(column)

    def createRulesButtons(self):
        pass

    def drawBackground(self, colour):
        pygame.draw.rect(self._window, colour,
                         (self._boardCornerX, self._boardCornerY, self._boardWidth, self._boardHeight))

    def drawingCoin(self, player, row, column):

        if (player == 1):
            colour = colours["BLUE"]
        elif (player == 2):
            colour = colours["RED"]
        else:
            colour = colours["BLACK"]

        x = self._boardCornerX + self._gap + self._coinRadius + 2 * column * (
                self._coinRadius + self._gap)
        y = self._boardCornerY + self._gap + self._coinRadius + 2 * row * (self._coinRadius + self._gap)

        pygame.draw.circle(self._window, colour,
                           (x, y), self._coinRadius)

    def createWinnerButton(self, winner):
        textColour = colours["BLACK"]
        buttonWidth = 200
        buttonHeight = 50
        buttonX = self._boardCornerX + self._boardWidth + (
                self._windowWidth - self._boardCornerX - self._boardWidth) / 2 - (buttonWidth / 2)
        buttonY = 200
        if (winner == Player1):
            winner = "WYGRAL GRACZ NR 1"
        elif (winner == Player2):
            winner = "WYGRAL GRACZ NR 2"
        else:
            winner = "REMIS"

        return Button(self._window, buttonX, buttonY, buttonWidth, buttonHeight, colours["WHITE"],
                      colours["WHITE"], (winner, 25, textColour))

    def checkWinner(self):
        winner = self._game.getWinner()
        if (winner != Empty):
            lastWinner = self.createWinnerButton(winner)
            lastWinner.draw()
            self.setButtonsState(False)