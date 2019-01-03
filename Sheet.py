import re
from Matrix import Matrix
from functools import reduce
import string
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
        self._value = None
        self.dependencies = []
        self.create_dependencies_tree()
        #self.updateValue()

    def get_value(self):
        self.updateValue()
        return self._value

    def set_value(self, value):
        self._value = value

    value = property(get_value, set_value)

    def input_matcher(self,input):
        p = re.compile('[A-Z]+[1-9][0-9]?|100+')
        return p.finditer(input)  # list of matches



    def create_dependencies_tree(self):
        input = self.formula[1:]
        matches = self.input_matcher(input)

        for match in matches:
            self.dependencies.append(input[match.start():match.end()])  # cell number e.g. A1

    def updateValue(self):

        def average(aList):
            return sum(aList) / len(aList)

        ### before calc the value the dependencies must be solved
        for cell_id in self.dependencies:
            cell = self._sheet.lookupCell(cell_id)
            if type(cell) is FormulaCell:
                cell.updateValue()

        # Eval the content of cell (without =) and save in the value
        #addCall convert A1 into lookup(A1)
        #lookup search the value
        self.value = eval(self.addCalls(self.formula[1:]))


    # transforms the formula stored in a cell into python code
    # so A1 => self.lookup('A1')
    # A1 + B1 => self.lookup('A1') + self.lookup('B1')
    def addCalls(self, input):
        matches = self.input_matcher(input)                     #list of matches
        result = []                                             # list of components
        prev = 0
        for match in matches:
            result.append(input[prev:match.start()])            # the symbol before character
            result.append('self._sheet.lookup(\'')              # self._sheet.lookup('
            result.append(input[match.start():match.end()])     # cell number e.g. A1
            result.append('\')')                                # ')
            prev = match.end()                                  # prev keep track of the position

        result.append(input[prev:])                             # append the content after the last match
        resultString = ''.join(result)                          # convert the result list into a string
        return resultString

    def __str__(self):
        #self.updateValue()
        return str(self.value)


class Sheet(object):
    def __init__(self,rows,cols):
        self.rows = rows
        self.cols = cols
        self.matrix = Matrix(rows, cols)
        # fill the sheet with zero numbercells
        for row in range(self.rows):
            for col in range(self.cols):
                self.modifyValue(row, col, "0")



    def modifyValue(self, row, col, newValue):
        if newValue.isdigit():
            cellObject = NumberCell(newValue)
        else:
            cellObject = FormulaCell(newValue, self)

        self.matrix.setElementAt(row, col, cellObject)
        # self.checkAllDependenciesForUpdates()

    # A => 0
    def colNameToInt(self, name):
        # invert oder of letters (lowest count first)
        name = name[::-1]
        result = 0
        # loop over all letters
        for i in range(len(name)):
            # convert the letter to its value, make 1 the first value
            num = (ord(name[i]) - 65) + 1
            # add the number multiplied by its weight
            result += num * 26 ** i
        return result - 1

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
        cell = self.matrix.getElementAt(row, col)
        return cell.value

    def lookupCell(self, x):

        p = re.compile('[A-Z]+')
        matches = p.match(x)
        to = matches.end()
        letters = x[:to]
        digits = x[to:]
        row = int(digits) - 1  # for 0 based matrix index
        col = self.colNameToInt(letters)
        cell = self.matrix.getElementAt(row, col)
        return cell

    def __str__(self):
        return self.matrix.__str__()

