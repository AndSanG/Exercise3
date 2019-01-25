import re
from Matrix import Matrix
from Conversions import *
from functools import reduce
import string
from math import *

from statistics import *
import numpy as np
import matplotlib.pyplot as plt

'''
extraSpace: extra lines appended at the end to create buffer space
'''
def csv_to_sheet(file_path,extraSpace=10):
    mylist = []
    f = open(file_path, 'r')
    for line in f:
        cleanline = re.sub('[^A-Za-z0-9;,.-]+', '', line)
        mylist.append(cleanline)
    f.close()

    for i in range(len(mylist)):
        mylist[i] = mylist[i].split(",")

    rows_of_csv = len(mylist)
    cols_of_csv = len(mylist[0])

    ret_sheet = Sheet(rows_of_csv + extraSpace, cols_of_csv)  # 15 extra space for statistical analysis
    for row in range(rows_of_csv):
        for column in range(cols_of_csv):
            temp_argument = '=' + str(mylist[row][column])
            ret_sheet.modifyValue(row, column, temp_argument)

    return ret_sheet


class NumberCell():
    def __init__(self, x):
        self.value = int(x)
    def getValue(self):
        return self.value
    def __str__(self):
        return str(self.value)

class Constants():
    REGEX_CELL = '[A-Z]+[1-9][0-9]?|100+'
    REGEX_RANGE = '[A-Z]+[1-9][0-9]*[:][A-Z]+[1-9][0-9]*'

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


    def create_dependencies_tree(self):
        input = self.formula[1:]
        matches = self.input_matcher(input,Constants.REGEX_CELL)

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

    def input_matcher(self,input,regex):
        p = re.compile(regex)
        return p.finditer(input)  # list of matches

    def expand_range(self,input):

        matches = self.input_matcher(input,Constants.REGEX_RANGE)  # list of matches
        result = []  # list of components
        prev = 0
        for match in matches:
            result.append(input[prev:match.start()])
            result.append('[')
            cell_range = rangeToListConverter(input[match.start():match.end()])
            result.append(','.join(cell_range))
            result.append(']')
            prev = match.end()

        result.append(input[prev:])
        resultString = ''.join(result)
        return resultString

    # transforms the formula stored in a cell into python code
    # so A1 => self.lookup('A1')
    # A1 + B1 => self.lookup('A1') + self.lookup('B1')
    def addCalls(self, input):
        input = self.expand_range(input)
        matches = self.input_matcher(input,Constants.REGEX_CELL)                     #list of matches
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
    # get values of cells in range
    def get_range(self, cellRange):
        result = []
        range = self.expand_range(cellRange)
        for n in range:
            result.append(self.lookup(n))

        return result
    # get cells name in range
    def get_range_cells(self,cellRange):
        return self.expand_range(cellRange)

    # convert implicit into explicit range
    def expand_range(self,input):
        p = re.compile(Constants.REGEX_RANGE)
        matches = p.finditer(input)
        result = []  # list of components
        prev = 0
        for match in matches:
            result.append(input[prev:match.start()])
            result = rangeToListConverter(input[match.start():match.end()])
        return result

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

    '''
        Creates some new cells at the bottom, with some basic statistical analysis. 

        Assumptions - Comments: 
        1. Every set of data is organised column by column. For example, in a sheet with temperatures for some days, every day 
            has a column of temperatures. We also assume some symmetry: Same number of rows for each column
        2. The parameter final_row tells us manually where to start the analysis. It indicates the final row used for data,
            but it can be anything
        3. New function in at the top to import data from csv file (csv_to_sheet). Accompanied with ff.csv file in the directory
        4. all the following could be done under the same for-loop because it is ALMOST EXACTLY the same code.
            I let them in separate loops for presentation clarity


        ### LINES in the analysis sub-sheet ###
        1. mean
        2. std.deviation
        3. median
        4. variance
        5. max
        6. sum
        7. count
        _____________    (from -statistics- library)
        '''

    def statistical_analysis(self, final_row):
        rows_of_hs = self.rows
        cols_of_hs = self.cols
        start_row = final_row + 1  # leave a blank line between the analysis and the Data

        # 1-MEANS
        for col in range(0, cols_of_hs):
            letter_col = int_to_letter(col)
            s = '=mean(' + letter_col + '1:' + letter_col + str(final_row) + ')'
            self.modifyValue(start_row, col, s)
        start_row += 1

        # 2-STANDARD DEVIATIONS
        for col in range(0, cols_of_hs):
            letter_col = int_to_letter(col)
            s = '=stdev(' + letter_col + '1:' + letter_col + str(final_row) + ')'
            self.modifyValue(start_row, col, s)
        start_row += 1

        # 3-MEDIANS
        for col in range(0, cols_of_hs):
            letter_col = int_to_letter(col)
            s = '=median(' + letter_col + '1:' + letter_col + str(final_row) + ')'
            self.modifyValue(start_row, col, s)
        start_row += 1

        # 4-Variance
        for col in range(0, cols_of_hs):
            letter_col = int_to_letter(col)
            s = '=variance(' + letter_col + '1:' + letter_col + str(final_row) + ')'
            self.modifyValue(start_row, col, s)
        start_row += 1

        # 5-maximum
        for col in range(0, cols_of_hs):
            letter_col = int_to_letter(col)
            s = '=max(' + letter_col + '1:' + letter_col + str(final_row) + ')'
            self.modifyValue(start_row, col, s)
        start_row += 1

        # 6-sum
        for col in range(0, cols_of_hs):
            letter_col = int_to_letter(col)
            s = '=sum(' + letter_col + '1:' + letter_col + str(final_row) + ')'
            self.modifyValue(start_row, col, s)
        start_row += 1

        # 7-count
        for col in range(0, cols_of_hs):
            letter_col = int_to_letter(col)
            s = '=len(' + letter_col + '1:' + letter_col + str(final_row) + ')'
            self.modifyValue(start_row, col, s)

    '''
    Histograms of frequencies and cumulative frequencies on demand.
    '''

    def histogramPlot(self, the_column, final_row, type='frequency'):
        col = colNameToInt(the_column)

        l = []
        for row in range(final_row):
            l.append(self.matrix.getElementAt(row, col).value)

        if type == 'frequency':
            plt.hist(l)

            plt.title('Frequency histogram')
            plt.ylabel('Frequency')

        elif type == 'cumulative':
            bins = np.arange(np.floor(min(l)), np.ceil(max(l)))  # for cumulative to 1
            plt.hist(l, bins=bins, cumulative=True, density=1)  # statistical parameters

            plt.title('% CumulativeFrequency histogram')
            plt.ylabel('% Cumulative Frequency')
        else:
            raise ValueError(
                'Student Generated Error: No type \'' + type + '\' exists. Choose between \'cumulative\' and \'frequency\'.')

        # plt.legend(loc='right')
        plt.grid(True)
        plt.xlabel('Number Of Games')

        plt.show()

    def __str__(self):
        return self.matrix.__str__()

