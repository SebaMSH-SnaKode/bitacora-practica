

listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Lista original: ", listaNumeros)
print("Largo de la lista: ", len(listaNumeros))


for numero in range(len(listaNumeros)):

    if listaNumeros[numero] % 2 == 0:
        print("Número par: ", listaNumeros[numero])
    else:
        print("Número impar: ", listaNumeros[numero])





