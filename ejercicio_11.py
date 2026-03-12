"""Heladería: factura de varios clientes
Una heladería quiere registrar varios clientes hasta que el usuario
decida salir.
Productos:
 cono = 3000
 vaso = 4000
 banana split = 9000
Por cada cliente:
 pedir producto
 pedir cantidad
 calcular total
Al final mostrar:
 total vendido
 cuántos clientes se atendieron
 cuál producto se pidió más veces
Practica: ciclos, acumuladores, contadores."""

# Se inicializan contadores y acumuladores antes de empezar a procesar datos.
# `total_vendido` guardará la suma de todas las ventas en pesos.
# `contador_clientes` llevará la cuenta de cuántos clientes se atendieron.
# Los siguientes tres contadores guardarán cuántas unidades de cada producto se vendieron.
total_vendido = 0
contador_clientes = 0
contador_cono = 0
contador_vaso = 0
contador_banana_split = 0

# Entramos en un bucle infinito que solo se romperá cuando el usuario escriba "salir".
# Este ciclo representa la atención de clientes uno por uno.
while True:
    # Pedimos al usuario el tipo de producto que desea comprar.
    producto = input('ingrese el producto (cono, vaso, banana split) o "salir" para terminar: ')
    # Si el usuario quiere terminar, salimos del bucle.
    if producto.lower() == 'salir':
        break
    # Para cualquier otro valor, pedimos la cantidad de unidades.
    cantidad = int(input('ingrese la cantidad: '))
    # Según el producto elegido, calculamos el precio y actualizamos los contadores.
    if producto.lower() == 'cono':
        # Cada cono cuesta 3000 pesos.
        total_vendido += 3000 * cantidad
        contador_cono += cantidad
    elif producto.lower() == 'vaso':
        # Cada vaso cuesta 4000 pesos.
        total_vendido += 4000 * cantidad
        contador_vaso += cantidad
    elif producto.lower() == 'banana split':
        # Cada banana split cuesta 9000 pesos.
        total_vendido += 9000 * cantidad
        contador_banana_split += cantidad
    else:
        # Si el producto no es reconocido, avisamos y volvemos a preguntar.
        print('Producto no válido. Intente nuevamente.')
        continue
    # Contamos un cliente más atendido (solo si el producto fue válido).
    contador_clientes += 1

# Una vez terminado el registro de clientes, decidimos qué producto se pidió más veces.
if contador_cono > contador_vaso and contador_cono > contador_banana_split:
    producto_mas_pedido = 'cono'
elif contador_vaso > contador_cono and contador_vaso > contador_banana_split:
    producto_mas_pedido = 'vaso'
elif contador_banana_split > contador_cono and contador_banana_split > contador_vaso:
    producto_mas_pedido = 'banana split'
else:
    # Si hay empate entre dos o más productos, indicamos que no hay un claro ganador.
    producto_mas_pedido = 'ninguno, hay un empate'

# Finalmente mostramos el resumen de la jornada al usuario.
print(f"Total vendido: {total_vendido} pesos.")
print(f"Cantidad de clientes atendidos: {contador_clientes}.")
print(f"Producto más pedido: {producto_mas_pedido}.")
print("Gracias por su participación.")
print("¡Que tenga un buen día!")
print("¡Vuelva pronto!")
print("¡Gracias por elegir nuestra heladería!")
print("¡Esperamos verlo de nuevo pronto!")