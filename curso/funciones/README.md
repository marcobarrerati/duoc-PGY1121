[Programación de algoritmos](../README.md)
# Funciones
```python
def saludar(nombre):
    return nombre
    x = 0
    if x > 0:
        print("el numero es",x," y es positivo")
    elif x < 0:

        print("el numero es negativo")    
    else:
        print("el numero es cero")    

salud= saludar("hola")
print(salud)

def fib2(n): # devolver la serie de Fibonacci
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


f100 = fib2(100)
print(f100)    

def pedir_confirmacion(promt, reintentos=4, recordatorio='Por favor, intente nuevamente'):
    while True:
        ok = input(promt)
        if ok in ('s','S','si','Si','SI'):
            return True
        if ok in ('n','no','No','NO'):
            return False
        reintentos = reintentos - 1
        if reintentos < 0:
            #reaise ValueError
            print('respuesta de usuarion no correcta')
        print(recordatorio)


pedir_confirmacion('¿Realmente quieres salir?')
pedir_confirmacion('¿Sobreescribir archivo?',2)
pedir_confirmacion('¿Sobreescribir archivo?',2, "Vamos, solo si o no")

def loro(tension, estado='rotizado', accion='explotar'):
    print("-- Este loro no va a", accion )
    print("si le aplicás", tension, "voltios.")
    print("Está", estado, "!")

d = {"tension": "cinco mil", "estado": "demacrado", "accion": "VOLAR"}
loro(**d)


print("fin")


def hacer_incrementador(n):
    return lambda x: x + n


f = hacer_incrementador(42)
print(f)

def mi_funcion():
        """  No hace más que documentar

        No, de verda. No hace nada,
        """
        pass

print(mi_funcion.__doc__)


def f(jamon:str, huevos:str = 'huevos') -> str:
    print("anotaciones:", f.__annotations__)
    print("Argumentos:", jamon, huevos)
    return jamon + 'y' + huevos

    
f('carnes')


def pedir_confirmacion(
    prompt, reintentos=4, recordatorio="Por favor, intente nuevamente"
):
    while True:
        ok = input(prompt)
        if ok in ("s", "S", "si", "Si", "SI"):
            return True
        if ok in ("n", "no", "No", "NO"):
            return False
        reintentos = reintentos - 1
        if reintentos < 0:
            print("reintentos 0")
        print(recordatorio)


pedir_confirmacion("quieres salir")


# guardar variable


def guarda_variable(a, L=[]):
    if L is None:
        L = []
    L.append(a)
    return L


print(guarda_variable(1))
print(guarda_variable(2))
print(guarda_variable(3))


def ventadequeso(tipo, *argumentos, **palabrasclaves):
    print("-- ¿Tiene", tipo, "?")
    print("-- Lo siento, nos quedamos sin", tipo)
    for arg in argumentos:
        print(arg)
    print("--" * 40)
    for c in palabrasclaves:
        print(c, ":", palabrasclaves[c])


ventadequeso(
    "Limburger",
    "Es muy liquido, sr.",
    "Realmente es muy liquido, sr.",
    cliente="uJuan Garau",
    vendedor="Miguel Paez",
    puesto="Venta de Queso Argentino",
)


def concatenar(*arg, sep="/"):
    return sep.join(arg)


print(concatenar("tierra", "marte", "venus"))

print(concatenar("tierra", "marte", "venus", sep="."))


def peso(masa, gravedad=9.8):
    "Formula de peso"
    return masa * gravedad

# Parámetros opcionales
print("Peso en la tierra", peso(10))
print("peso en la luna", peso(10, 1.63))

# Parámetros con palabras claves (o argumento nombrados)
print("Peso en la luna", peso(10, gravedad=1.63))
print("peso en la luna:", peso(masa=10, gravedad=1.63))
print("Peso en la luna", peso(gravedad=1.63, masa=10))

# Esta opción no es valida. Los parámetros posicionales no pueden ir después de un keyboar
# print("Peso en la luna:", peso(masa=10,1.63))
# SyntaxError: positional argument folloes keyword argument

# Lista de parámetros
def suma_numeros(*args):
    "Suma los número pasados por parametro"
    return sum(args)

print("6 + 7 + 8 =", suma_numeros(*[6, 7, 8])) # empaquetado
print("6 + 7 + 8 =", suma_numeros(6, 7, 8)) # desempaquetado

# Diccionario de parámetros
def impirmir_ticket(*arg, **kwargs):
    "Imprime el ticket de una compa"
    print("Detalle Ticket")
    for item, precio in kwargs.items():
        print(item, ":", precio)


# funciones anónimas o reservadas
# se definen con la palabra reservada lambda
# están restringidas a una sola función

f = lambda x: x + 1

print("Tipo de f:", type(f))
print("f(3)=", f(3))

```