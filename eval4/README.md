[Programación de algoritmos](../README.md)
# Evaluación 4
## Enunciado 1
Vuelos-Duoc requiere contratar de tus servicios de informática para el desarrollo de un proyecto en Python para la venta de sus pasajes, el sistema es bastante simple, lo primero que hay que tener en cuenta es que son en total 41 asientos por avión, como se ve a continuación:

```
|	1	2	3		4	5	6	|
|								|
|	7	8	9		10	11	12	|
|								|
|	13	14	15		16	17	18	|
|								|
|	19	20	21		22	23	24	|
|								|
|	25	26	27		28	29	30	|
|                               |
|	31	32	33		34	35	36	|
|								|
|	37	38	39		40	41	42	|
```

Donde desde el asiento 31 al 42 se consideran asientos para pasajeros vip.

Los precios de un asiento normal son de $78.900, mientras que los de un asiento vip son de $240.000.

El sistema deberá permitir al usuario seleccionar un asiento disponible (mostrando los asientos disponibles) e indicar el valor, una vez que el usuario acepte, deberá solicitar los datos del usuario, en los cuales tenemos nombrePasajero, rutPasajero, telefonoPasajero y bancoPasajero, además, el sistema deberá implementar el siguiente menú:

    •	Ver asientos disponibles
    •	Comprar asiento
    •	Anular vuelo
    •	Modificar datos de pasajero
    •	Salir

Ver asientos disponibles mostrará por pantalla todos los asientos disponibles con su número de asiento y los no disponibles los con una “X”

```
|	1	2	3		4	5	6	|
|								|
|	7	X	X		10	11	12	|
|								|
|	X	X	X		16	X	18	|
|								|
|	19	20	21		22	23	24	|
|								|
|	25	26	27		X	29	30	|
|                               |
|	X	32	33		34	35	36	|
|								|
|	X	38	X		40	41	X	|
```

### Comprar asiento
Solicita los datos del usuario, luego el usuario escoge un asiento, si es usuario de “bancoDuoc” el sistema le realiza un 15% de descuento en el total de su pasaje.

### Anular Pasaje
Deja el asiento nuevamente disponible y elimina los datos del usuario.

### Modificar datos de pasajero
Solicita el asiento y Rut (para verificar datos) luego muestra un submenú en el cual debe escoger que dato va a modificar:
Puede modificar nombrePasajero y telefonoPasajero.

Para realizar la evaluación se recomienda crear arreglo multidimensional.

```python
opt = 0
menu = [
    {"value": 1, "label": "Ver Asientos"},
    {"value": 2, "label": "Comprar Asiento"},
    {"value": 3, "label": "Anular Vuelo"},
    {"value": 4, "label": "Modificar Datos de Pasajero"},
    {"value": 5, "label": "Salir"}]
pasajes = []
pasajeros = []
print("", end="\n")
print("🎓 Vuelos DUOC", end="\n")
while opt != 5:
    print("", end="\n")
    print("🛠 Opciones", end="\n")
    print("", end="\n")
    for m in menu:
        print(m["value"], m["label"])
        print("", end="\n")
    try:
        opt = int(input("Ingresa un número para usar el sistema : "))
        if opt > 0 and opt < 5:
            if opt == 5:
                print("", end="\n")
                print("🥺 Hasta pronto, ha salido del sistema", end="\n")
                print("", end="\n")
            else:
                print("", end="\n")
                if opt == 1:
                    print("Ver asientos")
                    for a in range(1, 42):
                        disponible = True
                        for p in pasajeros:
                            for pa in p:
                                if pa["key"] == "asiento":
                                    if int(pa["value"]) == int(a):
                                        disponible = False
                                    if disponible == False:
                                        print("x")
                                    else:
                                        print(a)
                elif opt == 2:
                    descuento = False
                    personForm = [
                        {"key": "asiento", "label": "Asiento", "value": "",
                            "valid": False, "msg": "ingresa un asiento disponible"},
                        {"key": "run", "label": "RUN", "value": "", "valid": False,
                            "msg": "ingresa un número entre 11111111 y 99999999"},
                        {"key": "nombre", "label": "Nombre",
                            "value": "", "valid": False, "msg": ""},
                        {"key": "banco", "label": "Banco", "value": "",
                            "valid": False, "msg": "Es de bancoDuoc (s, n)"},
                        {"key": "price", "label": "Precio",
                            "value": "", "valid": True, "msg": ""},
                    ]
                    for p in personForm:
                        while p["valid"] == False:
                            p["value"] = input(p["label"] + "("+p["msg"]+"): ")
                            try:
                                if p["key"] == "run":
                                    if int(p["value"]) >= 11111111 and int(p["value"]) <= 99999999:
                                        existe = False
                                        for pa in pasajeros:
                                            for paa in pa:
                                                if paa["key"] == "run":
                                                    if paa["value"] == p["value"]:
                                                        print("", end="\n")
                                                        print(
                                                            "El pasajero ya existe, no podemos registrarlo")
                                                        print("", end="\n")
                                                        existe = True
                                        if existe == False:
                                            p["valid"] = True
                                elif p["key"] == "nombre":
                                    p["valid"] = True
                                elif p["key"] == "banco":
                                    if p["value"].lower() == "s" or p["value"].lower() == "n":
                                        p["valid"] = True
                                        p["value"] = True

                                elif p["key"] == "asiento":
                                    print("valor", p["value"])
                                    if int(p["value"]) > 0 and int(p["value"]) < 42:
                                        print(
                                            "estamos en asiento SI SI", p["key"])
                                        existe = False
                                        for pa in pasajeros:
                                            for paa in pa:
                                                if paa["key"] == "asiento":
                                                    if int(paa["value"]) == int(p["value"]):
                                                        print("", end="\n")
                                                        print(
                                                            "El asiento no esta disponible")
                                                        print("", end="\n")
                                                        existe = True
                                        if existe == False:
                                            price = 0
                                            if int(p["value"]) > 30 and int(p["value"]) < 43:
                                                price = "240000"
                                            else:
                                                price = "78900"
                                        print("valor del asiento", price,
                                              " ¿lo necesita? (s, n)")
                                        acepta = input("¿Lo necesita? (s)")
                                        if acepta == "si":
                                            p["valid"] = True
                                            personForm[4]["value"] = price

                            except:
                                print(p["msg"])
                    print(personForm)
                    pasajeros.append(personForm)
                    print(pasajeros)
    except:
        print("solo ingresa opciones disponibles")

```


## Enunciado 2

Dadas dos listas pobladas con elementos de tipo carácter, se pide generar una tercera sólo con los elementos que estén repetidos en ellas. Considerar que la nueva lista no contenga elementos duplicados.

## Enunciado 3
Declarar y poblar un arreglo unidimensional de largo 10 con números enteros positivos, utilizando la función random, luego ingrese un número e indique si éste se encuentra en el arreglo.

## Enunciado 4
Ingresar dos números enteros positivos entre 3 y 6, ambos inclusive, luego esos números serán las dimensiones de un arreglo bidimensional. Posteriormente, poblar la matriz con números reales. Finalmente, muestre:
• La suma por filas
• El promedio por columnas

## Enunciado 5
Crear un programa que permita el ingreso de dos números enteros, luego debe llamar a una función que reciba estos números y que realice lo siguiente:
• Si el primer número es mayor que el segundo, debe devolver 1.
• Si el primer número es menor que el segundo, debe devolver -1.
• Si ambos números son iguales, debe devolver un 0.

## Enunciado 6
Crear un programa que contenga un menú con las siguientes opciones:
• Área de un circulo
• Perímetro de un cuadrado

Ingrese los valores necesarios para calcular y entregar resultados utilizando funciones

## Enunciado 7
Ingresar un número entero entre 10 y 15, este número será el máximo de número que debe mostrar en la serie Fibonacci.

## Enunciado 8
Ingrese una palabra, luego indique:
• Si es un Palíndromo (es una palabra o frase que se lee igual en un sentido que en otro)
• Cantidad de letras que contiene.
