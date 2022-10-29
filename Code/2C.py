from sys import stdin,stdout
def readln():
    return stdin.readline().rstrip()

def outln(n):
    stdout.write(str(n))
    stdout.write("\n")

n = int(readln())
a = [int(i) for i in readln().split()]

def sum(a,n):
    m1 = 0
    m2 = 0
    for j in range(n):
        if a[j] > m1:
            m2 = m1
            m1 = a[j]

        elif a[j] > m2:
            m2 = a[j]

        elif m2 > m1:
            m1 = m2
            m2 = m1

        elif m1 == m2:
            m1 = m2

    return m1+m2

outln(sum(a,n))