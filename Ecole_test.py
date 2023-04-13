import Ecole
import Salle
import unittest

class TestEcole(unittest.TestCase):

    def test_ajout_salle(self):
        salle = Salle.local(usage = 'CM',nom = 'A101',capacite = 200,batiment = 'A',etage = 1)
        ecole = Ecole.Ecole()
        ecole.append(salle)
        self.assertEqual(len(ecole), 1)


if __name__ == '__main__':
    unittest.main()