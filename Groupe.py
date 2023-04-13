class groupe():

    """
    Création d'une classe groupe d'étudiants à placer dans une salle
    """

    def __init__(self, nom, membres ,etat, acti):
        self.nom = nom
        self.membres = membres
        self.etat = etat # indique si le groupe d'élèves est placé dans une salle
        self.activite = acti

    def ajouter_participant(self, participant):
        self.membres.append(participant)

    def enlever_participant(self, participant):
        if participant in self.membres:
            self.membres.remove(participant)

    def trouver_salle(self, salles, debut, fin):
        # on parcourt toutes les salles et on vérifie si elles sont disponibles
        for salle in salles:
            if salle.usage == self.activite and salle.disponible(debut,fin):
                return salle
        # si aucune salle n'est disponible, on retourne None
        return None

    def __str__(self):
        return f"Groupe {self.nom} ({len(self.membres)} membres pour l'activité {self.activite}"


class Promo(groupe):

    def __init__(self,nom, membres ,etat, acti):
        super().__init__(nom, membres ,etat, acti)
        self.activite = 'CM'


"""

# version pour avoir un héritage depuis un type intégré 

class groupe(list):
    def __init__(self,nom, activite):
        super().__init__()
        self.nom = nom
        self.activite = activite
        self.salle = None
        self.date_debut = None
        self.date_fin = None
"""