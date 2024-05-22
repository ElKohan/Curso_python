#Bucle while 

# while condicion:
#   Bloque de instrucciones
#   Actuslizacion de contador

contador = 1

while contador <= 100:
    print(f"Estoy en el numero: {contador}")
    contador += 1
    #contador = contador + 1


print("--------------------------------------------------------------------")
contador = 1
muestrame = str(0)

while contador <= 100:
    muestrame = muestrame + ", " + str(contador)
    contador += 1

print(muestrame)


print("------------------------------------------------------------------")

numero_usuario = int(input("De que numero quieres la tabla?: "))


    
print(f"### Tabla del {numero_usuario} ####")

contador = 1 
while contador <= 10:
    print(f"{numero_usuario} x {contador} = {numero_usuario*contador}")
    contador += 1

else: 
    print("Aqui termina la tabla.")