"""Algoritmos recursivos em Python."""


def fibonacci_iterativo(n):
    """Calcula o n-esimo numero de Fibonacci, iterativamente."""
    f1 = 0
    f2 = 1
    for _ in range(n):
        t = f1 + f2
        f1 = f2
        f2 = t
    return f1


def fibonacci_recursivo(n):
    """Calcula o n-esimo numero de Fibonacci, iterativamente."""
    return 0 if n == 0 \
        else 1 if n == 1 \
        else fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)


if __name__ == "__main__":
    from sys import stdout
    for n in range(50):
        print("Iterativo:", end=" ")
        stdout.flush()
        print(n, fibonacci_iterativo(n))
        print("Recurviso:", end=" ")
        stdout.flush()
        print(n, fibonacci_recursivo(n))
