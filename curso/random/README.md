[Programación de algoritmos](../README.md)
# Random
```python
import random

# 1- 10 número random  del 0 al 10
lista = []
for i in range(10):
    lista.append(random.randrange(10))

print("lista", lista)

# 2- imprimir número par
for i in lista:
    if(i % 2 == 0):
        print("número par", i)

# 3 y 4- imprimir número mayor
mayor = 0
for i in lista:
    if(i > mayor):
        mayor = i

print("el mayor es", mayor, " y su posición es", lista.index(i))

# 5, 6 -
vector = [""]*10
opcion = 0
contador = 0
while(opcion != 3):
    print("1- meú")
    print("2- listar")
    opcion = input(input("ingresa opción"))
    if(opcion == 1):
        nombre = input("nombre")
        vector[contador] = nombre
        contador = contador + 1
    if(opcion == 2):
        for i in range(contaddor):
            print((f"{i+1}){vector[i]}"))

```