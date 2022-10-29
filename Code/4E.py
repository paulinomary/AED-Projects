###   QUICKSORT PIVOT: MEDIANA DE 3 ELEMENTOS   ###

from sys import stdin, stdout


def readln():
    return stdin.readline().rstrip()


def outln(n):
    stdout.write(str(n))
    stdout.write('\n')


def out(n):
    stdout.write(str(n))


n = int(readln())
lista = []


def insert():
    for i in range(n):
        elemento = int(readln())
        lista.append(elemento)


def print():
    for i in range(n):
        outln(lista[i])


def mediana():
    x = []
    x.append(lista[0])  # Junta o primeiro
    x.append(lista[-1])  # Junta o ultimo

    if len(lista) % 2 == 0:
        mval = len(lista) // 2
        x.append(lista[mval]) # Junta o valor do meio no caso do array ter n par de elementos

    elif len(lista) % 2 != 0:
        mval = (len(lista) // 2) + 1
        x.append(lista[mval]) # Junta o valor do meio no caso do array ter n impar de elementos

    x.sort()
    med = x[1]
    return med

def divide(lista, med, fim):
    indpivot = med
    pivot = lista[indpivot]
    while med < fim:
        while med < len(lista) and lista[med] <= pivot:
            med += 1
        while lista[fim] > pivot:
            fim -= 1
        if med < fim:
            lista[med], lista[fim] = lista[fim], lista[med]
    lista[fim], lista[indpivot] = lista[indpivot], lista[fim]
    return fim

def quickSort(lista, inicio, fim):
    if inicio < fim:
        div = divide(lista, inicio, fim)

        quickSort(lista, inicio, div - 1)
        quickSort(lista, div + 1, fim)



insert()
divide(lista, 0, n - 1)
quickSort(lista, 0, n - 1)

for i in range(n):
    outln(lista[i])