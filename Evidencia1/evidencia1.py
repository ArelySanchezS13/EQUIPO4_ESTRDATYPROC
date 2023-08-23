edad = int(input("Ingrese su edad: ")) # En esta línea se le pide al usuario que ingrese su nombre

if edad >= 18:  # Condición para validar si la edad es 18 o mayor 
    print("Eres mayor de edad")

elif edad < 0:  # Condición para validar si la edad ingresada es válida, que sea mayor que 0
    print("Edad no válida, ingresar una edad correcta")

elif edad < 18:                  # Condición para verificar si la edad es menor que 18,
    print("Eres menor de edad")  # si se cumple esta condición aparecerá el texto que es menor de edad