from Functionality.Field import *

class WinnerInRule4:
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