import os
suma = lambda a, b: a + b
resta = lambda a, b: a - b
multiplicacion = lambda a, b: a * b
division = lambda a, b: a / b if b != 0 else False
potencia = lambda a, b: a**b


def asignar():
    a = float(input("Numero 1: "))
    b = float(input("Numero 2: "))
    return a, b


def menu():
    opcion = 0

    while opcion != 6:
        print("***************")
        print("* CALCULADORA *")
        print("* 1. SUMA     *")
        print("* 2. RESTA    *")
        print("* 3. PRODUCTO *")
        print("* 4. COCIENTE *")
        print("* 5. POTENCIA *")
        print("* 6. SALIR    *")
        print("***************")
        opcion = int(input("Ingrese una opcion: "))

        if (opcion == 1):
            a, b = asignar()
            print(suma(a, b))
        elif (opcion == 2):
            a, b = asignar()
            print(resta(a, b))
        elif (opcion == 3):
            a, b = asignar()
            print(multiplicacion(a, b))
        elif (opcion == 4):
            a, b = asignar()
            print(division(a, b))
        elif (opcion == 5):
            a, b = asignar()
            print(division(a, b))
        elif (opcion == 6):
            return
        else:
            print("Opcion no valida")

        os.system("pause")
        os.system("cls")


menu()
print("Fin")