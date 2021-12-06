[Programación de algoritmos](../README.md)
# Fibonnaci
```python
def fib(n):
    """"Devuelve la serie de fibonacci hasta n"""
    result = []
    a, b = 0, 1

    while a < n:
        print(a)
        result.append(a)
        a, b = b, a + b


f = fib
print(f(35))
fib(1)



def fib2(n):
    if n == 1 or n == 2:
        return 1
    else:
        return (fib2(n - 1) + fib2(n - 2))


print(fib2(35))
```