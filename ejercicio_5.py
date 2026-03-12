"""Tienda de mascotas: alimento por tipo de animal
Pide el tipo de mascota:
 perro
 gato
 conejo
Luego muestra una recomendación de alimento según el animal.
Practica: comparaciones con texto."""

# Solicitar tipo de mascota al usuario
mascota = input("Ingrese el tipo de mascota (perro, gato, conejo): ").lower()
# Mostrar recomendación de alimento según el tipo de mascota
if mascota == "perro":
    print("Recomendación: Alimento para perros.")
elif mascota == "gato":
    print("Recomendación: Alimento para gatos.")
elif mascota == "conejo":
    print("Recomendación: Alimento para conejos.")
else:
    print("Tipo de mascota no válido. Por favor, ingrese un tipo de mascota válido.")