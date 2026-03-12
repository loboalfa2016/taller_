"""Registrar 5 personas en un gimnasio.
Por cada una pedir:
 nombre
 días asistidos en la semana
 minutos promedio entrenados por día
Clasificar:
 menos de 3 días → bajo compromiso
 3 a 4 días → compromiso medio
 5 o más → compromiso alto
Al final mostrar cuántas personas quedaron en cada categoría.
Practica: ciclos, contadores, condicionales."""
# Inicializamos los contadores para cada categoría de compromiso.
compromiso_bajo = 0
compromiso_medio = 0
compromiso_alto = 0
# Usamos un bucle para registrar a 5 personas.
for i in range(5):
    # Solicitamos el nombre de la persona (aunque no se usará para la clasificación).
    nombre = input('Ingrese el nombre de la persona: ')
    # Solicitamos los días asistidos a la semana y los minutos promedio entrenados por día.
    dias_asistidos = int(input('Ingrese los días asistidos en la semana: '))
    minutos_entrenados = int(input('Ingrese los minutos promedio entrenados por día: '))
    # Clasificamos el compromiso según los días asistidos.
    if dias_asistidos < 3:
        compromiso_bajo += 1
    elif 3 <= dias_asistidos <= 4:
        compromiso_medio += 1
    else:
        compromiso_alto += 1
# Al finalizar el registro de las 5 personas, mostramos cuántas quedaron en cada categoría
print(f"Personas con compromiso bajo: {compromiso_bajo}")
print(f"Personas con compromiso medio: {compromiso_medio}")
print(f"Personas con compromiso alto: {compromiso_alto}")