"""Centro de idiomas: evaluación de estudiantes
Registrar varios estudiantes de un curso de inglés.
Por cada uno pedir:
 nombre
 nota speaking
 nota listening
 nota reading
Calcular promedio simple y clasificar:
 menor de 60 → bajo
 60 a 79 → medio
 80 o más → alto
Al final mostrar:
 promedio general del grupo
 mejor estudiante
 cuántos quedaron en cada nivel
Practica: promedios, máximos, contadores."""

# Inicializamos los contadores y acumuladores necesarios para el registro de estudiantes.
total_estudiantes = 0
suma_promedios = 0
contador_bajo = 0
contador_medio = 0
contador_alto = 0
mejor_estudiante = ""
mejor_promedio = 0
# Usamos un bucle para registrar a los estudiantes. El bucle se detendrá cuando el usuario decida no ingresar más estudiantes.
while True:
    # Solicitamos el nombre del estudiante.
    nombre = input('Ingrese el nombre del estudiante: ')
    # Solicitamos las notas de speaking, listening y reading.
    nota_speaking = float(input('Ingrese la nota de speaking: '))
    nota_listening = float(input('Ingrese la nota de listening: '))
    nota_reading = float(input('Ingrese la nota de reading: '))
    # Calculamos el promedio simple de las tres notas.
    promedio = (nota_speaking + nota_listening + nota_reading) / 3
    # Acumulamos el total de promedios para calcular el promedio general del grupo más adelante.
    suma_promedios += promedio
    total_estudiantes += 1
    # Clasificamos al estudiante según su promedio y actualizamos los contadores correspondientes.
    if promedio < 60:
        contador_bajo += 1
    elif 60 <= promedio < 80:
        contador_medio += 1
    else:
        contador_alto += 1
    # Verificamos si este estudiante tiene el mejor promedio registrado hasta ahora.
    if promedio > mejor_promedio:
        mejor_promedio = promedio
        mejor_estudiante = nombre
    # Preguntamos al usuario si desea ingresar otro estudiante.
    continuar = input('¿Desea ingresar otro estudiante? (s/n): ')
    if continuar.lower() != 's':
        break
# Al finalizar el registro de los estudiantes, calculamos el promedio general del grupo y mostramos los resultados.
promedio_general = suma_promedios / total_estudiantes if total_estudiantes > 0 else 0
print(f"Promedio general del grupo: {promedio_general:.2f}")
print(f"Mejor estudiante: {mejor_estudiante} con un promedio de {mejor_promedio:.2f}")
print(f"Cantidad de estudiantes con nivel bajo: {contador_bajo}")
print(f"Cantidad de estudiantes con nivel medio: {contador_medio}")
print(f"Cantidad de estudiantes con nivel alto: {contador_alto}")