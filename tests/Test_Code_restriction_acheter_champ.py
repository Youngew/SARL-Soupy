
from Fonction_restriction_acheter_champ import restriction_acheter_champ

def test_restriction_acheter_champ():
    autorisation_acheter_champ = restriction_acheter_champ(nb_champ = 0)
    assert autorisation_acheter_champ == True

# Test de la fonction avec un nombre de champs égal à 4 (autorisation d'acheter un champ)
#autorisation = restriction_acheter_champ(nb_champ=4)
#assert autorisation == 1

# Test de la fonction avec un nombre de champs égal à 5 (interdiction d'acheter un champ)
#autorisation = restriction_acheter_champ(nb_champ=5)
#assert autorisation == 0 # Affiche 0
    



