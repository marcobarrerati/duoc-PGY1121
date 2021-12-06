[Programación de algoritmos](../README.md)
# Ciclos
## for
Midiendo cadenas de texto con ciclo for

```python
palabras = ["gato", "ventana", "defenestrado"]
for p in palabras:
    print(p, len(p))
```
Hacer una copia por rebanada de toda la lista
```python
for p in palabras[:]:
    if len(p) > 6:
        palabras.insert(0, p)

print(palabras)
```
## Función range
Iterar una secuencia de números
```python
for i in range(5):
    print(i)
```
Iterar sobre los índices de una secuencia combinando range() y len()
```python
a = ["Mary", "tenia", "un", "corderito"]

for i in range(len(a)):
    print(i, a[i])
```
Iterar sobre los indices usando enumerate
```python
for i in enumerate(a, 0):
    print(i[1])
```
```python
def sumarEnFor():
    total = 0
    for i in range(2, 101):
        # print(i)
        if i % 2 == 0:
            total += i
    return total

print(sumarEnFor())
```
```python
def fu():
    s = 0
    for n in range(10):
        s += n
    return s


print(fu())

```

# Sentencia continue en for

```python
par, impar = [], []
for num in range(2, 10):
    if num % 2 == 0:
        par.append(num)  # print(f"Enconré un número par : {num}")
        continue
    else:
        impar.append(num)  # print(f"Encontre un número impar {num}")

print(f"par {par}")
print(f"impar {impar}")
```

## Tabla de multiplicar
```python
def tabla_multiplicar(numero):
    "Imprime la tabla de multiplicar"
    for indice in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print(f"{numero} * {indice} = {numero * indice}")

tabla_multiplicar(2)
```


## while
```python
def sumaEnWhile(n):
    "suma los número de 1 a n"
    result = 0
    x = n
    while x > 0:
        result += x
        x -= 1
    return result


sumaEnWhile(5)
```


🚨🚨 Importante: esto se imprime infinitas veces ctrl + c para detener la ejecución
```python
"""
n = 10
while n <= 10:
    # sentencia break en for
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print(f"{n} es igual a {x} * {n//x}")
                break
    else:
        # sigue el bucle sin encontrar un factor
        print(f"{n} es un número primo")
"""
```