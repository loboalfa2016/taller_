"""Una heladería quiere registrar 5 pedidos.
Por cada cliente, el programa debe pedir el sabor elegido:
 vainilla
 chocolate
 fresa
Al final debe mostrar cuántas veces se pidió cada sabor.
Practica: ciclos, condicionales, contadores."""

# Inicializar contadores
contador_vainilla = 0
contador_chocolate = 0
contador_fresa = 0

# Registrar pedidos
for i in range(5):
    sabor = input("ingrese el sabor elegido (vainilla, chocolate, fresa): ").lower()
    if sabor == "valnilla":
        contador_vainilla += 1
    elif sabor == "chocolate":
        contador_chocolate += 1
    elif sabor == "fresa":
        contador_fresa += 1
    else:
        print("Sabor no válido. Por favor, ingrese un sabor válido.")

# Mostrar resultados
print(f"Cantidad de pedidos de vainilla: {contador_vainilla}")
print(f"Cantidad de pedidos de chocolate: {contador_chocolate}")
print(f"Cantidad de pedidos de fresa: {contador_fresa}")
