def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero."
    return a / b

print("Calculadora básica")
print("Operaciones disponibles:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

# Entrada de datos
opcion = input("Elige una operación (1/2/3/4): ")
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Lógica de operaciones
if opcion == '1':
    resultado = suma(num1, num2)
    operacion = "+"
elif opcion == '2':
    resultado = resta(num1, num2)
    operacion = "-"
elif opcion == '3':
    resultado = multiplicacion(num1, num2)
    operacion = "*"
elif opcion == '4':
    resultado = division(num1, num2)
    operacion = "/"
else:
    resultado = "Opción no válida."
    operacion = "?"

# Mostrar resultado
print(f"Resultado: {num1} {operacion} {num2} = {resultado}")
