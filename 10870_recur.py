import sys
input = sys.stdin.readline

N = int(input())

def fibo(N):
    if N == 0:
        return 0
    elif N == 1 or N == 2:
        return 1
    else:
        return fibo(N-1) + fibo(N-2)

print(fibo(N))
