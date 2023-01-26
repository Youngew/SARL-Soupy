#Range, Act, assert

from Fonction_acheter_champ import acheter_champ


def test_acheter_champ():
    commandes, nb_champs = acheter_champ(nb_de_champs_a_acheter=1, nb_champ=1, autorisation_acheter_champ=True)
    assert nb_champs == 2
    assert commandes == ["0 ACHETER_CHAMP"]




