import argparse
from typing import NoReturn
from chronobio.network.client import Client

class PlayerGameClient(Client):

    def __init__(
        self: "PlayerGameClient", server_addr: str, port: int
    ) -> None:
        super().__init__(server_addr, port, "Soupy SARL", spectator=False)
        self._commands: list[str] = []

    def run(self: "PlayerGameClient") -> NoReturn:        
        
        champ_cpt = [0, 0, 0, 0, 0]
        champ_seme = [1, 1, 1, 1, 1]
        legumes = ["PATATE", "POIREAU", "TOMATE", "OIGNON", "COURGETTE"]
        tempo = [0, 0, 0, 0, 0]
        stockage = [0, 0, 0, 0, 0]
        N_champ = 0
        tempo_trac = 0
        marche_soupe = 0
        premiere_soupe = 0
        switch = 0


        while True:

            game_data = self.read_json()

            for farm in game_data["farms"]:

                if farm["name"] == self.username:
                    my_farm = farm
                    break
            else:
                raise ValueError(f"My farm is not found ({self.username})")
            print(my_farm)

            def recup_info_arrosage_champ():
                commandes_info_arrosage_champ = [] #On crée la liste qui sotckera les chaînes de caractères à envoyer au serveur
                for num_champ in range(5):
                    commandes_info_arrosage_champ.append(my_farm['fields'][num_champ]['needed_water']) #On met dans une liste l'info d'arrosage de tous les champs
                return commandes_info_arrosage_champ

            def recup_info_plantation_champ():
                commandes_info_plantation_champ = [] #On crée la liste qui sotckera les chaînes de caractères à envoyer au serveur
                for num_champ in range(5):
                    commandes_info_plantation_champ.append(my_farm['fields'][num_champ]['content']) #On met dans une liste l'info du légume actuellement planté de tous les champs
                return commandes_info_plantation_champ
                        
            if game_data["day"] == 0:

                for _ in range(17):
                    self.add_command("0 EMPLOYER")


                self.add_command("0 EMPRUNTER 300000")

                for _ in range(5):
                    self.add_command("0 ACHETER_TRACTEUR")

                self.add_command("0 ACHETER_CHAMP")
                self.add_command("0 ACHETER_CHAMP")
                self.add_command("0 ACHETER_CHAMP")
                self.add_command("0 ACHETER_CHAMP")
                self.add_command("0 ACHETER_CHAMP")
        
                self.add_command("1 SEMER PATATE 1")
                self.add_command("2 SEMER POIREAU 2")
                self.add_command("3 SEMER TOMATE 3")
                self.add_command("4 SEMER OIGNON 4")
                self.add_command("5 SEMER COURGETTE 5")
                self.add_command("6 ARROSER 1")
                self.add_command("7 ARROSER 2")
                self.add_command("8 ARROSER 3")
                self.add_command("9 ARROSER 4")
                self.add_command("10 ARROSER 5")

                self.send_commands()

            elif game_data["day"] == 1:

                self.add_command("1 ARROSER 1")
                self.add_command("6 ARROSER 1")
    
                self.send_commands()

            elif game_data["day"] == 2:

                self.add_command("1 ARROSER 1")
                self.add_command("6 ARROSER 1")
                self.add_command("2 ARROSER 2")
                self.add_command("7 ARROSER 2")

                self.send_commands()

            elif game_data["day"] == 3:

                self.add_command("1 ARROSER 1")
                self.add_command("6 ARROSER 1")
                self.add_command("2 ARROSER 2")
                self.add_command("3 ARROSER 3")
                self.add_command("8 ARROSER 3")

                self.send_commands()

            elif game_data["day"] == 4:

                self.add_command("1 ARROSER 1")
                self.add_command("6 ARROSER 1")
                self.add_command("2 ARROSER 2")
                self.add_command("3 ARROSER 3")
                self.add_command("8 ARROSER 3")
                self.add_command("4 ARROSER 4")
                self.add_command("9 ARROSER 4")

                self.send_commands()

            elif game_data["day"] == 5:

                self.add_command("1 ARROSER 1")
                self.add_command("6 ARROSER 1")
                self.add_command("2 ARROSER 2")
                self.add_command("7 ARROSER 2")
                self.add_command("3 ARROSER 3")
                self.add_command("8 ARROSER 3")
                self.add_command("4 ARROSER 4")
                self.add_command("5 ARROSER 5")
                self.add_command("10 ARROSER 5")

                self.send_commands()

            else:
                
                champ_cpt = recup_info_arrosage_champ() 

                champ_seme = recup_info_plantation_champ()

                if champ_cpt[N_champ] == 0 and tempo_trac < 0:

                    self.add_command(f"{11 + switch} STOCKER {N_champ + 1} {1 + switch}")
                    stockage[N_champ] = stockage[N_champ] + 1000
                    champ_cpt[N_champ] = 0
                    champ_seme[N_champ] = 0
                    tempo_trac = 2

                    if N_champ < 2 :
                        tempo[N_champ] = 6
                    else :
                        tempo[N_champ] = 4

                    if N_champ != 4 :
                        N_champ = N_champ + 1 
                    else :
                        N_champ = 0

                    if switch != 4:
                        switch = switch + 1
                    else :
                        switch = 0

                for i in range(5):

                    if tempo[i] > 0:

                        tempo[i] = tempo[i] - 1

                    elif champ_seme[i] == "NONE":

                        self.add_command(f"{i + 1} SEMER {legumes[i]} {i + 1}")
                        self.add_command(f"{i + 6} SEMER {legumes[i]} {i + 1}")
                        champ_seme[i] = 1

                    elif champ_cpt[i] > 0 :

                        self.add_command(f"{i + 1} ARROSER {i + 1}")
                        self.add_command(f"{i + 6} ARROSER {i + 1}")
                        champ_cpt[i] = champ_cpt[i] - 1 

                tempo_trac = tempo_trac - 1
                
                cpt_5_legume = 0

                for i in range(5):
                    contenant = stockage[i] 
                    if contenant != 0:
                        cpt_5_legume = cpt_5_legume + 1

                if cpt_5_legume == 5  :

                    if marche_soupe == 0 :

                        if premiere_soupe == 0 :

                            self.add_command("16 CUISINER")
                            self.add_command("17 CUISINER")
                            for i in range(5):
                                stockage[i] = stockage[i] - 100
                            premiere_soupe = 1
                            marche_soupe = 6

                        else :

                            self.add_command("16 CUISINER")
                            self.add_command("17 CUISINER")
                            cpt_5_legume = 0
                            for i in range(5):
                                stockage[i] = stockage[i] - 100
                        
                    else :

                        marche_soupe = marche_soupe - 1

                self.send_commands() 


    def add_command(self: "PlayerGameClient", command: str) -> None:

        self._commands.append(command)

    def send_commands(self: "PlayerGameClient") -> None:

        data = {"commands": self._commands}
        print("sending", data)
        self.send_json(data)
        self._commands.clear()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Game client.")
    parser.add_argument(
        "-a",
        "--address",
        type=str,
        help="name of server on the network",
        default="localhost",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        help="location where server listens",
        default=1025,
    )
    args = parser.parse_args()

    client = PlayerGameClient(args.address, args.port).run()
