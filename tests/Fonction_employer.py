delais=[]
pos_employe=[]

def employer(nb_employes_a_employer, nb_employe):
    commandes_employer_employe = []
    for _ in range(nb_employes_a_employer): 
        commandes_employer_employe.append("0 EMPLOYER") #On demande au gérant d'employer un employé un nombre de fois égal à ce qui est demandé en entrée de fonction
        nb_employe = nb_employe + 1 #On incrémente le compteur d'employés possédés
        delais.append(0)
        pos_employe.append(0)
    return commandes_employer_employe, nb_employe, delais, pos_employe

    
