from Sheet import *
from Conversions import *
import numpy as np
import matplotlib.pyplot as plt




sheet1 = Sheet(5, 4)


# TEST values and references (also done in question1)
sheet1.modifyValue(0, 0, '7')
#print(sheet1)
sheet1.modifyValue(1, 0, '5')
#print(sheet1)
sheet1.modifyValue(0, 1, '=(3+4)*2')
#print(sheet1)
sheet1.modifyValue(0, 2, '=A1+B1')
#print(sheet1)
sheet1.modifyValue(1, 2, '=A1-B1')
#print(sheet1)
sheet1.modifyValue(2, 2, '=A1*B1')
#print(sheet1)
sheet1.modifyValue(0, 3, '=(A1+8)-(A2)')
#print(sheet1)
sheet1.modifyValue(0, 0, '1')
print(sheet1)

# TEST DEPENDENCIES
sheet2 = Sheet(10,4)
sheet2.modifyValue(0,0,'=B1')
sheet2.modifyValue(0,1,'=C1')
sheet2.modifyValue(0,2,'3')
print(sheet2)

# TEST RANGE IMPLEMENTATION
sheet2.modifyValue(1,0,'=sum(A1:D1)')
print(sheet2)
sheet2.modifyValue(2,0,'=sum(A1:A2)+C1')
print(sheet2)

# TEST Statistics
    #TEST ANALYSIS
print('statistical analysis below')
cc = csv_to_sheet('ff.csv',9)
cc.statistical_analysis(79)
print(cc)

    # TEST HISTOGRAMS
cc.histogramPlot('A',79,'frequency')
cc.histogramPlot('B',79,'cumulative')
#cc.histogramPlot('C',79,'something') # --> uncomment to see the error it generates
