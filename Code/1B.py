from sys import stdin, stdout


def readln():
    return stdin.readline().rstrip()


def outln(n):
    stdout.write(str(n))
    stdout.write("\n")


def out(n):
    stdout.write(str(n))


linhas, colunas = [int(i) for i in readln().split()]
if linhas > 10 or colunas > 10:
    linhas, colunas = [int(i) for i in readln().split()]
m = []
for i in range(linhas):
    m.append([int(i) for i in readln().split()])


def rodar90(matriz):
    nova_matriz = [[0 for coluna in range(len(matriz))] for linha in range(len(matriz[0]))]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            nova_matriz[j][len(matriz) - (i + 1)] = matriz[i][j]
    return nova_matriz


def rodar180(matriz):
    return rodar90(rodar90(matriz))


def rodar270(matriz):
    return rodar90(rodar180(matriz))


def imprime(matriz, grau):
    out(grau)
    for i in range(len(matriz)):
        outln("")
        for j in range(len(matriz[0])):
            out(matriz[i][j])
            if j != len(matriz[0]) - 1:
                out(" ")
    outln("")


imprime(rodar90(m), 90)
imprime(rodar180(m), 180)
imprime(rodar270(m), 270)

