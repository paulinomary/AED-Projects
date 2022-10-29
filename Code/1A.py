from sys import stdin,stdout
def readln():
    return stdin.readline().rstrip()
def outln(n):
    stdout.write(str(n))
    stdout.write("\n")
n1,n2 = [int(i) for i in readln().split()]
result = n1+n2
outln(result)