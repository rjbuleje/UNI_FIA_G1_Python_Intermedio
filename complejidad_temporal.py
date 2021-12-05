import time
import sys

sys.setrecursionlimit(100000)

def factorial_r(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_r(n-1)

def factorial_for(n):
    if n == 0 or n == 1:
        return 1
    acumulador = 1
    for i in range(1,n+1):
        acumulador *= i
    return acumulador




if __name__ == "__main__":
    beginning = time.time()
    factorial_r(100)
    step_1 = time.time()
    factorial_for(100)
    step_2 = time.time()
    print(step_1 - beginning)
    print(step_2 - step_1)

