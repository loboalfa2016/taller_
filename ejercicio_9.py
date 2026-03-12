"""Spa: servicio disponible
En un spa hay estos servicios:
 masaje
 facial
 manicure
Pide al usuario qué servicio desea y muestra un mensaje confirmando
si existe o no.
Practica: condicionales con texto."""
# Solicitar servicio al usuario
servicio = input('  Ingrese el servicio que desea (masaje, facial, manicure): ').lower()
# Verificar si el servicio existe y mostrar mensaje de confirmación
if servicio == "masaje":
    print("Servicio de masaje disponible. ¡Disfrute su experiencia!")
elif servicio == "facial":
    print("Servicio de facial disponible. ¡Disfrute su experiencia!")
elif servicio == "manicure":
    print("Servicio de manicure disponible. ¡Disfrute su experiencia!")
else:
    print("Servicio no disponible. Por favor, elija un servicio válido.")
print("Gracias por su visita.")
print("¡Que tenga un buen día!")
print("¡Vuelva pronto!")
print("¡Gracias por elegir nuestro spa!")
print("¡Esperamos verlo de nuevo pronto!")
print("¡Disfrute de su día en nuestro spa!")
