## Reto n° 1
### Nombre: Brayan Santiago Rincón Rodríguez
### Curso: Programación orientada a objetos

### 1. Crear una función que realice operaciones básicas (suma, resta, multiplicación, división) entre dos números, según la elección del usuario, la forma de entrada de la función será los dos operandos y el caracter usado para la operación. entrada: (1,2,"+"), salida (3)

 ``` python 
 
def result(operation: str, first_number: int, second_number: int) -> float:
    if operation == "+":
        return first_number + second_number

    elif operation == "-":
        return first_number - second_number

    elif operation == "*":
        return first_number * second_number

    elif operation == "/":
        while second_number == 0:
            print("No se puede dividir por 0 ingrese un nuevo valor para el denominador")
            second_number = int(input("Ingrese el segundo número: "))
        return first_number / second_number


if __name__ == "__main__":
    operation = input("Ingrese el signo de la operación deseada(+,-,*,/): ")
    first_number = int(input("Ingrese el primer número: "))
    second_number = int(input("Ingrese el segundo número: "))
    print(result(operation, first_number, second_number))


# Para llegar a la solución plantié una función que recibiera como entradas
# el signo de la operación y los dos números ingresados por el usuario. Luego,
# mediante estructuras condicionales se evalúa cuál operación debe realizarse,
# retornando el resultado correspondiente.En el caso de la división se evalua
# que el denominador sea distinto de cero para evitar errores, de lo contrario 
# si el número b es 0, se entrará en un bucle while hasta que b sea distinto de 0.

 ```

### 2. Realice una función que permita validar si una palabra es un palíndromo. Condición: No se vale hacer slicing para invertir la palabra y verificar que sea igual a la original.

``` python

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

```

### 3. Escribir una función que reciba una lista de números y devuelva solo aquellos que son primos. La función debe recibir una lista de enteros y retornar solo aquellos que sean primos.

``` python

def prime_numbers(numbers: list[int]) -> list[int]:
    prime_list = []

    for number in numbers:
        prime = True

        for counter in range(2, number):
            if number % counter == 0:
                prime = False
                break

        if number > 1 and prime:
            prime_list.append(number)

    return prime_list


if __name__ == "__main__":
    quantity = int(input("Cuántos números desea evaluar: "))
    numbers = []

    for i in range(quantity):
        value = int(input("Ingrese el numero " + str(i + 1) + " de su lista: "))
        numbers.append(value)

    print("los números primos de su lista: " + str(numbers) + " son: " + str(prime_numbers(numbers)))


# Para este problema se creó una función en donde el usuario puede poner la cantidad de números que desee en la lista.
# Mediante un for se recorre cada número de la lista y se inicializa una bandera con valor True. Posteriormente, se evalua si el módulo
# (residuo) es igual a 0, respecto a 2, y así sucesivamente hasta que el contador se actualice progresivamente al número - 1
# Si el módulo es 0 en algún momento, el número no será primo por lo que la bandera se actualizará. Finalmente, los números primos
# se guardarán en una nueva lista.

```

### 4. Escribir una función que reciba una lista de números enteros y retorne la mayor suma entre dos elementos consecutivos.

``` python

def addition(numbers: list[int]) -> int:
    sum_list = []

    for index in range(len(numbers) - 1):
        addition = numbers[index] + numbers[index + 1]
        sum_list.append(addition)

    return max(sum_list)


if __name__ == "__main__":
    quantity = int(input("Cuántos números desea evaluar: "))
    numbers = []

    for i in range(quantity):
        value = int(input("Ingrese el numero " + str(i + 1) + " de su lista: "))
        numbers.append(value)

    print("La mayor suma de dos números de la lista " + str(numbers) + " es: " + str(addition(numbers)))


# Se hizo un programa con una función donde el usuario ingreso la cantidad de números a ser evaluados en una lista.
# Para luego, mediante un ciclo for, sumar el primer elemento de la lista con el siguiente elemento, guardando el resultado 
# en otra lista. Se le aclaró al programa que el último elemento señalado será el penúltimo para no caer en un error.
# Para finalizar, mediante la función max(), se identificó cuál era la suma mayor.

```
### 5. Escribir una función que reciba una lista de string y retorne unicamente aquellos elementos que tengan los mismos caracteres. e.g. entrada: ["amor", "roma", "perro"], salida ["amor", "roma"]

``` python

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

```
### Nombre: Brayan Santiago Rincón Rodríguez
### Curso: Programación orientada a objetos
