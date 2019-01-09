from Conversions import *

class Matrix(object):
    """A simple Matrix class in Python"""

    def __init__(self, rows, columns):
        self.width = columns
        self.height = rows
        self.data = []
        for i in range(rows):
            self.data.append([])
            for j in range(columns):
                self.data[i].append(0)

    def setElementAt(self, x, y, value):
        self.data[x][y] = value

    def getElementAt(self, x, y):
        return self.data[x][y]

    def __str__(self):

        result = []
        result.append('%6s' % (' '))
        for col in range(self.width):
            result.append('%7s' % (int_to_letter(col) + ' '))
        result.append("\n")
        for col in range(self.width+1):
            result.append('%7s' % (7*'-'))
        result.append("\n")

        r=1
        for row in self.data:
            result.append('%6s' % ('<'+str(r)+'> '+'|'))
            r+=1
            for cell in row:
                result.append('%6.5s' % (str(cell)+'|'))
                result.append(" ")
            result.append("\n")
        string = ''.join(result)
        return string


