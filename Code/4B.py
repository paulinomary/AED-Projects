###   INSERTION SORT   ###

from sys import stdin, stdout


def readln():
    return stdin.readline().rstrip()


def outln(n):
    stdout.write(str(n))
    stdout.write('\n')


def out(n):
    stdout.write(str(n))


input = int(readln())
lista = []


def insert():
    for i in range(input):
        item = int(readln())
        lista.append(item)


def insertionSort():
    for i in range(len(lista)):
        elemento = lista[i]
        j = i - 1

        while j >= 0 and elemento < lista[j]:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = elemento

    for i in range(len(lista)):
        outln(lista[i])

insert()
insertionSort()