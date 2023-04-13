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
