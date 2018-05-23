class Field:
    def __init__(self, row, column, state):
        self._row = row
        self._column = column
        self._state = state

    def getRow(self):
        return self._row

    def getColumn(self):
        return self._column

    def getState(self):
        return self._state

Empty = 0
Player1 = 1
Player2 = 2
