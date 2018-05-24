import pygame
from Graphic.Drawing import *
from Functionality.Board import *
from Functionality.Winner import *


class Game():
    def __init__(self):
        self._board = Board()
        self._winner = Winner(self._board)
        self._playerToThrow = Empty

    def startGame(self, player):
        self._playerToThrow = player
        self._board.reset()

    def getPlayerToThrow(self):
        return self._playerToThrow

    def getWinner(self):
        return self._winner.getWinner()

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
