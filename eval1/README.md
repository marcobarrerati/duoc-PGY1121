[Programación de algoritmos](../README.md)
# Evaluación 1 
## Enunciado
Se desea crear un sistema informática el cual utilizando los datos de día de nacimiento y mes de nacimiento (datos ingresados y solicitados por pantalla) muestre que signo zodiacal es el usuario y también deberá mostrar una lectura de su signo, la información de cada signo puede ser inventada.

Para ello se recomienda trabajar con mes en forma numérica (opcional). Ejemplo:
```
Día = 15
mes = 7
Usuario = Cáncer.
Descripción = Encontrará el amor de su vida en los próximos 107 meses.
```


```python
# python
opt = 0
zodiaco =[
{"monthStart":1,"monthEnd":2,"dayStart":20,"dayEnd":18,"signo":"Acuario","message":"Hola Acuario","symbol":"♒️"},
{"monthStart":2,"monthEnd":3,"dayStart":19,"dayEnd":20,"signo":"Piscis","message":"Hola Piscis","symbol":"♓️"},
{"monthStart":3,"monthEnd":4,"dayStart":21,"dayEnd":19,"signo":"Aries","message":"Hola Aries","symbol":"♈️"},
{"monthStart":4,"monthEnd":5,"dayStart":20,"dayEnd":20,"signo":"Tauro","message":"Hola Tauro","symbol":"♉️"},
{"monthStart":5,"monthEnd":6,"dayStart":21,"dayEnd":20,"signo":"Géminis","message":"Hola Géminis","symbol":"♊️"},
{"monthStart":6,"monthEnd":7,"d11ayStart":21,"dayEnd":22,"signo":"Cáncer","message":"Hola Cáncer","symbol":"♋️"},
{"monthStart":7,"monthEnd":8,"dayStart":23,"dayEnd":22,"signo":"Leo","message":"Hola Leo","symbol":"♌️"},
{"monthStart":8,"monthEnd":9,"dayStart":23,"dayEnd":22,"signo":"Virgo","message":"Hola Virgo","symbol":"♍️"},
{"monthStart":9,"monthEnd":10,"dayStart":23,"dayEnd":22,"signo":"Libra","message":"Hola Libra","symbol":"♎️"},
{"monthStart":10,"monthEnd":11,"dayStart":23,"dayEnd":21,"signo":"Escorpio","message":"Hola Escorpio","symbol":"♏️"},
{"monthStart":11,"monthEnd":12,"dayStart":23,"dayEnd":21,"signo":"Sagitario","message":"Hola Sagitario","symbol":"♐️"},
{"monthStart":12,"monthEnd":1,"dayStart":22,"dayEnd":19,"signo":"Capricornio","message":"Hola Capricornio","symbol":"♑️"}
]
menu =[
{"value":1,"label":"Ver Horoscopo","symbol":"1️⃣"},
{"value":2,"label":"Salir","symbol":"2️⃣"}
]
print("",end="\n")
print("🎓 Zodiaco DUOC", end="\n")

while(opt != 2):
    print("",end="\n")
    print("🛠  Opciones",end="\n")
    print("",end="\n")
    for m in menu: # crear menú de sistema
        print(m["symbol"]," ", m["label"]," ", end="\n")
    print("",end="\n")
    try:# Evaluar selección del menú
        opt = int(input("👨🏻‍💻 Ingresa un número para usar el sistema: "))
        if(opt>0 and opt<2):
            if(opt == 2):
                print("",end="\n")
                print("🥺 Hasta pronto, ha salido del sistema", end="\n")
                print("",end="\n")
            else:
                print("",end="\n")
            if(opt == 1):
                print(" Ver Horoscopo", end="\n")
                print("",end="\n")
                print("👨🏻‍💻 Ingresa datos",end="\n")
                print("",end="\n")

                horoscopoForm=[
                {"key":"day","label":"Día","value":"","valid":False,"msg":"ingresa un número entre 1 y 31"},
                {"key":"month","label":"Mes","value":"","valid":False,"msg":"ingresa un número entre 1 y 12"}
                ]
                dayInp = 0
                monthInp = 0
                for inp in horoscopoForm:
                    while(inp["valid"] == False):
                        inp["value"] = input(inp["label"]+ "("+inp["msg"]+"): ")
                        try:
                            if(inp["key"] == "day"):
                                if(int(inp["value"]) >= 1 and int(inp["value"]) <= 31 ):
                                    inp["valid"] = True
                                    dayInp = int(inp["value"])
                            elif(inp["key"]=="month"):
                                if(int(inp["value"]) >= 1 and int(inp["value"]) <= 12 ):
                                    inp["valid"] = True
                                    monthInp = int(inp["value"])
                        except:
                            print(inp["msg"])

                print ("{:<8} {:<15} {:<25}".format('Símbolo','Signo','Mensaje'))
                for z in zodiaco:
                    if (dayInp >= z["dayStart"] and monthInp == z["monthStart"]) or (dayInp <= z["dayEnd"] and monthInp == z["monthEnd"]):
                        print ("{:<8} {:<15} {:<25}".format(z["symbol"],z["signo"],z["message"]))
            else:
                print("😰 Ingresa una opción del sistema")
                print("",end="\n")
    except:
        print("Sólo puedes ingresar números disponibles en el sistema")
        print("",end="\n")

```
