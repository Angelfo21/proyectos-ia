import math

def calculadora_mejorada():
    while True:
        print("\n--- Calculadora Avanzada ---")
        print("1. Suma | 2. Resta | 3. Multiplicación | 4. División")
        print("5. Potencia | 6. Raíz Cuadrada | 7. Salir")
        
        opcion = input("Elige una operación (1-7): ")
        if opcion == '7':
            break
        
        if opcion in ['1', '2', '3', '4', '5']:
            try:
                n1 = float(input("Primer número: "))
                n2 = float(input("Segundo número: "))
                if opcion == '1': print(f"Resultado: {n1 + n2}")
                elif opcion == '2': print(f"Resultado: {n1 - n2}")
                elif opcion == '3': print(f"Resultado: {n1 * n2}")
                elif opcion == '4': print(f"Resultado: {n1 / n2}" if n2 != 0 else "Error: División por cero")
                elif opcion == '5': print(f"Resultado: {math.pow(n1, n2)}")
            except ValueError:
                print("Error: Ingresa valores numéricos válidos.")
        elif opcion == '6':
            try:
                n = float(input("Número: "))
                print(f"Resultado: {math.sqrt(n)}" if n >= 0 else "Error: Raíz negativa")
            except ValueError:
                print("Error: Ingresa un valor numérico válido.")
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    calculadora_mejorada()