import Salle
import unittest


if __name__ == 'main':
    amphi1 = Salle.local(usage='CM', nom='Amphi 1', capacite=240, batiment='A', etage=0)
    amphi2 = Salle.local(usage='CM', nom='Amphi 2', capacite=144, batiment='A', etage=0)
    amphi3 = Salle.local(usage='CM', nom='Amphi 3', capacite=116, batiment='A', etage=0)
    F005 = Salle.local(usage='TD', nom='F005', capacite=24, batiment='F', etage=0)
    E205 = Salle.local('TD','E205',40,E,2)



