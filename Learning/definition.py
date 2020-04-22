def f(a, L=[]):
    L.append(a)
    print(L)
f(1)
f(2)
f(3)
f(4)


def f1(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f1(1))
print(f1(2))    