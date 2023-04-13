
class local():

    """
    Classe décrivant la définition d'un local dans l'école, d'une salle de
    classe
    """

    def __init__(self,usage,nom,capacite,batiment,etage):
        """
        Créer une salle à une localisation précise (batiment et étage)
        et une capacité d'occupants prédéfinie
        :param usage: str
        :param nom: str
        :param capacite: int
        :param batiment: str
        :param etage: int
        """
        self.usage = usage
        self.nom = nom
        self.capacite = capacite
        self.batiment = batiment
        self.etage = etage
        self.occupe = False # définit l'état de la salle si elle est occupée ou non
        self.occupants = []

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

    def __str__(self): # retourne le nombre de places occupées sur la capacité totale
        return f"{self.nom} ({len(self.occupants)}/{self.capacite} occupants)"


class Ecole():

    """
    Création d'une classe Ecole regroupant toutes les salles de l'ENSTA Bretagne
    """

    def __init__(self):
        self.nom = 'ENSTA Bretagne'
        self.salles = []

    def ajouter_salle(self,salle):
        self.salles.append(salle)


    # méthode pour trouver si il y a une salle dispo pour une activité et un créneau donnés
    def trouver_salle_dispo(self,activite,debut,fin):
        for salle in self.salles:
            if activite.usage in salle.usage and not salle.occupe:
                if activite.localisation == salle.localisation:
                    disponible = True
                    for groupe in activite.groupes:
                        if groupe.salle == salle:
                            continue
                        if groupe.heure_debut < fin and debut < groupe.heure_fin:
                            disponible = False
                            break
                    if disponible:
                        return salle
        return None


class acti():

    def __init__(self,eleves,nom,debut,fin,groupe):
        """
        Créer une une activité
        :param eleves:
        :param nom:
        :param debut:
        :param fin:
        :param groupe:
        """
        self.nbr_eleves = eleves
        self.nom = nom # la matière concernée apparait dans le nom de l'activité
        self.debut = debut
        self.fin = fin
        self.groupe = groupe


class TP(acti):

    def __init__(self,eleves,nom):
        super().__init__(eleves,nom)
        self.usage = "TP"

class TD(acti):

    def __init__(self,eleves,nom):
        super().__init__(eleves, nom)
        self.usage = "TD"

class TD_info(acti):

    def __init__(self,eleves,nom):
        super().__init__(eleves, nom)
        self.usage = "TD_info"

class CM(acti):

    def __init__(self,eleves,nom):
        super().__init__(eleves, nom)
        self.usage = "CM"



class groupe():

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




if __name__ == "__main__":

    # création d'une salle de classe avec localisation
    A101 = local(usage = 'CM',nom = 'A101',capacite = 200,batiment = 'A',etage = 1)

    # ajout d'étudiants
    A101.ajouter_occupant('Alpha')
    A101.ajouter_occupant('Beta')
    A101.ajouter_occupant('Charlie')

    # affichage des informations de la salle
    print('nom de la salle :',A101.nommer())
    print('localisation de la salle',A101.localiser())
    print(A101)
