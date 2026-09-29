def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print("Lista original: ", listaNumeros)
print("Largo de la lista: ", len(listaNumeros))

while len(listaNumeros) > 0:
    numero = listaNumeros.pop(0)
    if es_par(numero):
        print("Número par: ", numero)
    else:
        print("Número impar: ", numero)