import Activité
import unittest

class TestActi(unittest.TestCase):

    def test_debut(self):
        acti = Activité.acti(nom = 'TD de maths', debut = '10:00', fin = '12:00', groupe = ['Alice'])
        self.assertEqual(acti.debut,'10:00')


if __name__ == '__main__':
    unittest.main()

