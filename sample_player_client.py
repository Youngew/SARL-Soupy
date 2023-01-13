import argparse
from typing import NoReturn
from chronobio.network.client import Client

arrosage_champ = [0, 0, 0, 0, 0]

legumes = ["PATATE", "POIREAU", "TOMATE", "OIGNON", "COURGETTE"]

class PlayerGameClient(Client):

    def __init__(
        self: "PlayerGameClient", server_addr: str, port: int
    ) -> None:
        super().__init__(server_addr, port, "Soupy SARL", spectator=False)
        self._commands: list[str] = []

    def run(self: "PlayerGameClient") -> NoReturn:
        while True:

            game_data = self.read_json()

            for farm in game_data["farms"]:

                if farm["name"] == self.username:
                    my_farm = farm
                    break
            else:
                raise ValueError(f"My farm is not found ({self.username})")
            print(my_farm)

            def arroser(num_champ):
                if num_champ == 1 or num_champ == 2:
                    if arrosage_champ[num_champ - 1] == 10:
                        return 0
                    elif arrosage_champ[num_champ - 1] < 6:
                        memoire_employe = 1 + (num_champ - 1) * 5
                        for employe in range(memoire_employe, memoire_employe + 5):
                            self.add_command(f"{employe} ARROSER {num_champ}")
                            arrosage_champ[num_champ - 1] = arrosage_champ[num_champ - 1] + 1
                    else:
                        memoire_employe = 1 + (num_champ - 1) * 5
                        for employe in range(memoire_employe, memoire_employe + 5 - arrosage_champ[num_champ - 1]):
                            self.add_command(f"{employe} ARROSER {num_champ}")
                            arrosage_champ[num_champ - 1] = arrosage_champ[num_champ - 1] + 1
                else:
                    if arrosage_champ[num_champ - 1] == 10:
                       return 0
                    else:
                        memoire_employe = 1 + (num_champ - 2)  * 10
                        for employe in range(memoire_employe, memoire_employe + 10 - arrosage_champ[num_champ - 1]):
                            self.add_command(f"{employe} ARROSER {num_champ}")
                            arrosage_champ[num_champ - 1] = arrosage_champ[num_champ - 1] + 1
            
            for game_data["day"] in range(1800):
               
                if game_data["day"] == 0:

                    self.add_command("0 EMPRUNTER 320000")

                    for _ in range(5):
                        self.add_command(" 0 ACHETER_CHAMP")

                    for _ in range(10):
                        self.add_command(" 0 ACHETER_TRACTEUR")

                    for _ in range(70):
                        self.add_command("0 EMPLOYER")

                    memoire_employe = 1
                    employe = memoire_employe

                    for champ in range(1, 6):

                        if champ < 3:
                            
                            self.add_command(f"{employe} SEMER {legumes[champ - 1]} {champ}")
                            memoire_employe = memoire_employe + 1

                            for employe in range(memoire_employe, memoire_employe + 4):
                                self.add_command(f"{employe} ARROSER {legumes[champ - 1]} {champ}")
                                memoire_employe = employe
                                
                        else:

                            self.add_command(f"{employe} SEMER {legumes[champ -1 ]} {champ}")
                            memoire_employe = memoire_employe + 1

                            for employe in range(memoire_employe, memoire_employe + 9):
                                self.add_command(f"{ employe} ARROSER {legumes[champ - 1]} {champ}")
                                memoire_employe = employe

                    for employe in range(memoire_employe, memoire_employe + 20):
                        self.add_command(f"{employe} CUISINER ")
                        memoire_employe = employe
                    self.send_commands()
                
                else:
                    for champ in range(1, 6):
                        arroser(champ)
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
