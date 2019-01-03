from Sheet import Sheet

sheet = Sheet(10,10)
#sheet.modifyValue(0, A, string)
'''
sheet.modifyValue(0, 0, '7')  #A1
sheet.modifyValue(1, 0, '5')  #A2
sheet.modifyValue(0, 1, '=(3+4)*2') #B1
sheet.modifyValue(0, 2, '=A1+B1')  #C1
sheet.modifyValue(1, 2, '=A1-B1')  #C2
sheet.modifyValue(2, 2, '=A1*B1')  #C3
sheet.modifyValue(0, 3, '=(A1+8)/2')  #D1
sheet.modifyValue(1, 3, '=max(A1,A2)') #D2
'''
#sheet.modifyValue(2, 26, "=11") #AA3
#sheet.modifyValue(1, 0, "=AA3") #A2
#sheet.modifyValue(0, 27, "111") #AB1

#sheet.modifyValue(3, 0, '=sum([A1,B10,C10,D10])') #A4
#sheet.modifyValue(4, 0, '=average([A1,B1,C1,D9])') #A4

sheet.modifyValue(0, 1, '7')    #B1
sheet.modifyValue(1, 0, '=B1')  #A2
sheet.modifyValue(1, 1, '=B1')  #B2
sheet.modifyValue(2, 2, '=A2')  #C3
sheet.modifyValue(0, 0, '=B2+C3')  #A1
sheet.modifyValue(0, 1, '8')    #B1

#sheet.modifyValue(4, 0, '5')  #A5

#sheet.modifyValue(0, 2, '=B2')  #C1
print(sheet)
