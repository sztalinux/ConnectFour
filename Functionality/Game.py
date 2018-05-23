import pygame
from Graphic.Drawing import *
from Functionality.Board import *


class Game():
    def __init__(self):
        self._board = Board()
        self._playerToThrow = Empty

    def startGame(self, player):
        self._playerToThrow = player
        self._board.reset()

    def getPlayerToThrow(self):
        return self._playerToThrow

    def getWinner(self):
        winner = self.getRowWinner()
        winner = self.getColumnWinner()
        if (winner != Empty):
            return winner

        return Empty

    def getRowWinner(self):
        selectedField = self._board.getLastSelectedField()
        if (selectedField == None):
            return Empty

        row = selectedField.getRow()
        state = selectedField.getState()
        countOnTheLeft = 0
        for column in range(selectedField.getColumn() - 1, -1, -1):
            if (self.getFieldState(row, column) == state):
                countOnTheLeft += 1
            else:
                break

        countOnTheRight = 0
        for column in range(selectedField.getColumn() + 1, self._board.ColumnCount, 1):
            if (self.getFieldState(row, column) == state):
                countOnTheRight += 1
            else:
                break

        if (countOnTheLeft + countOnTheRight + 1 >= 4):
            return state

        return Empty

    def getColumnWinner(self):
        selectedField = self._board.getLastSelectedField()
        if (selectedField == None):
            return Empty

        column = selectedField.getColumn()
        state = selectedField.getState()

        countToDown = 0
        for row in range(selectedField.getRow() + 1, self._board.RowCount, 1):
            if (self.getFieldState(row, column) == state):
                countToDown += 1
            else:
                break

        if (countToDown + 1 >= 4):
            return state

        return Empty

    def getFieldState(self, row, column):
        return self._board.getField(row, column).getState()

    def dropToColumn(self, column):
        self._board.dropToColumn(column, self._playerToThrow)
        self.switchPlayers()

    def getField(self, row, column):
        return self._board.getField(row, column)

    def isColumnFull(self, column):
        return self._board.getField(0, column).getState() != Empty

    def switchPlayers(self):
        if (self._playerToThrow == Player1):
            self._playerToThrow = Player2
        else:
            self._playerToThrow = Player1
