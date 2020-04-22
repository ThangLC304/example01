def reverse(num):
    rev = 0
    while num > 0:
        tam = num % 10
        rev = rev * 10 + tam
        num = num // 10
    return rev

