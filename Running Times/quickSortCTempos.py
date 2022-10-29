from sys import stdout
import random
import time


def outln(n):
    stdout.write(str(n))
    stdout.write("\n")


def partition(arr,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[med]     # pivot

    for j in range(low , high):
        if   arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)

med = 0
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
    partition(lista, 0, n - 1)
    quickSort(lista, 0, n-1)
    end = time.time()
    outln("Tempo Quick Sort C Aleatório para " + str(n) + " : " + str(end - start))
    n += 25000

n = 25000
lista = []
for i in range(5):
    geraDecrescente(n)
    start = time.time()
    partition(lista, 0, n - 1)
    quickSort(lista, 0, n-1)
    end = time.time()
    outln("Tempo Quick Sort C Decrescente para " + str(n) + " : " + str(end - start))
    n += 25000


n = 25000
lista = []
for i in range(5):
    geraN(n, 0.05)
    start = time.time()
    partition(lista, 0, n - 1)
    quickSort(lista, 0, n-1)
    end = time.time()
    outln("Tempo Quick Sort C 1% para " + str(n) + " : " + str(end - start))
    n += 25000

n = 25000
lista = []
for i in range(5):
    geraN(n, 0.05)
    start = time.time()
    partition(lista, 0, n - 1)
    quickSort(lista, 0, n-1)
    end = time.time()
    outln("Tempo Quick Sort C 5% para " + str(n) + " : " + str(end - start))
    n += 25000
