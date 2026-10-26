def calculadora():
    print("Operaciones: 1.Suma 2.Resta 3.Multiplicación 4.División")
    opcion = input("Elige una opción (1/2/3/4): ")
    num1 = float(input("Primer número: "))
    num2 = float(input("Segundo número: "))

    if opcion == '1':
        print(f"Resultado: {num1 + num2}")
    elif opcion == '2':
        print(f"Resultado: {num1 - num2}")
    elif opcion == '3':
        print(f"Resultado: {num1 * num2}")
    elif opcion == '4':
        print(f"Resultado: {num1 / num2}" if num2 != 0 else "Error: División por cero")
    else:
        print("Opción no válida")

calculadora()