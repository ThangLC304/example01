
#Dem so lan xuat hien cua "Emma"
def dem_Emma(kitu): 
    count = 0
    for i in range(0,len(kitu)-1):
        count += kitu[i:i+4] == "Emma"
    return count
day_ki_tu = "Emma is a good developer. Emma is also a write"
count = dem_Emma(day_ki_tu)
print("Emma appeared %2.0f times" %count)

#Noi 1 day co separator
def concat (*args, sep = ", "):
    return sep.join(args)

print(concat("A", "B", "C", cach = "/ "))


#9. Reverse a given number and return True if it is the same as the original
def reverse_and_check(number):
    originalNum = number
    reverseNum = 0
    while number > 0:
        reminder = number % 10
        reverseNum = (reverseNum * 10) + reminder
        number = number // 10
    if originalNum == reverseNum:
        return True
    else:
        return False

print("Original and reversed number is equal")
print(reverse_and_check(313))



