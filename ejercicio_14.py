"""Cine: control de sala
Pedir la capacidad total de una sala de cine y luego registrar cuántas
personas ingresan.
Por cada persona pedir edad y clasificar:
 niño
 adulto
 adulto mayor
Al final mostrar:
 total de personas ingresadas
 cuántos niños
 cuántos adultos
 cuántos adultos mayores
 si la sala se llenó o no
Practica: ciclos con límite, contadores."""
# Pedimos al usuario la capacidad total de la sala de cine.
capacidad_sala = int(input("Ingrese la capacidad total de la sala de cine: "))
# Inicializamos contadores para cada categoría de edad y un contador total de personas.
contador_ninos = 0
contador_adultos = 0
contador_adultos_mayores = 0
contador_total_personas = 0
# Usamos un bucle para registrar la entrada de personas hasta que se alcance la capacidad de
# la sala.
while contador_total_personas < capacidad_sala:
    # Pedimos la edad de la persona que ingresa.
    edad = int(input("Ingrese la edad de la persona que ingresa: "))
    # Clasificamos a la persona según su edad y actualizamos los contadores correspondientes.
    if edad < 18:
        contador_ninos += 1
    elif 18 <= edad < 60:
        contador_adultos += 1
    else:
        contador_adultos_mayores += 1
    # Incrementamos el contador total de personas ingresadas.
    contador_total_personas += 1
    # Verificamos si la sala se ha llenado después de cada ingreso.
    if contador_total_personas == capacidad_sala:
        print("La sala se ha llenado. No se pueden ingresar más personas.")
        break
# Al finalizar el registro de personas, mostramos los resultados.
print(f"Total de personas ingresadas: {contador_total_personas}")
print(f"Cantidad de niños: {contador_ninos}")
print(f"Cantidad de adultos: {contador_adultos}")
print(f"Cantidad de adultos mayores: {contador_adultos_mayores}")