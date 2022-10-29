###   BUBBLE SORT   ###

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


def bubbleSort():
    for i in range(input - 1):
        for j in range(input - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    for i in range (len(lista)):
        outln(lista[i])

insert()
bubbleSort()