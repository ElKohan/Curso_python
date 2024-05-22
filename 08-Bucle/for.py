""""
for variable in elemento iterable (lista, rango, etc)
"""


contador = 0
resultado = 0

for contador in range(0, 10):
    print(f"Voy por el "+ str(contador))

    resultado = resultado + contador
    #resultado += contador es lo mismo 

print(f"El resultado de todo el ciclo for es: {resultado}")


print(".-.-.-.-.-.-.-.-.-.-.--.-EJEMPLO.-.-.-.-.-.-.-.-.-.")

numero_usuario = int(input("De que numero quieres la tabla?: "))

if numero_usuario < 1:
   

  print(f"#### Tabla de multiplicar del numero {numero_usuario} ####")

for numero_tabla in range(0, 11):
    if numero_usuario == 45:
        print("No se pueden mostrar numeros prohibidos")
        break

    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")

else:
    print("Tabla finalizada.")