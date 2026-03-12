"""entrada según edad
El precio de la entrada cambia así:
 niños menores de 12 → 8000
 adultos de 12 a 59 → 12000
 mayores de 60 → 9000
Pide la edad del cliente y muestra cuánto debe pagar.
Practica: condicionales."""

# Solicitar edad al usuario
age = int(input("Ingrese la edad del cliente: "))
# Determinar el precio de la entrada según la edad
if age < 12:
    precio = 8000
elif 12 <= age <= 59:
    precio = 12000
else:
    precio = 9000
# Mostrar el precio a pagar
print(f"El cliente debe pagar: {precio} pesos.")
print("Gracias por su compra.")
print("¡Disfrute su visita!")