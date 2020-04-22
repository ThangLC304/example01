'''
with open('file.txt','w') as f:
    f.write('Day la dong dau tien\n')
    f.write('Day la dong thu hai\n')
    f.write('Day la dong cuoi cung')  
with open('file.txt') as f:
    data = f.read()
with open('file.txt', 'rb+') as f:
    data1 = f.read(10)
    f.seek(1, 0)
    data2 = f.read(10) 
    f.seek(1, 1)
    data3 = f.read(15)
    f.seek(-8, 2)
    data4 = f.read(10)
print(data)
print(data1)
print(data2)
print(data3)
print(data4)

with open('file.txt', 'r+') as f:
    data = f.read()
    f.seek(0, 0)
    data1 = f.read(10)
    data2 = f.read(10) 
    data3 = f.read(15)
    data4 = f.read(10)
print('X:', data)
print('A:', data1)
print('B:', data2)
print('C:', data3)
print('D:', data4)
'''
with open('file.txt','w') as f:
    f.write('Day la dong dau tien\n')
    f.write('Day la dong thu hai\n')
    f.write('Day la dong cuoi cung') 

x = 169
import json
while True:
    try:
        with open('file.txt', 'r+') as f:
            json.dump(x, f)
            f.seek(0, 0)
            y = f.read()
        break
    except TypeError:
        y = 'Oops, object of type set is not JSON serializable'
print(y)

x = 'Toi la Huy Suke ngu si dan don\n'
import json
while True:
    try:
        with open('file.txt', 'r+') as f:
            f.writelines(x)
            f.seek(0, 0)
            y = f.read()
        break
    except TypeError:
        y = 'Oops, object of type set is not JSON serializable'
print(y)

class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, ):
        super().__init__(*args, **kwargs)

