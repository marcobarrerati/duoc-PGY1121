[Programación de algoritmos > curso](../README.md)
# Sentencias If
```python
def evaluaNumero(x):
    " Sentencia if y bloques elif y else"
    if x < 0:
        x = 0
        print("Negativo cambiado a cero")
    elif x == 0:
        print("Cero")
    elif x == 1:
        print("Simple")
    else:
        print("Más")


evaluaNumero(2)
```