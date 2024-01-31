choix = input("Veuillez entrer un nombre : ")
nombre = int(choix)
print(f"Votre nombre {nombre}")
for i in range (0, 10):
    multiple = nombre * (i+1)
    print(f"{multiple}")