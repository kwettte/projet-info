from Groupe import groupe

class acti():

    def __init__(self, nom, debut: str, fin: str, groupe: groupe, usage: str):
        """
        Créer une une activité
        :param nom:
        :param debut: str
        :param fin: str
        :param groupe: groupe
        """
        self.nom = nom # la matière concernée apparait dans le nom de l'activité
        self.__debut = debut # vrenvoie l'heure au format tuple
        self.debut = debut # renvoie l'heure au format h:m
        self.__fin = fin # vrenvoie l'heure au format tuple
        self.fin = fin # renvoie l'heure au format h:m
        self.groupe = groupe
        self.usage = usage
        self.info = False # True si besoin d'ordinateurs, par exemple pour un TD d'info

    @property
    def debut(self):
        h, m = self.__debut
        return str(h) + ':' + str(m)

    @debut.setter
    def debut(self, newHeure: str):
        newHeure = newHeure.split(':')
        h, m = newHeure[:]
        self.__debut = (h, m)

    @property
    def fin(self):
        h, m = self.__fin
        return str(h) + ':' + str(m)

    @fin.setter
    def fin(self, newHeure: str):
        newHeure = newHeure.split(':')
        h, m = newHeure[:]
        self.__fin = (h, m)

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
        self.usage = "TD"
        self.info = True

class CM(acti):

    def __init__(self,eleves,nom):
        super().__init__(eleves, nom)
        self.usage = "CM"

class examen(acti):

    def __init__(self):
        super().__init__()
