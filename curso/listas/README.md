[Programación de algoritmos](../README.md)
# Listas

```python
def persona(nombre="marco", edad="33", sexo="Masculino"):
    print("Hola", nombre, end=" ")
    print("tu edade es", edad, end=" ")
    print("tu sexo es", sexo, end=" \n")


p = {"nombre": "Jehtro", "edad": "35", "sexo": "Hombre"}
persona(**p)
```