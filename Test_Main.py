from sample_player_client import restriction_semer, acheter_champ, employer, licencier, semer, restriction_acheter_champ, nb_journée

# Test fonction avec 2 employés, 3 champs et plantation de champ 'NONE'
num_employe = 2
num_champ = 3
commandes_info_plantation_champ = ['NONE']
def test_restriction_semer():
    autorisation = restriction_semer(num_employe, num_champ, commandes_info_plantation_champ)

    assert autorisation == True

def test_acheter_champ():
    commandes, nb_champs = acheter_champ(nb_de_champs_a_acheter=1, nb_champ=1, autorisation_acheter_champ=True)
    assert nb_champs == 2
    assert commandes == ["0 ACHETER_CHAMP"]



def test_acheter_champ():
    commandes, nb_champs = acheter_champ(nb_de_champs_a_acheter=1, nb_champ=1, autorisation_acheter_champ=True)
    assert nb_champs == 2
    assert commandes == ["0 ACHETER_CHAMP"]

def test_employer():
    commandes, nb_employe, delais, pos_employe = employer(nb_employes_a_employer=3, nb_employe=1)
    assert delais[0] == 0
    assert pos_employe[0] == 0
    assert nb_employe == 4
    assert commandes == ["0 EMPLOYER", "0 EMPLOYER", "0 EMPLOYER"]




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

def nb_journe():
    commandes_journée = nb_journée("game_data['day']"==2)
    assert commandes_journée == 2

def test_restriction_acheter_champ():
    autorisation_acheter_champ = restriction_acheter_champ(nb_champ = 0)
    assert autorisation_acheter_champ == True

# Test de la fonction avec un nombre de champs égal à 4 (autorisation d'acheter un champ)
#autorisation = restriction_acheter_champ(nb_champ=4)
#assert autorisation == 1

# Test de la fonction avec un nombre de champs égal à 5 (interdiction d'acheter un champ)
#autorisation = restriction_acheter_champ(nb_champ=5)
#assert autorisation == 0 # Affiche 0
    
# Test fonction avec 2 employés, 3 champs et plantation de champ 'NONE'
num_employe = 2
num_champ = 3
commandes_info_plantation_champ = ['NONE']
def test_restriction_semer():
    autorisation = restriction_semer(num_employe, num_champ, commandes_info_plantation_champ)

    assert autorisation == False

def test_semer():
    commandes, num_employe, autorisation_semer = semer(num_champ = 1, num_employe = 1, autorisation_semer = True)
    assert num_champ == 2
    assert commandes == ["1 SEMER"]
