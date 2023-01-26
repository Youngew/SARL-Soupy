#Range, Act, assert

# pytest ou py.test

# pytest -rA : Avoir détails sur tests

# pytest test_1.py -rA : n'execute que le fichier test_1

# pytest -rA -k "test_3" : Analyse tout et execute toutes les fonctions "test_3".

# pytest test_1.py -rA -k "test_3" : n'execute que la fonction "test_3" du fichier test_1.

# pytest -rA -k "test_3" -v : Analyse tout t execute toutes les fonctions "test_3" avec plus d'infos.

# pytest -s : Affiche prints pour debbug.

# pytest -s -v : Execute avec détails et écrit les prints pour debbug.

# pytest -vv --cov=. Semer.py : Coverage

from Fonction_acheter_champ import acheter_champ


def test_acheter_champ():
    commandes, nb_champs = acheter_champ(nb_de_champs_a_acheter=1, nb_champ=1, autorisation_acheter_champ=True)
    assert nb_champs == 2
    assert commandes == ["0 ACHETER_CHAMP"]

from Fonction_employer import employer


def test_employer():
    commandes, nb_employe, delais, pos_employe = employer(nb_employes_a_employer=3, nb_employe=1)
    assert delais[0] == 0
    assert pos_employe[0] == 0
    assert nb_employe == 4
    assert commandes == ["0 EMPLOYER", "0 EMPLOYER", "0 EMPLOYER"]
from Fonction_licencier import licencier

# On définit les variables nécessaires


def test_licencier():
    #délais = [1, 2, 3]
    #pos_employe = [(1, 1), (2, 2), (3, 3)]

    # Test de la fonction avec une autorisation de licenciement
    num_employe = 1
    autorisation_licencier = True
    commandes_licencier = licencier(num_employe, autorisation_licencier)
    assert commandes_licencier == "0 LICENCIER 1"
    #assert délais == [2, 3]
    #assert pos_employe == [(2, 2), (3, 3)]
    
    # Test de la fonction avec une interdiction de licenciement
    num_employe = 2
    autorisation_licencier = False
    commandes_licencier = licencier(num_employe, autorisation_licencier)
    assert commandes_licencier == 'NONE'

from Fonction_nb_journee import nb_journée

def nb_journe():
    commandes_journée = nb_journée("game_data['day']"==2)
    assert commandes_journée == 2



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
    
from Fonction_Restriction_Semer import restriction_semer 
# Test fonction avec 2 employés, 3 champs et plantation de champ 'NONE'
num_employe = 2
num_champ = 3
commandes_info_plantation_champ = ['NONE']
def test_restriction_semer():
    autorisation = restriction_semer(num_employe, num_champ, commandes_info_plantation_champ)

    assert autorisation == False

#Range, Act, assert

from Fonction_Semer import semer

def test_semer():
    commandes, num_employe, autorisation_semer = semer(num_champ = 1, num_employe = 1, autorisation_semer = True)
    assert num_champ == 2
    assert commandes == ["1 SEMER"]





