import Groupe

class local():


    def __init__(self, usage, nom, capacite, batiment, etage, debut, fin):
        """
        Créer une salle à une localisation précise (batiment et étage)
        et une capacité d'occupants prédéfinie
        :param usage: str
        :param nom: str
        :param capacite: int
        :param batiment: str
        :param etage: int
        :param debut: tuple
        :param fin: tuple
        """
        self.usage = usage
        self.nom = nom
        self.capacite = capacite
        self.batiment = batiment
        self.etage = etage
        self.occupe = False # définit l'état de la salle si elle est occupée ou non
        self.occupants = []
        self.debut = debut
        self.fin = fin

    def ajouter_occupant(self,participant): # méthode pour ajouter des participants dans une salle s'il reste de la place
        # on commence par vérifier s'il reste de la place dans la salle
        if len(self.occupants) < self.capacite:
            self.occupants.append(participant)
            print(f"{participant} a été ajouté au {self.nom}")
        else:
            print(f"{self.nom} est pleine")

    def enlever_occupant(self,participant):
        if participant in self.occupants:
            self.occupants.remove(participant)
        else:
            print(f"{participant} n'est pas dans {self.nom}")

    def localiser(self,):
        localisation = f"bâtiment {self.batiment}, étage {self.etage}"
        return localisation

    def nommer(self):
        return self.nom

    def disponible(self,debut,fin):
        if not self.occupe:
            return True
        else:
            # on vérifie si les périodes se chevauchent
            return (fin <= self.debut) or (debut >= self.fin)

    def occupants(self,debut,fin):
        if self.occupe:
            return f"{self.occupants} dans la salle {self.nom} de {debut} à {fin}"
        else:
            return f"personne dans la salle {self.nom} de {debut} à {fin}"

    def __str__(self): # retourne le nombre de places occupées sur la capacité totale
        return f"{self.nom} ({len(self.occupants)}/{self.capacite} occupants)"
