def mismos_caracteres():
    palabras = int(input("Ingrese la cantidad de palabras que va a ingresar: "))
    lista = []
    guardar = []

    for i in range(palabras):
        palabra = input("Ingrese su palabra numero " + str(i+1) + ": ")
        lista.append(palabra)

    resultado = []

    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if sorted(lista[i]) == sorted(lista[j]):

                if lista[i] not in resultado:
                    resultado.append(lista[i])

                if lista[j] not in resultado:
                    resultado.append(lista[j])

    return resultado

if __name__ == "__main__":
    print(mismos_caracteres())


# Para este problema se creó una función en la cual el usuario ingresa la cantidad de palabras a evaluar.
# Posteriormente, mediante ciclos for, se comparan las palabras de la lista verificando si poseen los mismos
# caracteres, independientemente del orden. Cuando dos palabras coinciden, se guardan en una nueva lista evitando
# repetir elementos. Finalmente, la función retorna únicamente las palabras que cumplen dicha condición.


