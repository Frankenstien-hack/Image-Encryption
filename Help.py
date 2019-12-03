import numpy as np

def Up_Shift(x, index, n):
    
    Col = []
    
    for j in range(len(x)):
        Col.append(x[j][index])
    
    Shift_Col = np.roll(Col,-n)
    
    for i in range(len(x)):
        for j in range(len(x[0])):
            if(j == index):
                x[i][j] = Shift_Col[i]

def Down_Shift(x, index, n):
    
    Col = []
    
    for j in range(len(x)):
        Col.append(x[j][index])
    
    Shift_Col = np.roll(Col,n)
    
    for i in range(len(x)):
        for j in range(len(x[0])):
            if(j==index):
                x[i][j] = Shift_Col[i]

def Rot_180(n):
    
    bits = "{0:b}".format(n)
    return int(bits[::-1], 2)
