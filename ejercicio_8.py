"""Tienda deportiva: contar productos caros
Pide el precio de 6 productos deportivos.
Al final indica cuántos cuestan más de 100000.
Practica: ciclo, contador, condicional."""

# Inicializar contador para productos caros
contador_caros = 0
# Solicitar precios de 6 productos al usuario
for i in range(6):
    precio = float(input(f'Ingrese el precio del producto {i + 1}: '))
    # Verificar si el producto cuesta más de 100000
    if precio > 100000:
        contador_caros += 1
# Mostrar el número de productos caros al usuario
print(f"El número de productos que cuestan más de 100000 es: {contador_caros}.")
print("Gracias por su visita.")
print("¡Que tenga un buen día!")
print("¡Vuelva pronto!")
print("¡Gracias por elegir nuestra tienda deportiva!")
print("¡Esperamos verlo de nuevo pronto!")