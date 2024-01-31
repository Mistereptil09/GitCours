continuer = True
while continuer:
    choix = input("Veuillez entrer un nombre : ")
    nombre = int(choix)
    print(f"Votre nombre {nombre}")
    for i in range(0, 10):
        multiple = nombre * (i+1)
        print(f"{multiple}")
    choix = input("Voullez vous continuer ? (oui pour continuer) : ")
    choix = choix.lower()
    if choix == "oui":
        continuer = True
    else:
        continuer = False
        print("Merci d'avoir essayé")
