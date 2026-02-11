
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
