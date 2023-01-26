
from Fonction_nb_journee import nb_journée

def nb_journe():
    commandes_journée = nb_journée("game_data['day']"==2)
    assert commandes_journée == 2


