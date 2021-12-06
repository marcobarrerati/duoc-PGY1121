[Programación de algoritmos](../README.md)
# Evaluación 2 
## Objetivo 
Programa para cine con venta de boletos y agregados (palomitas y bebidas)
## Procesos
```
1- Preguntar al cliente si pertenece a Duoc (estudiante o funcionario)
1.1 si el cliente pertenece se debe almacenar True en caso contrario registrar False
2- Preguntar al cliente el tipo de entrada
1- Estreno $4.800
    2- Normal $2.900
3- Preguntar al cliente la cantidad de entradas
4- Preguntar al cliente si necesita palomitas
4.1. Si el cliente ingresa "si" se debe mostrar las promociones:
1- Palomitas Pequeñas $2.500
    2- Palomitas Medianas   $4.500
3- Palomitas Grande $7.800
4.1.1- preguntar al cliente la cantidad
5- Preguntar al cliente si necesita bebidas
    1- Bebida Grande    $1.000
2- Bebida Mediana $1.250
    3- Bebida Grande    $2.500
6- Mostrar al cliente el total a pagar
7- Solicitar el efectivo
8- calcular el vuelto
8.1- Si el cliente pertenece a Duoc, aplicar descuento de 30% a las entradas
```

```python

opt = 0
tickets = [
    {"key": "e", "label": "Estreno", "value": 4800, "total": 0},
    {"key": "n", "label": "Normal", "value": 2900, "total": 0}
]
popcorns = [
    {"key": "s", "type": "small", "label": "Pequeña", "value": 2500, "total": 0},
    {"key": "m", "type": "medium", "label": "Mediana", "value": 4500, "total": 0},
    {"key": "l", "type": "large", "label": "Grande", "value": 7800, "total": 0}
]
bebidas = [
    {"key": "s", "type": "small", "label": "Bebida Pequeña", "value": 1000, "total": 0},
    {"key": "m", "type": "medium", "label": "Bebida Mediana", "value": 1250, "total": 0},
    {"key": "l", "type": "large", "label": "Bebida Grande", "value": 2500, "total": 0}
]
ticket = [
    {"cliente": [{"run": "", "duoc": False}], "type": "",
        "value": 0, "total": 0, "popcorns": [], "bebidas":[]}
]
menu = [
    {"value": 1, "label": "Iniciar Venta", "symbol": "1️⃣"},
    {"value": 2, "label": "Imprimir Venta", "symbol": "2️⃣"},
    {"value": 3, "label": "Salir", "symbol": "3️⃣"}
]
print("", end="\n")

while(opt != 3):1
    print("", end="\n")
    print("🎓 Cine DUOC", end="\n")
    print("🛠  Opciones", end="\n")
    print("", end="\n")
    for m in menu:  # crear menú de sistema
        print(m["symbol"], " ", m["label"], " ", end="\n")
    print("", end="\n")
    try:  # Evaluar selección del menú
        opt = int(input("👨🏻‍💻 Ingresa un número para usar el sistema: "))
        if opt > 0 and opt < 3:
            if opt == 3:
                print("", end="\n")
                print("🥺 Hasta pronto, ha salido del sistema", end="\n")
                print("", end="\n")
            else:
                print("", end="\n")
            if opt == 1:
                print("Iniciar venta", end="\n")
                print("", end="\n")
                print("👨🏻‍💻 Ingresa datos del cliente", end="\n")
                print("", end="\n")
                clientForm = [
                    {"key": "run", "label": "RUN", "value": "", "valid": False,
                        "msg": "ingresa un número entre 11111111 y 99999999"},
                    {"key": "duoc", "label": "Duoc", "value": "",
                        "valid": False, "msg": "ingresa s o n"}
                ]
                for inp in clientForm:
                    while(inp["valid"] == False):
                        inp["value"] = input(
                            inp["label"] + "("+inp["msg"]+"): ")
                        try:
                            if(inp["key"] == "run"):
                                if(int(inp["value"]) >= 11111111 and int(inp["value"]) <= 99999999):
                                    inp["valid"] = True
                                    ticket[0]["cliente"][0]["run"] = int(
                                        inp["value"])
                            elif(inp["key"] == "duoc"):
                                if((inp["value"]) == "s" or (inp["value"]) == "n"):
                                    inp["valid"] = True
                                    if inp["value"] == "s":
                                        ticket[0]["cliente"][0]["duoc"] = True
                        except:
                            print(inp["msg"])
                print("", end="\n")
                print("Ticket Disponibles", end="\n")
                print(("{:<8} {:<15} {:<25}").format(
                    "Opción", "Tamaño", "Valor"))
                for t in tickets:
                    print(("{:<8} {:<15} {:<25}").format(
                        t["key"], t["label"], t["value"]))
                print("", end="\n")

                ticketForm = [
                    {"key": "type", "label": "Tipo de Ticket", "value": "", "valid": False,
                        "msg": "Ingresa el tipo de ticket (e:Estreno $4800, n:Normal $2800)"},
                    {"key": "total", "label": "Cantidad de Ticket", "value": "",
                        "valid": False, "msg": "Ingresa la cantidad de ticket (1 al 4)"}
                ]
                for inp in ticketForm:
                    while inp["valid"] == False:
                        inp["value"] = input(inp["label"]+"("+inp["msg"]+"): ")
                        try:
                            if(inp["key"] == "type"):
                                if inp["value"] == "e" or inp["value"] == "n":
                                    inp["valid"] = True
                                    for ti in tickets:
                                        if ti["key"] == inp["value"]:
                                            ticket[0]["type"] = ti["label"]
                                            ticket[0]["value"] = ti["value"]
                            if inp["key"] == "total":
                                if int(inp["value"]) >= 1 and int(inp["value"]) <= 4:
                                    inp["valid"] = True
                                    ticket[0]["total"] = int(inp["value"])
                        except:
                            print(inp["msg"])

                optPopCorn = 0
                print("", end="\n")
                print("¿ Necesita Palomitas ? (n : para salir)")
                print("", end="\n")
                print(("{:<8} {:<15} {:<25}").format(
                    "Opción", "Tamaño", "Valor"))
                for p in popcorns:
                    print(("{:<8} {:<15} {:<25}").format(
                        p["key"], p["label"], p["value"]))
                while optPopCorn != "n":
                    optPopCorn = (
                        input("Ingresa el tipo de Palomitas: (s, m, l o n para continuar)"))
                    try:
                        if optPopCorn.lower() == "s" or optPopCorn.lower() == "m" or optPopCorn.lower() == "l":
                            for t in popcorns:
                                if t["key"] == optPopCorn.lower():
                                    t["total"] = input(
                                        "ingresa la cantidad (1 a 4)")
                                    if int(t["total"]) >= 1 and int(t["total"]) <= 4:
                                        ticket[0]["popcorns"].append(t)
                    except:
                        print("ingresa opciones disponibles (s, m, l, n)")

                optBebida = 0
                print("", end="\n")
                print("¿ Necesitas Bebidas ? (n : para salir)")
                print("", end="\n")
                print(("{:<8} {:<15} {:<25}").format(
                    "Opción", "Tamaño", "Valor"))
                for p in bebidas:
                    print(("{:<8} {:<15} {:<25}").format(
                        p["key"], p["label"], p["value"]))
                while optBebida != "n":
                    optBebida = (
                        input("Ingresa el tipo de Bebida: (s, m, l o n para continuar)"))
                    try:
                        if optBebida.lower() == "s" or optBebida.lower() == "m" or optBebida.lower() == "l":
                            for t in popcorns:
                                if t["key"] == optBebida.lower():
                                    t["total"] = input(
                                        "ingresa la cantidad (1 a 4)")
                                    if int(t["total"]) >= 1 and int(t["total"]) <= 4:
                                        ticket[0]["bebidas"].append(t)
                    except:
                        print("ingresa opciones disponibles (s, m, l, n)")

            elif opt == 2:
                print("Imprimir Venta", end="\n")
                print("", end="\n")

                duoc = "NO"
                totalVenta = 0
                for t in ticket:
                    total = int(t["total"]) * int(t["value"])
                    if t["cliente"][0]["duoc"] == True:
                        duoc = "SI, aplica 30% de descuento en total de las entradas"
                        total = total-(total * 30)/100
                    print(("{:<8} {:<15}").format("Cliente", "Duoc"))
                    print(("{:<8} {:<15}").format(
                        t["cliente"][0]["run"], duoc))
                    print("", end="\n")
                    print("Entradas")
                    print("", end="\n")
                    print(("{:<8} {:<15} {:<20} {:<25}").format(
                        "Entrada", "Valor", "Cantidad", "Total"))
                    print(("{:<8} {:<15} {:<20} {:<25}").format(
                        t["type"], t["value"], t["total"], total))
                    totalVenta = total
                    print("", end="\n")
                    print("Palomitas")
                    print("", end="\n")
                    print(("{:<8} {:<15} {:<20} {:<25}").format(
                        "Palomita", "Valor", "Cantidad", "Total"))
                    for p in t["popcorns"]:
                        total = int(p["value"]) * int(p["total"])
                        print(("{:<8} {:<15} {:<20} {:<25}").format(
                            p["label"], p["value"], p["total"], total))
                        totalVenta = totalVenta+total
                    print("", end="\n")
                    print("Bebidas")
                    print("", end="\n")
                    print(("{:<8} {:<15} {:<20} {:<25}").format(
                        "Bebidas", "Valor", "Cantidad", "Total"))
                    for p in t["bebidas"]:
                        total = int(p["value"]) * int(p["total"])
                        print(("{:<8} {:<15} {:<20} {:<25}").format(
                            p["label"], p["value"], p["total"], total))
                        totalVenta = totalVenta+total
                print("", end="\n")
                print("Total de la venta", totalVenta)

            else:
                print("😰 Ingresa una opción del sistema")
                print("", end="\n")
    except:
        print("Sólo puedes ingresar números disponibles en el sistema")
        print("", end="\n")


```