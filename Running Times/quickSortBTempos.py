from sys import stdout
import random
import time


def outln(n):
    stdout.write(str(n))
    stdout.write("\n")


def divide(lista, inicio, fim):
    indpivot = random.randint(inicio,fim)
    pivot = inicio

    for i in range(inicio,fim):
        if lista[i] < lista[fim]:
            lista[i],lista[pivot] = lista[pivot],lista[i]
            pivot += 1
        lista[fim], lista[indpivot] = lista[indpivot], lista[fim]
    lista[pivot],lista[fim] = lista[fim],lista[pivot]

    return pivot


def quickSort(lista, inicio, fim):
    if inicio < fim:
        pivot = divide(lista, inicio, fim)
        quickSort(lista, inicio, pivot-1)
        quickSort(lista, pivot+1, fim)

    return lista


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
    outln("Tempo Quick Sort B Aleatório para " + str(n) + " : " + str(end - start))
    n += 25000

n = 25000
lista = []
for i in range(5):
    geraDecrescente(n)
    start = time.time()
    divide(lista, 0, n - 1)
    quickSort(lista, 0, n-1)
    end = time.time()
    outln("Tempo Quick Sort B Decrescente para " + str(n) + " : " + str(end - start))
    n += 25000

n = 25000
lista = []
for i in range(5):
    geraN(n, 0.05)
    start = time.time()
    divide(lista, 0, n - 1)
    quickSort(lista, 0, n-1)
    end = time.time()
    outln("Tempo Quick Sort B 1% para " + str(n) + " : " + str(end - start))
    n += 25000

n = 25000
lista = []
for i in range(5):
    geraN(n, 0.05)
    start = time.time()
    divide(lista, 0, n - 1)
    quickSort(lista, 0, n-1)
    end = time.time()
    outln("Tempo Quick Sort B 5% para " + str(n) + " : " + str(end - start))
    n += 25000
