import unittest
from CalculerSalaire import *

class TestVerif(unittest.TestCase):

    def test_CalculerSalaire_Architecte(self):
        # print("coucou")
        # self.appel test unitaire (la fonction(mycode) ou si ** m (parametre de fonction, ce qu'on veux afficher)
        self.assertEqual(CalculerSalaire("Architecte", 4), "4000 euros")
        # print ("le salaire de l'Architecte est: 4000 euros")

    def test_CalculerSalaire_medecin(self):
        # print("ohlalal")
        # self.appel test unitaire (la fonction(mycode) ou si ** m (parametre de fonction, ce qu'on veux afficher)
        self.assertEqual(CalculerSalaire("médecin", 8), "7000 euros")
        # print("le salaire du médecin est: 7000 euros")

    def test_CalculerSalaire_consultant(self):
        # print("c bien")
        # self.appel test unitaire (la fonction(mycode) ou si ** m (parametre de fonction, ce qu'on veux afficher)
        self.assertEqual(CalculerSalaire("consultant", 5), "5000 euros")
        # print("le salaire du consultant est: 5000 euros")


if __name__ == '__main__':
    unittest.main()
# il faut toujour ajouter  les deux dernières phrases