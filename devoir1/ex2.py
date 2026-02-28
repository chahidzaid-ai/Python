contacts = []
while True:
    print("\n---Menu---")
    print("1. Ajouter un contact")
    print("2. Afficher les contacts")
    print("3. Quitter")

    choix = input("Entrez votre choix : ")

    if choix == "1":
        nom = input("Entrez le nom du contact : ")
        contacts.append(nom)
        print(f"Contact '{nom}' ajouté avec succès.")
        
    elif choix == "2":
        if not contacts:
            print("Aucun contact à afficher.")
        else:
            for i, contact in enumerate(contacts, 1):
                print(f"{i}. {contact}")    

    elif choix == "3":
        print("Au revoir!")
        break
    else:
        print("Choix invalide. Veuillez entrer un nombre entre 1 et 3.")            
