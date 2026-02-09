def verificar_palindromo():
    palabra = input("Ingrese su palabra: ")
    contador = (len(palabra)-1)
    guardar = []
    palindromo: bool = True

    for indice in palabra:
        guardar.append(indice)

    for i in range(len(guardar)):
        if guardar[i] != guardar[contador]:
            palindromo = False
            break
        contador = contador - 1

    if palindromo == True:
        print("La palabra "+ str(palabra)+ " es palíndromo")

    else:
        print("La palabra "+ str(palabra)+ " no es palíndromo")


if __name__ == "__main__":
    verificar_palindromo()


# Para la solución al problema 2, se creó una función en donde primero se separan las letras de la palabra ingresada.
# Posteriormente, se evalúa si la primera letra es diferente a la última letra de la palabra, de ser así, la variable 
# booleana quedará como falsa. De lo contario se le resta uno al contador para que ahora se evalue la segunda letra junto
# con la penúltima y así sucesivamente.
