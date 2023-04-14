import Groupe
import unittest

class TestGroupe(unittest.TestCase):

    def test_ajout_participant(self, nom, membres, etat, acti):
        groupe = Groupe.TD()
        groupe.append("salle")
        self.assertEqual(self.groupe.nombre, 1)


if __name__ == '__main__':
    unittest.main()