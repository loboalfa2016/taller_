"""Registrar varios pedidos en una cafetería hasta que el usuario escriba
“salir”.
Productos:
 café = 4000
 capuchino = 7000
 pastel = 6000
Reglas:
 si la compra supera 20000, aplicar 10% de descuento
 si no, cobrar normal
Mostrar total por cliente y al final total acumulado del día.
Practica: menú simple, ciclos, descuentos."""
# Precios de los productos
precio_cafe = 4000
precio_capuchino = 7000
precio_pastel = 6000
# Inicializamos el acumulador para el total del día.
total_dia = 0
# Entramos en un bucle infinito para registrar pedidos hasta que el usuario decida salir.
while True:
    # Pedimos al usuario el producto que desea comprar.
    producto = input('Ingrese el producto (café, capuchino, pastel) o "salir" para terminar: ')
    # Si el usuario quiere salir, rompemos el bucle.
    if producto.lower() == 'salir':
        break
    # Pedimos la cantidad de unidades que desea comprar.
    cantidad = int(input('Ingrese la cantidad de unidades: '))
    # Calculamos el total por cliente según el producto elegido.
    if producto.lower() == 'cafe':
        total_cliente = precio_cafe * cantidad
    elif producto.lower() == 'capuchino':
        total_cliente = precio_capuchino * cantidad
    elif producto.lower() == 'pastel':
        total_cliente = precio_pastel * cantidad
    else:
        print('Producto no válido. Intente nuevamente.')
        continue
    # Aplicamos descuento si el total del cliente supera los 20000 pesos.
    if total_cliente > 20000:
        total_cliente *= 0.9  # Aplica un descuento del 10%
    # Mostramos el total a pagar por el cliente.
    print(f"El total a pagar por este cliente es: {total_cliente} pesos.")
    # Acumulamos el total del día con el total del cliente actual.
    total_dia += total_cliente
# Al finalizar el registro de pedidos, mostramos el total acumulado del día.
print(f"El total acumulado del día es: {total_dia} pesos.")
print("Gracias por su compra. ¡Que tenga un buen día!")
print("¡Vuelva pronto a nuestra cafetería!")
print("¡Gracias por elegir nuestra cafetería! Esperamos verlo de nuevo pronto.")