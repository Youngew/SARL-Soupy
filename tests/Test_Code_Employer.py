
from Fonction_employer import employer


def test_employer():
    commandes, nb_employe, delais, pos_employe = employer(nb_employes_a_employer=3, nb_employe=1)
    assert delais[0] == 0
    assert pos_employe[0] == 0
    assert nb_employe == 4
    assert commandes == ["0 EMPLOYER", "0 EMPLOYER", "0 EMPLOYER"]




