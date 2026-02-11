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
