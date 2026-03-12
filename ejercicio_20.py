"""Club recreativo: control de membresías
Registrar varias personas en un club.
Por cada una pedir:
 nombre
 edad
 tipo de plan: básico, premium, familiar
Reglas:
 básico = 50000
 premium = 90000
 familiar = 130000
Además:
 si la persona es menor de 18, mostrar “registro juvenil”
 si tiene 60 o más, mostrar “beneficio senior”
Al final mostrar:
 total recaudado
 cantidad de personas por plan
 plan más vendido
Practica: condicionales, contadores, acumuladores."""
# Inicializamos los contadores y acumuladores necesarios para el registro de membresías.
total_recaudado = 0
contador_basico = 0
contador_premium = 0
contador_familiar = 0
# Usamos un bucle para registrar a varias personas. En este caso, se registrarán 10 personas, pero se puede ajustar según sea necesario.
for i in range(10): 
    # Solicitamos el nombre, edad y tipo de plan de la persona.
    nombre = input('Ingrese el nombre de la persona: ')
    edad = int(input('Ingrese la edad de la persona: '))
    tipo_plan = input('Ingrese el tipo de plan (básico, premium, familiar): ')
    # Verificamos el tipo de plan y actualizamos los contadores y acumuladores según corresponda.
    if tipo_plan.lower() == 'básico':
        total_recaudado += 50000
        contador_basico += 1
    elif tipo_plan.lower() == 'premium':
        total_recaudado += 90000
        contador_premium += 1
    elif tipo_plan.lower() == 'familiar':
        total_recaudado += 130000
        contador_familiar += 1
    else:
        print('Tipo de plan no válido. Intente nuevamente.')
        continue
    # Verificamos si la persona es menor de 18 años o tiene 60 o más años para mostrar los mensajes correspondientes.
    if edad < 18:
        print('Registro juvenil')
    elif edad >= 60:
        print('Beneficio senior')
# Al finalizar el registro de las personas, mostramos los resultados.
print(f"Total recaudado: {total_recaudado} pesos.")
print(f"Cantidad de personas con plan básico: {contador_basico}")
print(f"Cantidad de personas con plan premium: {contador_premium}")
print(f"Cantidad de personas con plan familiar: {contador_familiar}")
# Determinamos cuál plan fue el más vendido.
if contador_basico > contador_premium and contador_basico > contador_familiar:
    plan_mas_vendido = 'básico'
elif contador_premium > contador_basico and contador_premium > contador_familiar:
    plan_mas_vendido = 'premium'
elif contador_familiar > contador_basico and contador_familiar > contador_premium:
    plan_mas_vendido = 'familiar'
else:
    plan_mas_vendido = 'empate entre planes'
# Mostramos cuál plan fue el más vendido.
print(f"El plan más vendido es: {plan_mas_vendido}.")
