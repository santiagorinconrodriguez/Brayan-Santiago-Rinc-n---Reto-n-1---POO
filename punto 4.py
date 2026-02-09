def suma():
    cantidad = int(input("Cuántos números desea evaluar: "))
    lista = []
    lista_sumas = []

    for i in range(cantidad):
        x = int(input("Ingrese el numero " + str(i+1) + " de su lista: "))
        lista.append(x)

    for i in range(len(lista)-1):
        adicion = lista[i] + lista[i+1]
        lista_sumas.append(adicion)

    print("La mayor suma de dos números de la lista " + str(lista) +
          " es: " + str(max(lista_sumas)))


if __name__ == "__main__":
    suma()

# Se hizo un programa con una función donde el usuario ingreso la cantidad de números a ser evaluados en una lista.
# Para luego, mediante un ciclo for, sumar el primer elemento de la lista con el siguiente elemento, guardando el resultado 
# en otra lista. Se le aclaró al programa que el último elemento señalado será el penúltimo para no caer en un error.
# Para finalizar, mediante la función max(), se identificó cuál era la suma mayor.
