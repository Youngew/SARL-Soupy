délais = [1, 2, 3]
pos_employe = [(1, 1), (2, 2), (3, 3)] 

def licencier(num_employe, autorisation_licencier):
    commandes_licencier = 0
    if autorisation_licencier:
        commandes_licencier = f"0 LICENCIER {num_employe}" #On demande de virer un employer
        del délais[num_employe]
        del pos_employe[num_employe]
    else:
        commandes_licencier = 'NONE'
    return commandes_licencier

    
