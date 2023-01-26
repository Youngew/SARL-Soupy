
from Fonction_Restriction_Semer import restriction_semer 
# Test fonction avec 2 employés, 3 champs et plantation de champ 'NONE'
num_employe = 2
num_champ = 3
commandes_info_plantation_champ = ['NONE']
def test_restriction_semer():
    autorisation = restriction_semer(num_employe, num_champ, commandes_info_plantation_champ)

    assert autorisation == False

