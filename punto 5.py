def same_characters(words: list[str]) -> list[str]:
    result = []

    for first_variable in range(len(words)):
        for second_variable in range(first_variable + 1, len(words)):
            if sorted(words[first_variable]) == sorted(words[second_variable]):

                if words[first_variable] not in result:
                    result.append(words[first_variable])

                if words[second_variable] not in result:
                    result.append(words[second_variable])

    return result


if __name__ == "__main__":
    quantity = int(input("Ingrese la cantidad de palabras que va a ingresar: "))
    words = []

    for index in range(quantity):
        word = input("Ingrese su palabra numero " + str(index + 1) + ": ")
        words.append(word)

    print("los elementos de su lista: " + str(words) + " que tienen las mismas letras son: "+ str(same_characters(words)))


# Para este problema se creó una función en la cual el usuario ingresa la cantidad de palabras a evaluar.
# Posteriormente, mediante ciclos for, se comparan las palabras de la lista verificando si poseen los mismos
# caracteres, independientemente del orden. Cuando dos palabras coinciden, se guardan en una nueva lista evitando
# repetir elementos. Finalmente, la función retorna únicamente las palabras que cumplen dicha condición.
