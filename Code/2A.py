from sys import stdin,stdout
def readln():
    return stdin.readline().rstrip()

def outln(n):
    stdout.write(str(n))
    stdout.write("\n")

n = int(readln())
a = [int(i) for i in readln().split()]

def sum(a):
    m = 0
    for j in range(len(a)):
        for k in range(j+1,len(a)):
            if a[j]+a[k] > m:
                m = a[j]+a[k]
    return m

outln(sum(a))

