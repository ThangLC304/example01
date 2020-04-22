'''
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
#Lay ra cac row:
m_row = [row for row in matrix]
print(m_row)

#Lay ra cac column: 
#Ta lay phan tu thu i cua tung` row
m_col = [[row[i] for row in matrix] for i in range(4)]
print(m_col)

#hoac nhanh hon la dung built-in function
m_col1 = list(zip(*matrix))
print(m_col1)
print(m_col1[0])


#lenh del
def xoa_noi_dung_variable(x):
    del x[:]
    return print(x)     #ket qua la []
xoa_noi_dung_variable(m_col)

def xoa_variable(x):
    del x       
    print(x)            #ket qua la Syntax Error vi bien' x da bi xoa
'''
#List
t1 = [123, 456, 789]
u1 = [t1, [1, 2, 3]]
u1[1] = 4
print(u1[1])

#Tuple
t = 123, 456, 789 #Or t = (123, 456, 789)
u = t, (1, 2, 3)  #Or u = (t, (1, 2, 3))
#u[12] = 4        #Tuple object does not support item assignment
print(u[1])

x, y = u
print(x)











