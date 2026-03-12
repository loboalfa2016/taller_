"""Tienda de ropa deportiva: inventario crítico
Registrar 10 productos.
Por cada producto pedir:
 nombre
 cantidad disponible
Clasificar:
 0 → agotado
 1 a 5 → stock bajo
 6 o más → stock normal
Al final mostrar:
 cuántos están agotados
 cuántos tienen stock bajo
 cuántos están normales
Practica: clasificación por rangos, ciclo."""
# Inicializamos los contadores para cada categoría de stock.
contador_agotados = 0
contador_stock_bajo = 0
contador_stock_normal = 0
# Usamos un bucle para registrar 10 productos.
for i in range(10):
    # Solicitamos el nombre del producto (aunque no se usará para la clasificación).
    nombre_producto = input('Ingrese el nombre del producto: ')
    # Solicitamos la cantidad disponible del producto.
    cantidad_disponible = int(input('Ingrese la cantidad disponible: '))
    # Clasificamos el stock según la cantidad disponible.
    if cantidad_disponible == 0:
        contador_agotados += 1
    elif 1 <= cantidad_disponible <= 5:
        contador_stock_bajo += 1
    else:
        contador_stock_normal += 1
# Al finalizar el registro de los productos, mostramos cuántos están agotados, tienen stock bajo y están normales.
print(f"Productos agotados: {contador_agotados}")
print(f"Productos con stock bajo: {contador_stock_bajo}")
print(f"Productos con stock normal: {contador_stock_normal}")   
