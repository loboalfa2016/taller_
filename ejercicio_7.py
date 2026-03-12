"""Peluquería: turno del día
Pide la hora de llegada de un cliente en formato entero de 0 a 23.
Mostrar:
 mañana si está entre 6 y 11
 tarde si está entre 12 y 17
 noche si está entre 18 y 22
 fuera de horario en cualquier otro caso
Practica: rangos con condicionales."""

# Solicitar la hora de llegada al usuario
hora = int(input('Ingrese la hora de llegada del cliente (0-23): '))
# Determinar el turno del día según la hora ingresada
if 6 <= hora <= 11:
    turno = "mañana"
elif 12 <= hora <= 17:
    turno = "tarde"
elif 18 <= hora <= 22:
    turno = "noche"
else:
    turno = "fuera de horario"
# Mostrar el turno del día al usuario
print(f"El turno del día para la hora {hora} es: {turno}.")
print("Gracias por su visita.")
print("¡Que tenga un buen día!")
print("¡Vuelva pronto!")
print("¡Gracias por elegir nuestra peluquería!")