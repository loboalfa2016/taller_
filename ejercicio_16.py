"""Tienda de mascotas: ventas por categoría
Registrar ventas de una tienda de mascotas.
Categorías:
 alimento
 juguete
 accesorio
Pedir 10 ventas. En cada venta:
 categoría
 valor de la compra
Al final mostrar:
 cuánto se vendió por cada categoría
 cuál categoría generó más dinero
Practica: acumuladores separados."""
# Inicializamos los acumuladores para cada categoría de venta.
total_alimento = 0
total_juguete = 0
total_accesorio = 0
# Usamos un bucle para registrar 10 ventas.
for i in range(10):
    # Solicitamos la categoría de la venta y el valor de la compra.
    categoria = input('Ingrese la categoría de la venta (alimento, juguete, accesorio): ')
    valor_compra = float(input('Ingrese el valor de la compra: '))
    # Acumulamos el total vendido por cada categoría según la entrada del usuario.
    if categoria.lower() == 'alimento':
        total_alimento += valor_compra
    elif categoria.lower() == 'juguete':
        total_juguete += valor_compra
    elif categoria.lower() == 'accesorio':
        total_accesorio += valor_compra
    else:
        print('Categoría no válida. Intente nuevamente.')
# Al finalizar el registro de las ventas, mostramos cuánto se vendió por cada categoría.
print(f"Total vendido en alimento: {total_alimento} pesos.")
print(f"Total vendido en juguete: {total_juguete} pesos.")
print(f"Total vendido en accesorio: {total_accesorio} pesos.")
# Determinamos cuál categoría generó más dinero.
if total_alimento > total_juguete and total_alimento > total_accesorio:
    categoria_mayor_venta = 'alimento'
elif total_juguete > total_alimento and total_juguete > total_accesorio:
    categoria_mayor_venta = 'juguete'
elif total_accesorio > total_alimento and total_accesorio > total_juguete:
    categoria_mayor_venta = 'accesorio'
else:
    categoria_mayor_venta = 'empate entre categorías'
# Mostramos cuál categoría generó más dinero.
print(f"La categoría que generó más dinero es: {categoria_mayor_venta}.")

