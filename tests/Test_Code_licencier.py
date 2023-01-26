
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


