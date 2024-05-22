#Condicional if
print("################## EJEMPLO 1 ###############")

#color = "verde"
color = input("¿CUAL ES MI COLOR FAVORITO? ")

if color == "rojo":
    print("El color es Rojo")
else:
    print("El color NO es rojo ")

#operadores de comparacion
# == igual
# 

print("Nuevooo")


print("########### EJEMPLO 2################")

#Operadores de comparacion

#year = 2020
year = int(input("En que año estamos??"))

if year >= 2021:
    print("Estamos de 2021 en adelante!!!")

else:
    print("Es un año anterior a 2021")


print("########## EJEMPLO 3 ###################")

nombre = "Arturo Vidal"
ciudad = "Barcelona"
continente = "Europa"
edad = 55
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad !!")
    if continente != "Europa":
        print("El usuario no es Europeo")
    else: 
        print(f"Es europeo y de {ciudad}")
    

else:
    print(f"{nombre} NO es mayor de edad")
