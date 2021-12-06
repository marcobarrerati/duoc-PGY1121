[Programación de algoritmos](../README.md)
# Ejercicios
```python
import random

# Instrucciones
# Crear un programa que simule la tirada de datos.

# Cada vez que ejecutamos el programa, éste elegirá dos números aleatorios entre el 1 y el 6
# El programa deberá imprimirlos en pantalla, imprimir su suma y preguntarle al usuario si quiere tirar los datos otra vez.

# Versión 1
def tira_dados():
    numeros = []
    for l in [0, 1]:
        aleatorio = random.randint(1, 6)
        numeros.append(aleatorio)
    print(f"Los dos números son {numeros[0]} y {numeros[1]}  La suma es {sum(numeros)}")
    ok = input("¿Tirar otra vez? (posibles respuestas s, S, si, Si, SI)")
    if ok in ("s", "S", "si", "Si", "SI"):
        tira_dados()
    else:
        print("fin del programa")


# tira_dados()  # ejecutar

# Versión 2
tirar = "s"
while tirar == "s":
    numeros = random.choices([1, 2, 3, 4, 5, 6], k=2)
    print(f"Los números son {numeros}  y la suma es {sum(numeros)}")
    tirar = input("¿Tirar otra vez?: s/n")
else:
    print(f"fin del programa la variable tirar ahora es {tirar}")

```
número primo
```python
def es_primo(numero):
    resultado = True
    contador = 0
    for divisor in range(2, numero):
        contador += 1
        if (numero % divisor) == 0:
            resultado = False
            break
    return contador


print(es_primo(13))


```
```python

nombre = []
contador = 0
while(contador < 3):
    nombre.append(input("ingrese un nombre:\n"))
    contador = contador+1
aux = 0
largo = 0
for i in range(3):
    if(i == 0):
        # aqui se almacena el primer registro de la lista, la cantidad de caracteres
        largo = len(nombre[i])

    else:  # la seguna vuelta del for i vale 1, aqui comenzamos a comparar
        # nombre[1]--> if( cantidad caracteres de nombre[0]<cantidad de caracteres nombre[1])
        if(largo < len(nombre[i])):
            aux = i  # aux=1
            largo = len(nombre[i])

print(nombre[aux])


```
```python
personas = 0
lista = []
mayor = 0
while (int(personas) <= 2):
    nombre = input("Ingrese el nombre de la persona :  " + str(personas) + " ")
    if (len(nombre)) > 0:
        lista.append({"nombre": nombre, "largo": len(nombre)})
        personas += 1

""" print("el nombre más largo es " + max(lista) + "y tiene " +
      str(len(max(lista, key=len))) + " caracteres") """

print(lista)

```


