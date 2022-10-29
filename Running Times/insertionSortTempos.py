from sys import stdout
import random
import time


def outln(n):
    stdout.write(str(n))
    stdout.write("\n")

def insertionSort(lista, n):
    for i in range(n):
        elemento = lista[i]
        j = i - 1
        while j >= 0 and elemento < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = elemento


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
    insertionSort(lista, n)
    end = time.time()
    outln("Tempo Insertion Sort Aleatório para " + str(n) + " : " + str(end - start))
    n += 25000

n = 25000
lista = []
for i in range(5):
    geraDecrescente(n)
    start = time.time()
    insertionSort(lista, n)
    end = time.time()
    outln("Tempo Insertion Sort Decrescente para " + str(n) + " : " + str(end - start))
    n += 25000

n = 25000
lista = []
for i in range(5):
    geraN(n, 0.05)
    start = time.time()
    insertionSort(lista, n)
    end = time.time()
    outln("Tempo Insertion Sort 1% para " + str(n) + " : " + str(end - start))
    n += 25000

n = 25000
lista = []
for i in range(5):
    geraN(n, 0.05)
    start = time.time()
    insertionSort(lista, n)
    end = time.time()
    outln("Tempo Insertion Sort 5% para " + str(n) + " : " + str(end - start))
    n += 25000
