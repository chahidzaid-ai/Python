donnees = [
("Sara", "Math", 12, "G1"),
("Sara", "Info", 14, "G1"),
("Ahmed", "Math", 9, "G2"),
("Adam", "Chimie", 18, "G1"),
("Sara", "Math", 11, "G1"),
("Bouchra", "Info", "abc", "G2"),
("", "Math", 10, "G1"),
("Yassine", "Info", 22, "G2"),
("Ahmed", "Info", 13, "G2"),
("Adam", "Math", None, "G1"),
("Sara", "Chimie", 16, "G1"),
("Adam", "Info", 7, "G1"),
("Ahmed", "Math", 9, "G2"),
("Hana", "Physique", 15, "G3"),
("Hana", "Math", 8, "G3"),
]
def valider(ligne):
    nom, matiere, note, groupe = ligne

    if nom == "" or matiere == "" or groupe == "":
        return False, "Champ vide"

    try:
        note = float(note)
    except:
        return False, "Note invalide"

    if note < 0 or note > 20:
        return False, "Note hors limite"

    return True, ""

valides = []
erreurs = []
doublons_exact = set()
vus = set()

for ligne in donnees:

    if ligne in vus:
        doublons_exact.add(ligne)
    vus.add(ligne)

    ok, raison = valider(ligne)

    if ok:
        nom, matiere, note, groupe = ligne
        valides.append((nom, matiere, float(note), groupe))
    else:
        erreurs.append({"ligne": ligne, "raison": raison})
     
matieres = set()

etudiants = {}

groupes = {}

for nom, matiere, note, groupe in valides:

    matieres.add(matiere)

    if nom not in etudiants:
        etudiants[nom] = {}

    if matiere not in etudiants[nom]:
        etudiants[nom][matiere] = []

    etudiants[nom][matiere].append(note)

    if groupe not in groupes:
        groupes[groupe] = set()

    groupes[groupe].add(nom)


def somme_recursive(liste):
    if len(liste) == 0:
        return 0
    return liste[0] + somme_recursive(liste[1:])

def moyenne(liste):
    if len(liste) == 0:
        return 0
    return somme_recursive(liste) / len(liste)

moyennes = {}

for nom in etudiants:
    toutes_notes = []

    for matiere in etudiants[nom]:
        toutes_notes += etudiants[nom][matiere]

    moyennes[nom] = moyenne(toutes_notes)

alertes = {
    "doublon_matiere": [],
    "profil_incomplet": [],
    "groupes_faibles": [],
    "ecart_grand": []
}

for nom in etudiants:
    for matiere in etudiants[nom]:
        if len(etudiants[nom][matiere]) > 1:
            alertes["doublon_matiere"].append(nom)

for nom in etudiants:
    if len(etudiants[nom]) < len(matieres):
        alertes["profil_incomplet"].append(nom)

SEUIL = 10

for groupe in groupes:
    notes_groupe = []

    for nom in groupes[groupe]:
        notes_groupe.append(moyennes[nom])

    if moyenne(notes_groupe) < SEUIL:
        alertes["groupes_faibles"].append(groupe)

for nom in etudiants:
    notes = []

    for matiere in etudiants[nom]:
        notes += etudiants[nom][matiere]

    if len(notes) > 0:
        if max(notes) - min(notes) >= 10:
            alertes["ecart_grand"].append(nom)

print("Valides :", valides)
print("Erreurs :", erreurs)
print("Doublons exacts :", doublons_exact)
print("Moyennes :", moyennes)
print("Alertes :", alertes)     
