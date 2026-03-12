"""Parqueadero: control de vehículos
Registrar 8 vehículos en un parqueadero.
Por cada uno pedir:
 placa
 tipo: carro o moto
 horas parqueado
Tarifas:
 carro: 4000 por hora
 moto: 2000 por hora
Al final mostrar:
 total recaudado
 cuántos carros ingresaron
 cuántas motos ingresaron
 cuál vehículo pagó más
Practica: ciclos, máximos, acumuladores."""
# Inicializamos los contadores y acumuladores necesarios para el registro de vehículos.
total_recaudado = 0
contador_carros = 0
contador_motos = 0
max_pago = 0
vehiculo_mayor_pago = ""
# Usamos un bucle para registrar 8 vehículos.
for i in range(8):
    # Solicitamos la placa del vehículo.
    placa = input('Ingrese la placa del vehículo: ')
    # Solicitamos el tipo de vehículo (carro o moto).
    tipo = input('Ingrese el tipo de vehículo (carro o moto): ')
    # Solicitamos las horas que el vehículo estuvo parqueado.
    horas_parqueado = int(input('Ingrese las horas parqueado: '))
    # Calculamos el pago según el tipo de vehículo y actualizamos los contadores y acumuladores.
    if tipo.lower() == 'carro':
        pago = 4000 * horas_parqueado
        contador_carros += 1
    elif tipo.lower() == 'moto':
        pago = 2000 * horas_parqueado
        contador_motos += 1
    else:
        print('Tipo de vehículo no válido. Intente nuevamente.')
        continue
    # Acumulamos el total recaudado con el pago del vehículo actual.
    total_recaudado += pago
    # Verificamos si este vehículo pagó más que el máximo registrado hasta ahora.
    if pago > max_pago:
        max_pago = pago
        vehiculo_mayor_pago = placa
# Al finalizar el registro de los vehículos, mostramos los resultados.
print(f"Total recaudado: {total_recaudado} pesos.")
print(f"Cantidad de carros ingresados: {contador_carros}")
print(f"Cantidad de motos ingresadas: {contador_motos}")
print(f"El vehículo que pagó más es: {vehiculo_mayor_pago} con un pago de {max_pago} pesos.")