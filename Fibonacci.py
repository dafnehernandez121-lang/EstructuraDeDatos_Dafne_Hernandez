import sys

sys.setrecursionlimit(3000)

memoria = {0: 0, 1: 1}

def fibonacci_recursivo(n):
    if n in memoria:
        return memoria[n]
    
    memoria[n] = fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)
    return memoria[n]

print("Generando los primeros 500 números de Fibonacci...")

for i in range(501):
    print(f"F({i}): {fibonacci_recursivo(i)}")
