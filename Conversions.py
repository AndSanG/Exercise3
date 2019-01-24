def numeral(n):
    return chr(n + 65)

# 0-25 to A-Z
# 0=A
# 26=AA
# 675=YZ limit check how to manage left zeros

def int_to_letter(number, base=26):
    # if is 0 convertion is direct
    # not support for negative numbers
    if (number == 0): return numeral(0)
    elif(number<0): return '--'

    mods = []
    while number > 0:
        mods.append(number % base)
        number //= base
    if (len(mods) == 1): mods[0] = numeral(mods[0])

    else:
        for i in list(range(len(mods))):
            if(i==0):
                mods[i] = numeral(mods[i])
            else:
                mods[i] = numeral(mods[i] - 1)
            #manage left zeros

    mods.reverse()
    return ''.join(mods)

def colNameToInt( name):  # name is the letter part of the cell name
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

def rangeToListConverter(implicit_range):  # nameRange: 'A5:D11'

    implicit_range = implicit_range.split(':')

    first_col = colNameToInt(getLetters(implicit_range[0]))
    second_col = colNameToInt(getLetters(implicit_range[1]))
    start_column = min(first_col, second_col)
    end_column = max(first_col, second_col)
    first_row = int(getNumbers(implicit_range[0]))
    second_row = int(getNumbers(implicit_range[1]))
    start_row = min(first_row, second_row)
    end_row = max(first_row, second_row)

    explicit_range = []
    for i, colnumber in enumerate(range(start_column, end_column + 1)):
        localLetters = colNumberToName(colnumber + 1)  # i+1: actual to nominal correction
        for j, rownumber in enumerate(range(start_row, end_row + 1)):
            explicit_range.append(localLetters + str(rownumber))

    return explicit_range

def getLetters(cell):
    s = list(cell)
    letters = [x for x in s if (not x.isdigit())]
    result = ''.join(letters)
    return result

def getNumbers(cell):
    s = list(cell)
    numbers = [x for x in s if (x.isdigit())]
    result = ''.join(numbers)
    return result

#1=A, Z=26, AA=27 etc
def colNumberToName(number):
    if number<=0:
        print('Column number cannot be non positive')
        return

    # Base Conversion
    name_list = []

    divisible = number
    while divisible>0:
        remain = divisible%26
        if remain !=0:
            name_list.insert(0, str(remain))
            divisible = divisible // 26
        else:
            name_list.insert(0, str(26))
            divisible = divisible // 26-1

    letters=''
    for x in name_list:
        x = int(x)
        letters += chr(65+(x-1))

    return letters
