from abc import ABC, abstractmethod
from dataclasses import dataclass

class Boisson(ABC):

    @abstractmethod
    def cout(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

    def __add__(self, other):
        desc_combinee = self.description() + " + " + other.description()
        prix_total = self.cout() + other.cout()

        class BoissonCombinee(Boisson):
            def cout(self):
                return prix_total
            def description(self):
                return desc_combinee

        return BoissonCombinee()

    def afficher_commande(self):
        print(f"Commande : {self.description()}")
        print(f"Prix : {self.cout():.1f}€")

class Cafe(Boisson):

    def cout(self):
        return 2.0

    def description(self):
        return "Café simple"

class The(Boisson):

    def cout(self):
        return 1.5

    def description(self):
        return "Thé"

class ChocolatChaud(Boisson):

    def cout(self):
        return 2.5

    def description(self):
        return "Chocolat chaud"

class DecorateurBoisson(Boisson):

    def __init__(self, boisson):
        self._boisson = boisson

class Lait(DecorateurBoisson):

    def cout(self):
        return self._boisson.cout() + 0.5

    def description(self):
        return self._boisson.description() + ", Lait"

class Sucre(DecorateurBoisson):

    def cout(self):
        return self._boisson.cout() + 0.2

    def description(self):
        return self._boisson.description() + ", Sucre"

class Caramel(DecorateurBoisson):

    def cout(self):
        return self._boisson.cout() + 0.7

    def description(self):
        return self._boisson.description() + ", Caramel"

@dataclass
class Client:
    nom: str
    numero: int
    points_fidelite: int = 0

class Commande:

    def __init__(self, client):
        self.client = client
        self.boissons = []

    def ajouter_boisson(self, boisson):
        self.boissons.append(boisson)

    def prix_total(self):
        return sum(b.cout() for b in self.boissons)

    def afficher(self):
        print(f"=== Commande de {self.client.nom} ===")
        for b in self.boissons:
            print(f"  - {b.description()} : {b.cout():.2f}€")
        print(f"  TOTAL : {self.prix_total():.2f}€")

class CommandeSurPlace(Commande):

    def afficher(self):
        print("[ Sur place ]")
        super().afficher()

class CommandeEmporter(Commande):

    TAXE_EMBALLAGE = 0.10

    def prix_total(self):
        return super().prix_total() + len(self.boissons) * self.TAXE_EMBALLAGE

    def afficher(self):
        print("[ À emporter ]")
        super().afficher()
        print(f"  (taxe emballage : {len(self.boissons) * self.TAXE_EMBALLAGE:.2f}€ incluse)")

class Fidelite:

    def ajouter_points(self, client, montant):
        points_gagnes = int(montant)
        client.points_fidelite += points_gagnes
        print(f"  +{points_gagnes} points de fidélité -> Total : {client.points_fidelite} pts")

class CommandeFidele(Commande, Fidelite):

    def valider(self):
        total = self.prix_total()
        self.afficher()
        print("\n--- Validation de la commande ---")
        self.ajouter_points(self.client, total)

if __name__ == "__main__":

    boisson = Cafe()
    boisson = Lait(boisson)
    boisson = Sucre(boisson)
    boisson.afficher_commande()

    print()

    cafe_caramel = Caramel(Cafe())
    cafe_caramel.afficher_commande()

    print()

    menu = Cafe() + The()
    menu.afficher_commande()

    print()

    zaid = Client(nom="Zaid", numero=1)
    print(f"Client : {zaid}\n")

    cmd_sur_place = CommandeSurPlace(zaid)
    cmd_sur_place.ajouter_boisson(Lait(Cafe()))
    cmd_sur_place.ajouter_boisson(The())
    cmd_sur_place.afficher()

    print()

    cmd_emporter = CommandeEmporter(zaid)
    cmd_emporter.ajouter_boisson(Caramel(Cafe()))
    cmd_emporter.afficher()

    print()

    anass = Client(nom="Anass", numero=2)
    cmd_fidele = CommandeFidele(anass)
    cmd_fidele.ajouter_boisson(Lait(Sucre(Cafe())))
    cmd_fidele.ajouter_boisson(ChocolatChaud())
    cmd_fidele.valider()
    print(f"\nClient après commande : {anass}")