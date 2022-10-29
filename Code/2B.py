from sys import stdin,stdout
def readln():
    return stdin.readline().rstrip()

def outln(n):
    stdout.write(str(n))
    stdout.write("\n")

n = int(readln())
a = [int(i) for i in readln().split()]

def sum(a):
    a.sort()
    soma = a[-1] + a[-2]
    return soma

outln(sum(a))