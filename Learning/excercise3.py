#Question 9
def reverse_and_test(number):
    num = number
    n = len(str(number))
    rev_num = 0
    for i in range(n):
        tam = num % 10
        num = num // 10
        rev_num = rev_num + tam*(10**(n-i-1))
    print(rev_num)
    if rev_num == number:
        print('True')
    else:
        print('False')

reverse_and_test(122)



#Question 10
def mergelist(listOne, listTwo):
    merged = []
    for x in listOne:
        if x % 2 != 0:
            merged.append(x)
    for y in listTwo:
        if y % 2 == 0:
            merged.append(y)
    return merged


listOne = [10, 20, 23, 11, 17]
listTwo = [13, 43, 24, 36, 12]

print(mergelist(listOne, listTwo))

