from Button import *
from DropButton import DropButton
from Functionality.Board import *
from Functionality.Game import *


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
        self._buttons = self.createDropButtons()
        self._winnerClear = False

    def createStartButton(self):
        textColour = colours["BLACK"]
        buttonWidth = 200
        buttonHeight = 50
        buttonX = self._boardCornerX + self._boardWidth + (
                self._windowWidth - self._boardCornerX - self._boardWidth) / 2 - (buttonWidth / 2)
        buttonY = 50
        clickAction = lambda: self.startTheGame()  # lambda
        return Button(self._window, buttonX, buttonY, buttonWidth, buttonHeight, colours["GREEN"],
                      colours["LAWN GREEN"], ("START/RESET", 40, textColour), clickAction)

    def startTheGame(self):
        self.setButtonsState(True)
        self._winnerClear = True
        self._game.startGame(Player1)

    def setButtonsState(self, enabled):
        for i in range(ColumnCount):
            self._buttons[i].setEnabled(enabled)

    def createDropButtons(self):
        buttons = [None for i in range(7)]  # List Comprehensions
        textColour = colours["BLACK"]

        for i in range(ColumnCount):
            clickAction = lambda x: self.setCoin(x)  # lambda
            button = DropButton(self._window, self._boardCornerX + self._gap + i * 2 * (self._coinRadius + self._gap),
                                10,
                                2 * self._coinRadius, 2 * self._coinRadius, colours["SADDLE BROWN"],
                                colours["PERU"], (str(i + 1), 50, textColour), i, clickAction)
            button.setEnabled(False)
            buttons[i] = button
        return buttons

    def setCoin(self, column):
        try:
            self._game.dropToColumn(column)
        except FullColumnException as full:
            print(full.getMessage())

    def drawBackground(self, colour):
        pygame.draw.rect(self._window, colour,
                         (self._boardCornerX, self._boardCornerY, self._boardWidth, self._boardHeight))

    def drawingCoin(self, player, row, column):

        if (player == 1):
            colour = colours["DARK RED"]
        elif (player == 2):
            colour = colours["BRIGHT ORANGE"]
        else:
            colour = colours["BLACK"]

        x = self._boardCornerX + self._gap + self._coinRadius + 2 * column * (
                self._coinRadius + self._gap)
        y = self._boardCornerY + self._gap + self._coinRadius + 2 * row * (self._coinRadius + self._gap)

        pygame.draw.circle(self._window, colour,
                           (x, y), self._coinRadius)

    def createWinnerButton(self, winner):
        textColour = colours["BLACK"]
        buttonColour = colours["WHITE"]
        buttonWidth = 200
        buttonHeight = 50
        buttonX = self._boardCornerX + self._boardWidth + (
                self._windowWidth - self._boardCornerX - self._boardWidth) / 2 - (buttonWidth / 2)
        buttonY = 250
        if (winner == Player1):
            winner = "WYGRAL GRACZ 1"
            buttonColour = colours["DARK RED"]
        elif (winner == Player2):
            winner = "WYGRAL GRACZ 2"
            buttonColour = colours["BRIGHT ORANGE"]
        else:
            winner = "REMIS"

        return Button(self._window, buttonX, buttonY, buttonWidth, buttonHeight, buttonColour,
                      buttonColour, (winner, 30, textColour))

    def checkWinner(self):
        winner = self._game.getWinner()
        lastWinner = self.createWinnerButton(winner)
        if (winner != Empty):
            lastWinner.draw()
            self.setButtonsState(False)
        columnFull = 0
        for column in range(ColumnCount):
            if (winner == Empty and self._game.isColumnFull(column)):
                columnFull += 1
        if (winner == Empty and columnFull == 7):
            lastWinner.draw()
            self.setButtonsState(False)

    def createWhoseTurnButton(self, whoseTurn):
        textColour = colours["BLACK"]
        buttonColour = colours["WHITE"]
        buttonWidth = 200
        buttonHeight = 50
        buttonX = self._boardCornerX + self._boardWidth + (
                self._windowWidth - self._boardCornerX - self._boardWidth) / 2 - (buttonWidth / 2)
        buttonY = 150

        if (whoseTurn == Player1):
            whoseTurn = "TURA GRACZA 1"
            buttonColour = colours["DARK RED"]
        elif (whoseTurn == Player2):
            whoseTurn = "TURA GRACZA 2"
            buttonColour = colours["BRIGHT ORANGE"]
        else:
            whoseTurn = "WCISNIJ START"

        return Button(self._window, buttonX, buttonY, buttonWidth, buttonHeight, buttonColour,
                      buttonColour, (whoseTurn, 30, textColour))

    def whoseTurn(self):
        whose = self._game.getPlayerToThrow()
        button = self.createWhoseTurnButton(whose)
        button.draw()
