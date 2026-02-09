def primos():
    cantidad = int(input("Cuántos números desea evaluar: "))
    lista = []
    contador: int = 2

    for i in range(cantidad):
        x = int(input("Ingrese el numero " + str(i+1) + " de su lista: "))
        lista.append(x)

    lista_primos = []

    for numero in lista:
        es_primo = True
        
        for contador in range(2, numero):
            if numero % contador == 0:
                es_primo = False
                break

        if numero > 1 and es_primo:
            lista_primos.append(numero)

    return lista_primos


if __name__ == "__main__":
    print(primos())


# Para este problema se creó una función en donde el usuario puede poner la cantidad de números que desee en la lista.
# Mediante un for se recorre cada número de la lista y se inicializa una bandera con valor True. Posteriormente, se evalua si el módulo
# (residuo) es igual a 0, respecto a 2, y así sucesivamente hasta que el contador se actualice progresivamente al número - 1
# Si el módulo es 0 en algún momento, el número no será primo por lo que la bandera se actualizará. Finalmente, los números primos
# se guardarán en una nueva lista.
