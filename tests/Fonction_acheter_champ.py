

def acheter_champ(nb_de_champs_a_acheter, nb_champ, autorisation_acheter_champ): 
    commandes_acheter_champ = []
    if autorisation_acheter_champ:
        for _ in range(nb_de_champs_a_acheter):
                commandes_acheter_champ.append("0 ACHETER_CHAMP") #On demande au gérant d'acheter un champ un nombre de fois égal à ce qui est demandé en entrée de fonction
                nb_champ = nb_champ + 1 #On incrémente le compteur de champs possédés
    return commandes_acheter_champ, nb_champ

    
