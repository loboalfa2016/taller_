"""Cafetería: total de una compra sencilla
En una cafetería venden:
 café = 4000
 té = 3500
 jugo = 5000
Pide al usuario qué bebida quiere y cuántas unidades desea comprar.
Luego muestra el total a pagar.
Practica: condicionales, variables, multiplicación."""

# Precios de las bebidas
precio_cafe = 4000
precio_te = 3500
precio_jugo = 5000

# Solicitar bebida y cantidad al usuario
bebida = str(input("Ingrese la bebida que desea comprar (café, té, jugo): ")).lower()
cantidad = int(input("Ingrese la cantidad de unidades que desea comprar: "))
# Calcular el total a pagar según la bebida seleccionada
if bebida == 'cafe':
    total = precio_cafe * cantidad
elif bebida == 'te':
    total = precio_te * cantidad
elif bebida == 'jugo':
    total = precio_jugo * cantidad
else:
    total = 0
    print("Bebida no válida. Por favor, ingrese una bebida válida.")
# Mostrar el total a pagar
if total > 0:
    print(f"El total a pagar por {cantidad} unidades de {bebida} es: {total} pesos.")   
