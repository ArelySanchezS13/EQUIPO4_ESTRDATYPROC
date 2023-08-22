""" canciones = {
    10: "Otra noche en Miami",
    20: "La Santa",
    30: "Agosto",
    40: "Nataoki",
    50: "Cuento"
}
print(len(canciones))
print(canciones.keys())
print(canciones.values()) """

# Ejemplo de diccionario

contactos = {}

while True:
    nombre = input("Ingresa el nombre: ")

    if nombre.strip() == "":
        break

    telefono = input("Ingresa el telefono: ")

    nueva_clave = max(contactos.keys(), default=0) + 1
    contactos[nueva_clave]=(nombre, telefono)

print(contactos)