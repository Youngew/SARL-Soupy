délais = [1, 2, 3, 4, 5, 6]


def restriction_semer(num_employe, num_champ, commandes_info_plantation_champ):
    if (num_employe < num_champ) or (commandes_info_plantation_champ[num_champ - 1] != 'NONE') or (délais[num_employe] > 0): #Si on a un nombre d'employés supérieur au nombre de champs,ou un pas semé, on autorise à arroser le champ, sinon nan
        autorisation_semer = False
        print('OK ça marche')
        if délais[num_employe] > 0:
           délais[num_employe] = délais[num_employe] - 1 
    else:
        autorisation_semer = True
    return autorisation_semer
