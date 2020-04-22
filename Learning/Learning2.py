#Using the range function
for value in range(1, 6):
    print(value)

#Creating a list of number   
number = list(range(1, 6))
print(number)

odd_number = list(range(1,101,2))
print(odd_number)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(square)

digits = [1,2,3,4,5,6,7,8,9]
print(max(digits))
print(min(digits))
print(sum(digits))

#Slicing a list
names = ['huy', 'thang', 'kow', 'nho']
print(names[0:2])
print(names[:2])
print(names[1:3])
print(names[2:])
print(names[-3])

#Looping through a slice with a for loop
names = ['huy', 'thang', 'kow', 'nho']
print('Here are the names of the last 3 registrations.')
for name in names[:3]:
    print(name.title())

#Copying a list
names = ['huy', 'thang', 'kow', 'nho']
first_names = names[:]
print(first_names)



