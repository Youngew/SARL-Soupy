
def semer(num_champ, num_employe, autorisation_semer):
    if autorisation_semer:
        commandes_semance = f"{num_employe} SEMER {legumes[num_champ - 1]} {num_champ}" #On demande à un employé de semer
        délais[num_employe] = abs(num_champ - (pos_employe[num_employe]))
        pos_employe[num_employe] = num_champ
    return commandes_semance
