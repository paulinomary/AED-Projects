###   QUICKSORT PIVOT: INICIO   ###

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


def divide(lista, inicio, fim):
    indpivot = inicio
    pivot = lista[indpivot]
    while inicio < fim:
        while inicio < len(lista) and lista[inicio] <= pivot:
            inicio += 1
        while lista[fim] > pivot:
            fim -= 1
        if inicio < fim:
            lista[inicio], lista[fim] = lista[fim], lista[inicio]
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
