from Functionality.Field import *
from Functionality.Board import *

class Winner:
    def __init__(self, board):
        self._board = board

    def getWinner(self):
        row = self.getRowWinner()
        column = self.getColumnWinner()
        diagonal = self.getDiagonalWinner()
        if (row != Empty):
            return row
        elif (column != Empty):
            return column
        elif (diagonal != Empty):
            return diagonal

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
        for column in range(selectedField.getColumn() + 1, ColumnCount, 1):
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
        for row in range(selectedField.getRow() + 1, RowCount, 1):
            if (self.getFieldState(row, column) == state):
                countToDown += 1
            else:
                break

        if (countToDown + 1 >= 4):
            return state

        return Empty

    def getDiagonalWinner(self):
        selectedField = self._board.getLastSelectedField()
        if (selectedField == None):
            return Empty

        row = selectedField.getRow()
        state = selectedField.getState()
        countOnTheLeftBottom = 0
        for column in range(selectedField.getColumn() - 1, -1, -1):
            row += 1
            if(row >= ColumnCount - 1):
                break
            elif(self.getFieldState(row, column) == state):
                countOnTheLeftBottom += 1
            else:
                break

        countOnTheRightTop = 0
        row = selectedField.getRow()
        for column in range(selectedField.getColumn() + 1, ColumnCount, 1):
            row -= 1
            if (row < 0):
                break
            elif (self.getFieldState(row, column) == state):
                countOnTheRightTop += 1
            else:
                break
        if (countOnTheLeftBottom + countOnTheRightTop + 1 >= 4):
            return state

        countOnTheLeftTop = 0
        row = selectedField.getRow()
        for column in range(selectedField.getColumn() -1, -1, -1):
            row -= 1
            if (row < 0):
                break
            elif (self.getFieldState(row, column) == state):
                countOnTheLeftTop += 1
            else:
                break

        countOnTheRightBottom = 0
        row = selectedField.getRow()
        for column in range(selectedField.getColumn() + 1, ColumnCount, 1):
            row += 1
            if (row >= ColumnCount - 1):
                break
            elif (self.getFieldState(row, column) == state):
                countOnTheRightBottom += 1
            else:
                break

        if (countOnTheLeftTop + countOnTheRightBottom + 1 >= 4):
            return state

        return Empty

    def getFieldState(self, row, column):
        return self._board.getField(row, column).getState()
