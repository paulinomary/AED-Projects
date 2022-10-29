from sys import stdout
import random
import time


def outln(n):
    stdout.write(str(n))
    stdout.write("\n")

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


def geraDecrescente(n):
    for i in range(n):
        lista.append(n - i)


def geraN(n, percentagem):
    quantidade = n * percentagem
    posicao = []
    for j in range(int(quantidade)):
        posicao.append(random.randint(0, n))
        for i in range(n):
            if i in posicao:
                lista.append(i + random.randint(10000, 50000))
            else:
                lista.append(i)


def geraRandom(n):
    for i in range(n):
        lista.append(random.randint(0, 10000000))
    return lista


n = 25000
lista = []
for i in range(5):
    geraRandom(n)
    start = time.time()
    divide(lista, 0, n - 1)
    quickSort(lista, 0, n-1)
    end = time.time()
    outln("Tempo Quick Sort A Aleatório para " + str(n) + " : " + str(end - start))
    n += 25000

n = 25000
lista = []
for i in range(5):
    geraDecrescente(n)
    start = time.time()
    divide(lista, 0, n - 1)
    quickSort(lista, 0, n-1)
    end = time.time()
    outln("Tempo Quick Sort A Decrescente para " + str(n) + " : " + str(end - start))
    n += 25000

n = 25000
lista = []
for i in range(5):
    geraN(n, 0.05)
    start = time.time()
    divide(lista, 0, n - 1)
    quickSort(lista, 0, n-1)
    end = time.time()
    outln("Tempo Quick Sort A 1% para " + str(n) + " : " + str(end - start))
    n += 25000

n = 25000
lista = []
for i in range(5):
    geraN(n, 0.05)
    start = time.time()
    divide(lista, 0, n - 1)
    quickSort(lista, 0, n-1)
    end = time.time()
    outln("Tempo Quick Sort A 5% para " + str(n) + " : " + str(end - start))
    n += 25000
