def calcular_edad_futura(nombre, edad):

    edad_futura = edad + 10

    print("Hola", nombre + ", en 10 años tendrás", edad_futura, "años.")

 

# Entrada del usuario

nombre_usuario = input("¿Cuál es tu nombre? ")

edad_usuario = int(input("¿Qué edad tienes? "))

 

# Llamada a la función

calcular_edad_futura(nombre_usuario, edad_usuario)