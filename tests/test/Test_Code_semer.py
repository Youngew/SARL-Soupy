#Range, Act, assert

from Fonction_Semer import semer

def test_semer():
    commandes, num_employe, autorisation_semer = semer(num_champ = 1, num_employe = 1, autorisation_semer = True)
    assert num_champ == 2
    assert commandes == ["1 SEMER"]




