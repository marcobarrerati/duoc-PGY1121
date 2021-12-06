[Programación de algoritmos](../README.md) | 20210714
# Examen Transversal

```python
def calcularFactorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial*i
    return [{"numero": n, "factorial": factorial}]


def calculaMatematicaBasica(numeroUno):
    try:
        if int(numeroUno) >= 15 and int(numeroUno) <= 125:
            numeroUnoTxt = str(numeroUno)
            numeroInvertido = ""
            lista = []
            for l in numeroUnoTxt:
                numeroInvertido = l + numeroInvertido
                lista.append(int(l))
            lista.reverse()
            suma, resta, multiplicacion, division = lista[0], lista[0], lista[0], lista[0]
            for l in numeroInvertido[1:]:
                suma += int(l)
                resta -= int(l)
                multiplicacion *= int(l)
                division /= int(l)
            return [{"numeroInvertido": numeroInvertido, "suma": suma, "resta": resta, "multiplicacion": multiplicacion, "division": division, "numero": numeroUno}]
        print(msg)
        return False
    except:
        print(msg)
        return False


listaPersonas = []


def listarPersona():
    return listaPersonas


opt = 0
menu = [
    {"value": 1, "label": "Factorial"},
    {"value": 2, "label": "Invertir número"},
    {"value": 3, "label": "Lista con nombres de persona"},
    {"value": 4, "label": "Salir"}
]

while opt != 4:
    print("", end="\n")
    print("🍔 Opciones", end="\n")
    print("", end="\n")
    for m in menu:
        print(m["value"], m["label"])
        print("", end="\n")
    try:
        opt = int(input("Ingresa un número para usar el sistema : "))
        if opt > 0 and opt < 5:
            if opt == 4:
                print("", end="\n")
                print("🥺 Hasta pronto, ha salido del sistema", end="\n")
                print("", end="\n")
            else:
                print("", end="\n")
                if opt == 1:
                    print("Factorial")
                    numeroValido = False
                    while numeroValido == False:
                        try:
                            numero = int(input("ingresa un número positivo"))
                            if numero > 0:
                                print("✅")
                                print(calcularFactorial(numero))
                                numeroValido = True
                        except:
                            print("solo números")
                elif opt == 2:
                    numeroValido = False
                    while numeroValido == False:
                        try:
                            numero = int(input("ingresa un número positivo"))
                            if numero > 0:
                                resp = calculaMatematicaBasica(numero)
                                if resp == False:
                                    print(
                                        "error, ingresa un número entre 15 y 125")
                                else:
                                    print("✅")
                                    print("{:<10} {:<20} {:<10} {:<10} {:<20} {:<10}".format(
                                        "número", "números invertidos", "suma", "resta", "multiplicación", "división"))
                                    print("{:<10} {:<20} {:<10} {:<10} {:<20} {:<10}".format(resp[0]["numero"], str(
                                        resp[0]["numeroInvertido"]), resp[0]["suma"], resp[0]["resta"], resp[0]["multiplicacion"], resp[0]["division"]))
                                    numeroValido = True
                        except:
                            print("solo números entre 15 y 125")
                elif opt == 3:
                    numeroValido = False
                    while numeroValido == False:
                        try:
                            numero = int(
                                input("ingresa la cantida de personas"))
                            if numero > 0:
                                for p in range(numero):
                                    listaPersonas.append(
                                        input("ingresa nombre de persona : "))
                            print("✅ Lista de personas", listarPersona())
                            numeroValido = True
                        except:
                            print("solo números positivos")

    except:
        print("solo ingresa opciones disponibles")
```