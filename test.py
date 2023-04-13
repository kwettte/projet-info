from Groupe import groupe
from Ecole import Ecole
from Activité import acti
from Salle import local


if __name__ == "__main__":

    # ajouter des tests unitaires --> au moins 4 méthodes avec au moins 2 cas testés par méthode
    # toutes les classes intermédiaires doivent être testées

    # ajouter une base de données avec toutes les salles de l'école, leurs usage, nom, capacite, batiment, etage

    # création de l'école ENSTA Bretagne
    ENSTA = Ecole()

    # création d'une salle de classe avec localisation
    A101 = local(usage = 'CM',nom = 'A101',capacite = 200,batiment = 'A',etage = 1)
    # Ajouter une partie d'accès à une base de données regroupant toutes les salles et les infos correspondantes



    # ajout d'étudiants dans une salle
    A101.ajouter_occupant('Alpha')
    A101.ajouter_occupant('Beta')
    A101.ajouter_occupant('Charlie')

    action = input('Que voulez vous faire ? Localiser une salle ? Trouver une salle pour un groupe ?')
    if action == 'Localiser une salle' or 'localiser une salle':
        loc = input('Quelle est la salle désirée ?')
        if loc not in ENSTA.salles:
            print('pas de salle trouvée')

        else:
            print('nom de la salle :', loc.nommer())
            print('localisation de la salle', loc.localiser())

    if action == 'trouver une salle pour une groupe':
        grp = input('Quel est le groupe ?')
        nbr = input('Combien de personnes ?')
        acti = input("Quelle est l'activité ?")
        debut = input("Quelle est l'heure de début ?")
        fin = input("Quelle est l'heure de fin ?")



    # affichage des informations de la salle
    print('nom de la salle :',A101.nommer())
    print('localisation de la salle',A101.localiser())
    print(A101)
