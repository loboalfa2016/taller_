""" Peluquería: agenda de atención
Una peluquería atiende 7 clientes al día.
Por cada cliente pedir:
 nombre
 servicio solicitado: corte, cepillado, tintura
 valor pagado
Al final mostrar:
 total del día
 cantidad de clientes por servicio
 servicio más solicitado
Practica: contadores, acumuladores, comparaciones."""
# Inicializamos los contadores y acumuladores necesarios para el registro de clientes.
total_dia = 0
contador_corte = 0
contador_cepillado = 0
contador_tintura = 0
# Usamos un bucle para registrar a 7 clientes.
for i in range(7):
    # Solicitamos el nombre del cliente (aunque no se usará para la clasificación).
    nombre = input('Ingrese el nombre del cliente: ')
    # Solicitamos el servicio solicitado y el valor pagado.
    servicio = input('Ingrese el servicio solicitado (corte, cepillado, tintura): ')
    valor_pagado = float(input('Ingrese el valor pagado: '))
    # Acumulamos el total del día con el valor pagado por el cliente actual.
    total_dia += valor_pagado
    # Contamos la cantidad de clientes por cada servicio según la entrada del usuario.
    if servicio.lower() == 'corte':
        contador_corte += 1
    elif servicio.lower() == 'cepillado':
        contador_cepillado += 1
    elif servicio.lower() == 'tintura':
        contador_tintura += 1
    else:
        print('Servicio no válido. Intente nuevamente.')
# Al finalizar el registro de los clientes, mostramos el total del día y la cantidad de clientes
# por servicio.
print(f"Total del día: {total_dia} pesos.")
print(f"Cantidad de clientes por corte: {contador_corte}")
print(f"Cantidad de clientes por cepillado: {contador_cepillado}")
print(f"Cantidad de clientes por tintura: {contador_tintura}")
# Determinamos cuál servicio fue el más solicitado.
if contador_corte > contador_cepillado and contador_corte > contador_tintura:
    servicio_mas_solicitado = 'corte'
elif contador_cepillado > contador_corte and contador_cepillado > contador_tintura:
    servicio_mas_solicitado = 'cepillado'
elif contador_tintura > contador_corte and contador_tintura > contador_cepillado:
    servicio_mas_solicitado = 'tintura'
else:
    servicio_mas_solicitado = 'empate entre servicios'
# Mostramos cuál servicio fue el más solicitado.
print(f"El servicio más solicitado es: {servicio_mas_solicitado}.") 