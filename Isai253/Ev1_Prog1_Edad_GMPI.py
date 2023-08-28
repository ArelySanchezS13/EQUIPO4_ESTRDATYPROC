# A partir de una edad solicitada, decir si es mayor o menor de edad


edad = int(input("Introduce tu edad: "))
if edad < 0:
    print("Error: edad no aceptada.")
elif edad >= 18:
    print("Es mayor de edad.")
else:
    print('Es menor de edad.')