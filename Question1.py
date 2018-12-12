from Sheet import Sheet

sheet = Sheet(5,5)
#sheet.updateValue(0, A, string)
sheet.updateValue(0, 0, '7')  #A1
sheet.updateValue(1, 0, '5')  #A2
sheet.updateValue(0, 1, '=(3+4)*2') #B1
sheet.updateValue(0, 2, '=A1+B1')  #C1
sheet.updateValue(1, 2, '=A1-B1')  #C2
sheet.updateValue(2, 2, '=A1*B1')  #C3
sheet.updateValue(0, 3, '=(A1+8)/2')  #D1
sheet.updateValue(1, 3, '=max(A1,A2)') #D2


#sheet.updateValue(1, 0, "=AA1") #A2
#sheet.updateValue(0, 27, "111") #A2
sheet.updateValue(3, 0, '=A1') #A4

print(sheet)

def colNameToInt(name):
    result = 0;
    for i in range(len(name),-1,1):
        print(i)
        print((ord(name[i])-65) * pow(26,i))
    print(result)
    return ord(name[0]) - 65

colNameToInt('AA')