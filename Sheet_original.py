import re
from Matrix import Matrix
from math import *


class NumberCell():
    def __init__(self, x):
        self.value = int(x)

    def __str__(self):
        return str(self.value)


class FormulaCell():
    def __init__(self, expr, sheet):  # expr is of the shape "=A1+B2" in string
        self._sheet = sheet
        self.formula = expr
        self.updateValue()

    def updateValue(self):
        self.value = eval(self.addCalls(self.formula[1:]))

    # A => 0
    def colNameToInt(self, name):
        return ord(name[0]) - 65

    # lookup the value of a given cell.
    # x = A1, B22, AB33 ...
    def lookup(self, x):
        p = re.compile('[A-Z]+')
        matches = p.match(x)
        to = matches.end()
        letters = x[:to]
        digits = x[to:]
        row = int(digits) - 1  # for 0 based matrix index
        col = self.colNameToInt(letters)
        cell = self._sheet.matrix.getElementAt(row, col)
        return cell.value

    # transforms the formula stored in a cell into python code
    # so A1 => self.lookup('A1')
    # A1 + B1 => self.lookup('A1') + self.lookup('B1')
    def addCalls(self, input):
        p = re.compile('[A-Z]+[1-9]+')
        matches = p.finditer(input)
        result = []
        prev = 0
        for match in matches:
            result.append(input[prev:match.start()])
            result.append('self.lookup(\'')
            result.append(input[match.start():match.end()])
            result.append('\')')
            prev = match.end()

        result.append(input[prev:])
        resultString = ''.join(result)
        return resultString

    def __str__(self):
        self.updateValue()
        return str(self.value)


class Sheet(object):
    def __init__(self):
        self.rows = 3
        self.cols = 5
        self.matrix = Matrix(3, 5)
        # fill the sheet with zero numbercells
        for row in range(self.rows):
            for col in range(self.cols):
                self.updateValue(row, col, "0")

    def updateValue(self, row, col, newValue):
        if newValue.isdigit():
            cellObject = NumberCell(newValue)
        else:
            cellObject = FormulaCell(newValue, self)

        self.matrix.setElementAt(row, col, cellObject)
        # self.checkAllDependenciesForUpdates()

    def __str__(self):
        return self.matrix.__str__()

