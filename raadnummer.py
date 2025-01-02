import random

def play_game():
    print('\nDit is het Raad Nummer Spel!\n'
          'Je hebt 5 kansen om de juiste nummer tussen 1 en 20 te raden, als je het niet doet dan verandert de willekeurige nummer naar een andere, ook tussen 1 en 20.\n')

    nummer_te_raden = random.randint(1, 20)
    pogingen = 0
    pogingen_tot_reset = 0
    resets = 0

    while True:
        raad = input("Kies een nummer tussen 1 en 20: ")
        if raad.isdigit():
            raad = int(raad)
            if raad <= 0 or raad > 20 :
                print("Tussen 1 en 20.")
                continue
        else:
            print("Een getal.")
            continue

        if pogingen_tot_reset == 5:
            print("Nummer is veranderd.")
            nummer_te_raden = random.randint(1, 20)
            pogingen_tot_reset = 0
            resets += 1

        elif raad > nummer_te_raden:
            pogingen += 1
            pogingen_tot_reset += 1
            print("Lager")

        elif raad < nummer_te_raden:
            pogingen += 1
            pogingen_tot_reset += 1
            print("Hoger")

        elif raad == nummer_te_raden:
            print("Goedzo!")
            print('')
            print(f'Je hebt {pogingen} keer geraden.')
            print(f'Nummer is {resets} gereset.')
            break