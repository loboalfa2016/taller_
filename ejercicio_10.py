""" Academia de baile: asistencia
Pide la cantidad de clases asistidas por un estudiante en un mes.
Reglas:
 menos de 5 → asistencia baja
 entre 5 y 8 → asistencia media
 9 o más → asistencia alta
Practica: clasificación por rangos."""

# Solicitar la cantidad de clases asistidas al usuario
clases_asistidas = int(input('Ingrese la cantidad de clases asistidas por el estudiante en un mes: '))
# Clasificar la asistencia según las reglas establecidas
if clases_asistidas < 5:
    asistencia = "baja"
elif 5 <= clases_asistidas <= 8:
    asistencia = "media"
else:
    asistencia = "alta"
# Mostrar la clasificación de asistencia al usuario
print(f"La asistencia del estudiante es: {asistencia}.")
print("Gracias por su participación.")
print("¡Que tenga un buen día!")
print("¡Vuelva pronto!")
print("¡Gracias por elegir nuestra academia de baile!")
print("¡Esperamos verlo de nuevo pronto!")