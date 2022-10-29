###   QUICKSORT PIVOT: RANDOM   ###

import random
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


def divide(lista, inicio, fim):
    indpivot = random.randint(inicio,fim)
    lista[fim], lista[indpivot] = lista[indpivot], lista[fim]
    pivot = inicio

    for i in range(inicio,fim):
        if lista[i] < lista[fim]:
            lista[i],lista[pivot] = lista[pivot],lista[i]
            pivot += 1

    lista[pivot],lista[fim] = lista[fim],lista[pivot]

    return pivot


def quickSort(lista, inicio, fim):
    if inicio < fim:
        pivot = divide(lista, inicio, fim)
        quickSort(lista, inicio, pivot-1)
        quickSort(lista, pivot+1, fim)

    return lista


insert()
quickSort(lista, 0, n-1)
divide(lista, 0, n-1)
print()