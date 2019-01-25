from _sha3 import sha3_224

from Sheet import Sheet
from Conversions import *
import re

original = Sheet(10, 10)

original.modifyValue(0, 0, '0')    #A
original.modifyValue(1, 0, '0')    #
original.modifyValue(2, 0, '2')    #
original.modifyValue(3, 0, '8')    #
original.modifyValue(4, 0, '0')    #
original.modifyValue(5, 0, '7')    #
original.modifyValue(6, 0, '5')    #
original.modifyValue(7, 0, '0')    #
original.modifyValue(8, 0, '0')    #

original.modifyValue(9, 0, '=sum(A1:A9)')


original.modifyValue(0, 1, '6')    #B
original.modifyValue(1, 1, '0')    #
original.modifyValue(2, 1, '0')    #
original.modifyValue(3, 1, '0')    #
original.modifyValue(4, 1, '0')    #
original.modifyValue(5, 1, '0')    #
original.modifyValue(6, 1, '0')    #
original.modifyValue(7, 1, '0')    #
original.modifyValue(8, 1, '4')    #

original.modifyValue(9, 1, '=sum(B1:B9)')


original.modifyValue(0, 2, '0')    #C
original.modifyValue(1, 2, '8')    #
original.modifyValue(2, 2, '0')    #
original.modifyValue(3, 2, '0')    #
original.modifyValue(4, 2, '6')    #
original.modifyValue(5, 2, '0')    #
original.modifyValue(6, 2, '0')    #
original.modifyValue(7, 2, '7')    #
original.modifyValue(8, 2, '0')    #

original.modifyValue(9, 2, '=sum(C1:C9)')


original.modifyValue(0, 3, '1')    #D
original.modifyValue(1, 3, '3')    #
original.modifyValue(2, 3, '0')    #
original.modifyValue(3, 3, '4')    #
original.modifyValue(4, 3, '0')    #
original.modifyValue(5, 3, '9')    #
original.modifyValue(6, 3, '0')    #
original.modifyValue(7, 3, '2')    #
original.modifyValue(8, 3, '5')    #

original.modifyValue(9, 3, '=sum(D1:D9)')


original.modifyValue(0, 4, '0')    #E
original.modifyValue(1, 4, '0')    #
original.modifyValue(2, 4, '0')    #
original.modifyValue(3, 4, '0')    #
original.modifyValue(4, 4, '0')    #
original.modifyValue(5, 4, '0')    #
original.modifyValue(6, 4, '0')    #
original.modifyValue(7, 4, '0')    #
original.modifyValue(8, 4, '0')    #

original.modifyValue(9, 4, '=sum(E1:E9)')


original.modifyValue(0, 5, '4')    #F
original.modifyValue(1, 5, '5')    #
original.modifyValue(2, 5, '0')    #
original.modifyValue(3, 5, '7')    #
original.modifyValue(4, 5, '0')    #
original.modifyValue(5, 5, '1')    #
original.modifyValue(6, 5, '0')    #
original.modifyValue(7, 5, '6')    #
original.modifyValue(8, 5, '8')    #

original.modifyValue(9, 5, '=sum(F1:F9)')


original.modifyValue(0, 6, '0')    #G
original.modifyValue(1, 6, '6')    #
original.modifyValue(2, 6, '0')    #
original.modifyValue(3, 6, '0')    #
original.modifyValue(4, 6, '3')    #
original.modifyValue(5, 6, '0')    #
original.modifyValue(6, 6, '0')    #
original.modifyValue(7, 6, '9')    #
original.modifyValue(8, 6, '0')    #

original.modifyValue(9, 6, '=sum(G1:G9)')


original.modifyValue(0, 7, '5')    #H
original.modifyValue(1, 7, '0')    #
original.modifyValue(2, 7, '0')    #
original.modifyValue(3, 7, '0')    #
original.modifyValue(4, 7, '0')    #
original.modifyValue(5, 7, '0')    #
original.modifyValue(6, 7, '0')    #
original.modifyValue(7, 7, '0')    #
original.modifyValue(8, 7, '7')    #

original.modifyValue(9, 7, '=sum(H1:H9)')


original.modifyValue(0, 8, '0')    #I
original.modifyValue(1, 8, '0')    #
original.modifyValue(2, 8, '1')    #
original.modifyValue(3, 8, '6')    #
original.modifyValue(4, 8, '0')    #
original.modifyValue(5, 8, '4')    #
original.modifyValue(6, 8, '2')    #
original.modifyValue(7, 8, '0')    #
original.modifyValue(8, 8, '0')    #

original.modifyValue(9, 8, '=sum(I1:I9)')


original.modifyValue(0, 9, '=sum(A1:I1)')
original.modifyValue(1, 9, '=sum(A2:I2)')
original.modifyValue(2, 9, '=sum(A3:I3)')
original.modifyValue(3, 9, '=sum(A4:I4)')
original.modifyValue(4, 9, '=sum(A5:I5)')
original.modifyValue(5, 9, '=sum(A6:I6)')
original.modifyValue(6, 9, '=sum(A7:I7)')
original.modifyValue(7, 9, '=sum(A8:I8)')
original.modifyValue(8, 9, '=sum(A9:I9)')

fixedCells = ['A3', 'A4', 'A6', 'A7',
              'B1', 'B9',
              'C2', 'C5', 'C8',
              'D1', 'D2', 'D4', 'D6', 'D8', 'D9',
              'F1', 'F2', 'F4', 'F6', 'F8', 'F9',
              'G2', 'G5', 'G8',
              'H1', 'H9',
              'I3', 'I4', 'I6', 'I7']


def isValid(cell):
    if re.match('[A-Z]+[1-9][0-9]?|100+', cell) is not None:
        if (isValidNumber(getNumbers(cell)) and isValidNumber(ord(getLetters(cell))-64)):
            return True
    return False


def isValidNumber(value):
    if(str(value).isdigit()):
        return True if 0 < int(value) < 10 else False
    else:
        return False

def isCorrect(cell,value):
    # the row must contain the same number just once

    list_row = original.get_range('A%s:I%s' % (getNumbers(cell), getNumbers(cell)))

    # the col must contain the same number just once

    list_col = original.get_range('%s1:%s9' % (getLetters(cell), getLetters(cell)))

    # the zone  must contain the same number just once
    row_start = ((int(getNumbers(cell)) - 1) // 3) * 3 + 1
    row_end = ((int(getNumbers(cell)) - 1) // 3) * 3 + 3
    col_start = chr(((((ord(getLetters(cell)) - 64) - 1) // 3) * 3 + 1) + 64)
    col_end = chr(((((ord(getLetters(cell)) - 64) - 1) // 3) * 3 + 3) + 64)
    list_zone = original.get_range('%s%s:%s%s'%(col_start,row_start,col_end,row_end))
    correct = True

    if value in list_row:
        print('The value is already in the row of ' + cell)
        correct = False
    if value in list_col:
        print('The value is already in the row' + cell)
        correct = False
    if value in list_zone:
        print('The value is already in the zone' + cell)
        correct = False

    return correct

def isSolved():
    if (sum(original.get_range('A1:I9'))==45*9):
        return True
    return False


solved = False
while(not solved):
    print('\n')
    print(original)
    print('you cant change this cells  : ' + str(fixedCells))

    print('because those are the original cells \n')
    cell = input("Which cell do you want to change ")
    cell = cell.upper()
    if cell in fixedCells:
        print('You can not change the value of ' + cell + ' cell' )
    elif(isValid(cell)):
        row = cell_to_coords(cell)[0]
        col = cell_to_coords(cell)[1]

        done = False
        while not done:
            value = input('Number from 1 to 9 for cell ' + cell + ' ')
            if(isValidNumber(value)):
                if isCorrect(cell,int(value)):
                    done = True
                else:
                    print('\n')

            else:
                print('It is not correct, remember numbers from 1 to 9 \n')
                done = False

        original.modifyValue(row, col, value)
        print('Number inserted')

    else:
        print('not a valid cell number \n')

    solved = isSolved()

print('Congrats you WON!!!')





