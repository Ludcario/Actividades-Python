# Calculadora mejorada en Python

def addmultiplenumbers(numbers):
    """
    Suma todos los números en una lista.
    Si la lista está vacía, devuelve 0.
    """
    return sum(numbers) if numbers else 0


def multiplymultiplenumbers(numbers):
    """
    Multiplica todos los números en una lista.
    Si la lista está vacía, devuelve 0 para indicar que no hay números.
    """
    if not numbers:
        return 0
    result = 1
    for num in numbers:
        result *= num
    return result


def isiteven(number):
    """
    Devuelve True si el número es par y entero (acepta floats equivalentes a enteros).
    Devuelve False en caso contrario.
    """
    if number % 1 == 0:  # Equivalente a number.is_integer()
        return int(number) % 2 == 0
    return False


def isitaninteger(number):
    """
    Devuelve True si el número es un entero (acepta floats equivalentes a enteros).
    """
    return number % 1 == 0


def main():
    """
    Función principal para la calculadora interactiva.
    """
    print("=== Bienvenido a una Mejor Calculadora  Version de Ludwig===")

    while True:
        print("\nOpciones:")
        print("1. Sumar varios números")
        print("2. Multiplicar varios números")
        print("3. Ver si un número es par")
        print("4. Ver si un número es entero")
        print("5. Salir")

        opcion = input("Elige una opción (1-5): ")

        if opcion == "1":
            numeros = list(map(float, input("Escribe los números separados por espacio: ").split()))
            print("Resultado de la suma:", addmultiplenumbers(numeros))

        elif opcion == "2":
            numeros = list(map(float, input("Escribe los números separados por espacio: ").split()))
            print("Resultado de la multiplicación:", multiplymultiplenumbers(numeros))

        elif opcion == "3":
            numero = float(input("Escribe el número: "))
            print(f"¿Es {numero} par?", isiteven(numero))

        elif opcion == "4":
            numero = float(input("Escribe el número: "))
            print(f"¿Es {numero} un entero?", isitaninteger(numero))

        elif opcion == "5":
            print("¡Gracias por usar la calculadora! Hasta luego.")
            break

        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")


# Este bloque asegura que main() solo se ejecute si este archivo es el principal
if __name__ == "__main__":
    main()
