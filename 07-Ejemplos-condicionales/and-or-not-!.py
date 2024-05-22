pais = "España"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un pais de habla hispana !!")


else:
    print(f"{pais} No es un pais de habla hispana")




print(".-.-.-.-.-.--.-.OTRO EJEMPLO.-.-.-.-.-.-.-.-")

pais = "España"

if not(pais == "Mexico" or pais == "España" or pais == "Colombia"): #SI esto NO se cumple
    print(f"{pais} NO es un pais de habla hispana ")  #Vamos aqui


else:
    print(f"{pais} Si es un pais de habla hispana !!!!!")

print(".-.-.-.-.-.--.-.OTRO EJEMPLO.-.-.-.-.-.-.-.-")



pais = "Colombia"

if pais != "Mexico" and pais != "España" and pais != "Colombia": 
    print(f"{pais} NO es un pais de habla hispana ")  


else:
    print(f"{pais} Si es un pais de habla hispana !!!!!")