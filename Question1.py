from Sheet import Sheet

sheet = Sheet(10,10) #max(x,675)
#sheet.modifyValue(0, A, string)

#sheet.modifyValue(0, 0, '')    #B

sheet.modifyValue(0, 0, '=D1')    #A1
sheet.modifyValue(1, 0, '=D2')    #A2
sheet.modifyValue(2, 0, '=D3')    #A3
sheet.modifyValue(3, 0, '=D4')    #A4
sheet.modifyValue(4, 0, '=sum([A1,A2,A3,A4])')    #A1

sheet.modifyValue(0, 1, '=D1+C1')    #B1
sheet.modifyValue(1, 1, '=D2+C2')    #B2
sheet.modifyValue(2, 1, '=D3+C3')    #B3
sheet.modifyValue(3, 1, '=D4+C4')    #B4
sheet.modifyValue(4, 1, '=sum([B1,B2,B3,B4])')    #B5

sheet.modifyValue(0, 2, '1')    #C1
sheet.modifyValue(1, 2, '2')    #C2
sheet.modifyValue(2, 2, '3')    #C3
sheet.modifyValue(3, 2, '4')    #C4

sheet.modifyValue(0, 3, '=E1+F1')    #D1
sheet.modifyValue(1, 3, '=E2+F2')    #D2
sheet.modifyValue(2, 3, '=E3+F3')    #D3
sheet.modifyValue(3, 3, '=E4+F4')    #D4

sheet.modifyValue(0, 4, '=G1-H1')    #E1
sheet.modifyValue(1, 4, '=G2*H2')    #E2
sheet.modifyValue(2, 4, '=G3*H3')    #E3
sheet.modifyValue(3, 4, '=G4**H4')    #E4

sheet.modifyValue(0, 5, '=2*H1-G1')    #F1
sheet.modifyValue(1, 5, '=H2*G2')    #F2
sheet.modifyValue(2, 5, '=H3*G3')    #F3
sheet.modifyValue(3, 5, '=H4**G4')    #F4

sheet.modifyValue(0, 6, '6')    #G1
sheet.modifyValue(1, 6, '3')    #G2
sheet.modifyValue(2, 6, '2')    #G3
sheet.modifyValue(3, 6, '2')    #G4

sheet.modifyValue(0, 7, '4')    #H1
sheet.modifyValue(1, 7, '5')    #H2
sheet.modifyValue(2, 7, '2')    #H3
sheet.modifyValue(3, 7, '3')    #H4

sheet.modifyValue(0, 8, '=A5/B5')    #I1

sheet.modifyValue(0, 7, '12')    #H1
sheet.modifyValue(0, 7, '4')    #H1

print(sheet)


