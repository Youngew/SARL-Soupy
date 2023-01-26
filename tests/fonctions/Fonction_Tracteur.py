



def acheter_tracteur(nb_de_tracteurs_a_acheter, nbtracteur):
    commandes = []
    for _ in range(nb_de_tracteurs_a_acheter):
        commandes.append("0 ACHETER_TRACTEUR")  # On demande au gérant d'acheter un tracteur un nombre de fois égal à ce qui est demandé en entrée de fonction
        nb_tracteur = nb_tracteur + 1  # On incrémente le compteur d'employés possédés
    return commandes, nb_tracteur
