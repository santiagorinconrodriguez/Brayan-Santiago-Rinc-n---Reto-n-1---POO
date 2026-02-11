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


