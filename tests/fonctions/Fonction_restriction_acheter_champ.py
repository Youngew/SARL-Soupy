


def restriction_acheter_champ(nb_champ):
    if nb_champ >= 5: #Si on a déjà 5 champs, on autorise à acheter un autre champ, sinon nan
        autorisation_acheter_champ = False
    else:
        autorisation_acheter_champ = True
    return autorisation_acheter_champ
