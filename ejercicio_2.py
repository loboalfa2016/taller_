""" Gimnasio: acceso por edad
Un gimnasio ofrece clases según la edad:
 menor de 13 → no puede ingresar
 de 13 a 17 → clase juvenil
 de 18 a 59 → clase general
 60 o más → clase senior
Pide la edad de una persona y muestra a qué grupo pertenece.
Practica: if, elif, else."""

# Solicitar edad al usuario
age = int(input("Ingrese la edad de la persona: "))
# Determinar el grupo de clase según la edad
if age < 13:
    print("No puede ingresar al gimnasio.")
elif 13 <= age <= 17:
    print("Pertenece a la clase juvenil.")
elif 18 <= age <= 59:
    print("Pertenece a la clase general.")
else:
    print("Pertenece a la clase senior.")