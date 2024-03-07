import configparser
from pynput.keyboard import Key, Listener

# Načtení konfiguráku
config = configparser.ConfigParser()
config.read('./config/config.ini')

# Slovník pro uchování počtu stisků kláves
key_counts = {}

# Celkový počet stisknutých kláves
total_key_presses = 0

def on_press(key):
    global total_key_presses
    # Převedení objektu Key na řetězec pro jednodušší práci
    key_str = str(key).replace("'", "")

    # Inkrementace počtu stisků klávesy v slovníku
    if key_str in key_counts:
        key_counts[key_str] += 1
    else:
        key_counts[key_str] = 1

    # Inkrementace celkového počtu stisků kláves
    total_key_presses += 1

    # Zápis celkového počtu stisků a počtu stisků každé klávesy do souboru
    with open('./results/results.txt', 'w') as file:
        file.write(f'Kláves zmáčknuto: {total_key_presses}\n')
        for k, v in key_counts.items():
            file.write(f'{k}: {v}\n')

    print(f'Klávesa {key_str} zmáčkuta dohromady {key_counts[key_str]} x')
    print(f'Klávesa {key_str} zmáčkuta dohromady {key_counts[key_str]} x')


# Spuštění listeneru a sběr událostí
with Listener(on_press=on_press) as listener:
    listener.join()
