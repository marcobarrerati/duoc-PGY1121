[Programación de algoritmos](../README.md) | versión 20210612  
# Evaluación 3 
## Centro Médico DUOC
### Datos de paciente
1. run, sin dígito verificador y puntos
1. nombre
1. dirección
1. correo
1. edad, solo números entre 0 y 110
1. sexo, permitir letra f o m
1. registros
1. ps, isapre o fonasa
1. datos de de atenciones
### Opciones de sistema
1. 1️⃣ Registrar datos de paciente
1. 2️⃣ Registrar datos de atención de paciente
1. 3️⃣ Consultar datos de paciente
1. 4️⃣ Salir del sistema
---
## Desarrollo
1. Registrar datos de paciente:
```
     0  - Opción 2 en el sistema
     1  - Completar la ficha del paciente
          - run : número entre 5000000 y 99999999
          - edad: número entero que se encuentre en el rango de 0 y 110
          - sexo: letra f o m, mayúscula o minúscula
          - ps: solo acepta las palabras, isapre y fonasa
          - correo: debe ser una cadena de caracteres > 4 que tenga un @
          - dirección
     1.1 Verificar que el paciente no este registrado
```
1. Atención de paciente
```
      0  - Opción 2 en el sistema
      1  - Solicitar run del paciente
      2  - Verificar que el run existe
      2.1- Si existe se debe solicitar fecha y las observaciones de la visita
      2.2- Almacenar los datos concatenando con datos anteriores
```
1. Consultar datos de paciente
```
      1  - Solicitar run del paciente
      2  - Verificar que el run existe
      2.1- Si existe mostrar los datos
```
1. Salir
```
     1  - Finalizar sistema y mostrar un mensaje "ha salido del sistema"
```
## Programa
```python

opt = 0
patients = []
menu = [
    {"value": 1, "label": "Registra paciente", "icon": "1️⃣"},
    {"value": 2, "label": "Atención paciente", "icon": "2️⃣"},
    {"value": 3, "label": "Consultar paciente", "icon": "3️⃣"},
    {"value": 4, "label": "Salir", "icon": "4️⃣"}
]
patientAll = []
print("", end="\n")
print("🎓 Centro Médico DUOC", end="\n")

while(opt != 4):
    print("", end="\n")
    print("🛠  Opciones", end="\n")
    print("", end="\n")
    for m in menu:  # crear menú de sistema
        print(m["icon"], " ", m["label"], " ", end="\n")
    print("", end="\n")
    try:  # Evaluar selección del menú
        opt = int(input("👨🏻‍💻 Ingresa un número para usar el sistema: "))
        if(opt > 0 and opt < 5):
            if(opt == 4):
                print("", end="\n")
                print("🥺 Hasta pronto, ha salido del sistema", end="\n")
                print("", end="\n")
            else:
                print("", end="\n")
            if(opt == 1):
                print("😷 Agregar paciente", end="\n")
                print("", end="\n")
                print("👨🏻‍💻 Registrar datos", end="\n")
                print("", end="\n")

                patientForm = [
                    {"key": "run", "label": "RUN", "value": "", "readonly": False,
                        "valid": False, "msg": "ingresa un número entre 5000000 y 99999999"},
                    {"key": "nombre", "label": "Nombre", "value": "",
                        "readonly": False, "valid": False, "msg": ""},
                    {"key": "direccion", "label": "Dirección", "value": "",
                        "readonly": False, "valid": False, "msg": ""},
                    {"key": "correo", "label": "Correo", "value": "", "readonly": False,
                        "valid": False, "msg": "debe ser una cadena de caracteres > 4 que tenga un @"},
                    {"key": "edad", "label": "Edad", "value": "", "readonly": False,
                        "valid": False, "msg": "ingresa un número en el rango de 0 y 110"},
                    {"key": "sexo", "label": "Sexo", "value": "", "readonly": False,
                        "valid": False, "msg": "ingresa una letra:  M: masculino, F: femenino"},
                    {"key": "ps", "label": "PS", "value": "", "readonly": False, "valid": False,
                        "msg": "ingresa una letra para la previsión  social:  F: fonasa, I: isapre"},
                    {"key": "registros", "value": [],
                        "readonly":True, "valid":False, "msg":""}
                ]

                for p in patientForm:
                    while(p["valid"] == False and p["readonly"] == False):
                        p["value"] = input(p["label"] + "(" + p["msg"] + "): ")
                        try:
                            if(p["key"] == "run"):
                                if(int(p["value"]) >= 5000000 and int(p["value"]) <= 99999999):
                                    existe = False
                                    # todos los pacientes agrupados en una lista
                                    for pAll in (patientAll):
                                        for pd in pAll:  # todos los atributos de paciente
                                            if(pd["key"] == "run"):  # comparamos por run
                                                # si el run buscado existe
                                                if(pd["value"] == p["value"]):
                                                    print("", end="\n")
                                                    print(
                                                        "😛 El paciente ya existe, no podemos registralo 2 veces", end="\n")
                                                    # print(p) # imprimir datos del paciente...
                                                    print("", end="\n")
                                                    existe = True
                                    if(existe == False):
                                        p["valid"] = True
                            elif(p["key"] == "nombre"):
                                p["valid"] = True
                            elif(p["key"] == "direccion"):
                                p["valid"] = True
                            elif(p["key"] == "correo"):
                                if(len(p["key"]) > 4):
                                    contadorArroba = 0
                                    for l in p["value"]:
                                        if(l == "@"):
                                            contadorArroba = contadorArroba+1
                                    if(contadorArroba == 1 and len(p["value"]) > 4):
                                        p["valid"] = True
                            elif(p["key"] == "edad"):
                                if(int(p["value"]) >= 0 and int(p["value"]) <= 110):
                                    p["valid"] = True
                            elif(p["key"] == "sexo"):
                                sexoIn = p["value"].lower()
                                if(sexoIn == "f" or sexoIn == "m"):
                                    p["valid"] = True
                            elif(p["key"] == "ps"):
                                psIn = p["value"].lower()
                                if(psIn == "f" or psIn == "i"):
                                    p["valid"] = True
                            else:
                                print("validar")
                                print(["value"])
                        except:
                            print(p["msg"])
                #  si todo va bien... registramos
                patientAll.append(patientForm)
                print("", end="\n")
                print("🎉 Paciente registrado en el sistema", end="\n")
                print("", end="\n")
            elif(opt == 2):
                print("👨🏻‍⚕️ Atender paciente", end="\n")
                print("", end="\n")
                patientsearch = input("🕵🏻 Ingresa el run del paciente : ")
                print("🕵🏻  Buscando...", end="\n")
                encontrado = False
                patient = False
                for p in (patientAll):  # todos los pacientes agrupados en una lista
                    for pd in p:  # todos los atributos de paciente
                        if(pd["key"] == "run"):  # comparamos por run
                            # si el run buscado existe
                            if(patientsearch == pd["value"]):
                                encontrado = True
                                patient = p
                if(encontrado == True):
                    print("", end="\n")
                    print(
                        "🎉 Paciente encontrado, ingresa los datos de la atención", end="\n")
                    fecha = input("FECHA: ")
                    observacion = input("OBSERVACIÓN: ")
                    for p in patient:
                        if(p["key"] == "registros"):
                            p["value"].append(
                                {"fecha": fecha, "observacion": observacion})
                            print("", end="\n")
                            print("🎉 Datos registrados", end="\n")
                            print("", end="\n")
                else:
                    print("🥺 No existe paciente para el run " +
                          patientsearch, end="\n")
                    print("👽 Puedes registrarlo en la opción 1", end="\n")
                    print("", end="\n")
            elif(opt == 3):
                print("🕵🏻 Consultar por paciente:", end="\n")
                print("", end="\n")
                patientsearch = input("🕵🏻 Ingresa el run del paciente : ")
                print("", end="\n")
                print("🕵🏻 Buscando...", end="\n")
                print("", end="\n")
                encontrado = False
                patient = False
                for p in (patientAll):  # todos los pacientes agrupados en una lista
                    for pd in p:  # todos los atributos de paciente
                        if(pd["key"] == "run"):  # comparamos por run
                            # si el run buscado existe
                            if(patientsearch == pd["value"]):
                                encontrado = True
                                patient = p
                if(encontrado == True):
                    print("", end="\n")
                    print("🎉 Paciente encontrado", end="\n")
                    print("", end="\n")
                    for p in patient:  # recorrer atributos del paciente
                        if(p["key"] != "registros"):
                            print("{:<8} {:<15}".format(
                                p["label"], p["value"]))
                        else:
                            print("", end="\n")
                            print("Atenciones", end="\n")
                            print("", end="\n")
                            print("{:<8} {:<15}".format(
                                'Fecha', 'Observación'))
                            for r in p["value"]:
                                print("{:<8} {:<15}".format(
                                    r["fecha"], r["observacion"]))
                    print("", end="\n")
                else:
                    print("🥺 No existe paciente para el run " +
                          patientsearch, end="\n")
                    print("👽 Puedes registrarlo en la opción 1", end="\n")
                    print("", end="\n")

        else:
            print("😰 Ingresa una opción del sistema")
            print("", end="\n")
    except:
        print("Sólo puedes ingresar números disponibles en el sistema")
        print("", end="\n")

```