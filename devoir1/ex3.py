mot_de_passe_correct = "python123"

mot_de_passe = input("Entrez le mot de passe : ")

while mot_de_passe != mot_de_passe_correct:
    print("Mot de passe incorrect. Veuillez réessayer.")
    mot_de_passe = input("Entrez le mot de passe : ")
    
print("Mot de passe correct. Accès autorisé.")