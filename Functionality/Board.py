from Functionality.Field import *


class Board:
    RowCount = 6
    ColumnCount = 7

    def __init__(self):
        self.reset()

    def reset(self):
        self._lastSelectedField = None
        self._fields = [[Field(i, j, Empty) for i in range(self.ColumnCount)] for j in range(self.RowCount)] #List Comprehensions

    def dropToColumn(self, column, state):
        selectedField = None
        for i in range(self.RowCount - 1, -1, -1):
            if (self._fields[i][column].getState() == Empty):
                selectedField = Field(i, column, state)
                self._fields[i][column] = selectedField
                break
        ## zamiast tego wyjatku zrobic dany przycisk disabled
        if (selectedField == None):
            raise Exception("Cannot throw to column " + column + " because it is full")

        self._lastSelectedField = selectedField

    def getField(self, row, column):
        return self._fields[row][column]

    def getLastSelectedField(self):
        return self._lastSelectedField
