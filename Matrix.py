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
        for row in self.data:
            for cell in row:
                result.append(str(cell))
                result.append(" ")
            result.append("\n")
        string = ''.join(result)
        return string


