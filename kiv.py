import math

def kiv():
    prim: bool = False
    n: int = 9999

    while not prim:
        n += 1
        i: int = 2
        while (i <= math.sqrt(n)) and (n % i != 0):
            i += 1
        prim = i > math.sqrt(n)

    print(n)


kiv()