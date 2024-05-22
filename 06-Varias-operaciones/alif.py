dia = 4

if dia == 1:
    print("Es lunes")

elif dia == 2:
    print("Es martes")

elif dia == 3:
    print("Es miercoles")

elif dia == 4:
    print("Es Jueves")

elif dia == 5:
    print("Es viernes")
    
else:
    print("Ya es fin de semana")

print(".-.-.-.-.-.-.-.-.-.-.-.-.-Ejercicio 2..-.-.-.-.-.-..-..-")

edad_minima = 18
edad_maxima = 65
edad_oficial = int(input("Tienes edad de trabajar? Introduce tu edad: "))

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Esta en edad de trabajar")


else:
    print("No esta en edad de trabajar")