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


# on crée par héritage des classes pour les différents types d'activités proposées au sein de l'ENSTA Bretagne


class TP(acti):

    def __init__(self,eleves,nom):
        super().__init__(eleves,nom)
        self.usage = "TP"

class TD(acti):

    def __init__(self,eleves,nom):
        super().__init__(eleves, nom)
        self.usage = "TD"


# une classe TD_info ayant pour caractéristiques de nécessiter des ordinateurs
class TD_info(acti):

    def __init__(self,eleves,nom):
        super().__init__(eleves, nom)
        self.usage = "TD_info"

class CM(acti):

    def __init__(self,eleves,nom):
        super().__init__(eleves, nom)
        self.usage = "CM"
