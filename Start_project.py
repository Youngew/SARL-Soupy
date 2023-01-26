import signal
import os
import random
import argparse


port = random.randint(50000, 55000)


def handle_sigint(signum, frame):
    print("\n\nFERMETURE DE LA FERME\n\n")
    os._exit(0)


def main(f) -> int:

    os.system(
        "cls && echo LANCEMENT DES TESTS && pytest --cov= test.py"
        "&& echo LANCEMENT DE MYPY && mypy farm.py "
        f"&& echo LANCEMENT DE LA FERME && start /B pythonw3 -m chronobio.game.server {f} -p {2000} "
        f"&& python3 sample_player_client.py -p {2000}"
    )
    return 0


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fast", help="Mode fast", action="store_true")
    args = parser.parse_args()

    fast = "--fast" if args.fast else ""

    main(fast)
