import math


def osztok(szam):
    osztok_lista = []
    for i in range(2, round(math.sqrt(szam)) + 1):
        if szam % i == 0:
            osztok_lista.append(i)
    return osztok_lista


def osztok_while(szam):
    lista = []
    oszto = 2
    while oszto <= round(math.sqrt(szam)):
        if szam % oszto == 0:
            lista.append(oszto)
        oszto += 1
    return lista


