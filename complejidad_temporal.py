
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
    acumulador = 1.0
    for i in range(1,n+1):
        acumulador *= i
    return acumulador

def run():
    beginning = time.time()
    factorial_r(10000)
    step_1 = time.time()
    factorial_for(1000)
    step_2 = time.time()
    point_1 = step_1 - beginning
    print(point_1)


if __name__ == "__main__":

    run()
    
    
