from Functionality.Field import *
from Exceptions import *

RowCount = 6
ColumnCount = 7

class Board:


    def __init__(self):
        self.reset()

    def reset(self):
        self._lastSelectedField = None
        self._fields = [[Field(i, j, Empty) for i in range(ColumnCount)] for j in range(RowCount)] #List Comprehensions

    def dropToColumn(self, column, state):
        selectedField = None
        for i in range(RowCount - 1, -1, -1):
            if (self._fields[i][column].getState() == Empty):
                selectedField = Field(i, column, state)
                self._fields[i][column] = selectedField
                break
        if (selectedField == None):
            raise FullColumnException(column)

        self._lastSelectedField = selectedField

    def getField(self, row, column):
        return self._fields[row][column]

    def getLastSelectedField(self):
        return self._lastSelectedField
