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
