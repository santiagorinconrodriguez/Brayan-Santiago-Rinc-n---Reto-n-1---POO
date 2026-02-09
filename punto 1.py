
operacion = input("Ingrese el signo de la operación deseada(+,-,*,/): ")
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))


def resultado (operacion, a,b):
    if operacion == "+":
        return (a+b)
    
    elif operacion == "-":
        return (a-b)

    elif operacion == "*":
        return (a*b)
    
    elif operacion == "/":
        while b == 0:
            print("No se puede dividir por 0 ingrese un nuevo valor para el denominador")
            b = int(input("Ingrese el segundo número: "))
        return (a/b)

if __name__ == "__main__":
    print(resultado (operacion, a,b))

# Para llegar a la solución plantié una función que recibiera como entradas
# el signo de la operación y los dos números ingresados por el usuario. Luego,
# mediante estructuras condicionales se evalúa cuál operación debe realizarse,
# retornando el resultado correspondiente.En el caso de la división se evalua
# que el denominador sea distinto de cero para evitar errores, de lo contrario 
# si el número b es 0, se entrará en un bucle while hasta que b sea distinto de 0.
