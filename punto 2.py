def check_palindrome(word: str) -> bool:
    counter = len(word) - 1
    letters = []
    palindrome: bool = True

    for index in word:
        letters.append(index)

    for i in range(len(letters)):
        if letters[i] != letters[counter]:
            palindrome = False
            break
        counter = counter - 1

    return palindrome


if __name__ == "__main__":
    word = input("Ingrese su palabra: ")

    if check_palindrome(word):
        print("La palabra " + str(word) + " es palíndromo")
    else:
        print("La palabra " + str(word) + " no es palíndromo")


# Para la solución al problema 2, se creó una función en donde primero se separan las letras de la palabra ingresada.
# Posteriormente, se evalúa si la primera letra es diferente a la última letra de la palabra, de ser así, la variable
# booleana quedará como falsa. De lo contario se le resta uno al contador para que ahora se evalue la segunda letra junto
# con la penúltima y así sucesivamente.
