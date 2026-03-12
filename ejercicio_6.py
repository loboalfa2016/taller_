''' Parqueadero: cobro por horas
Pide cuántas horas estuvo un carro en un parqueadero.
Reglas:
 primera hora = 5000
 cada hora adicional = 3000
Muestra el total a pagar.
Practica: condicionales y operaciones.'''

# Solicitar horas al usuario
horas = int(input('Ingrese el número de horas que estuvo el carro en el parqueadero: '))
# Calcular el total a pagar según las horas ingresadas
if horas <= 1:
    total = 5000
else:
    total = 5000 + (horas - 1) * 3000
# Mostrar el total a pagar
print(f"El total a pagar por {horas} horas en el parqueadero es: {total} pesos.")
print("Gracias por su visita.")
print("¡Que tenga un buen día!")
print("¡Vuelva pronto!")
print("¡Gracias por elegir nuestro parqueadero!")