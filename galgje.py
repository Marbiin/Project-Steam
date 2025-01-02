import random

def play_game():
    woordenlijst = ("telefoon", "water", "continent", "laptop", "python", "alfabet")
    woord_te_raden = random.choice(woordenlijst)
    geraden_woord = ["_"] * len(woord_te_raden)
    fouten = 0
    max_fouten = 6
    hangman_art = {0: ("   ",
                       "   ",
                       "   "),
                      1: (" o ",
                       "   ",
                       "   "),
                       2: (" o ",
                       " | ",
                       "   "),
                       3: (" o ",
                       "/| ",
                       "   "),
                       4: (" o ",
                       "/|\\",
                       "   "),
                       5: (" o ",
                       "/|\\",
                       "/  "),
                       6: (" o ",
                       "/|\\",
                       "/ \\")}

    print(f"\nDit is het Galgje Spel!\n"
          f"Het woord te raden heeft {len(woord_te_raden)} letters.")

    for letter in geraden_woord:
        print(letter, end=" ")

    while fouten < max_fouten and '_' in geraden_woord:
        for line in hangman_art[fouten]:
            print(line)

        gok = input("Raad een letter: ").lower().strip()

        if gok in woord_te_raden:
            for i in range(len(woord_te_raden)):
                if woord_te_raden[i] == gok:
                    geraden_woord[i] = gok
            print("Goedzo!")
        else:
            fouten += 1
            print(f"Fout! Je hebt nog {max_fouten - fouten} kansen.")

        for letter in geraden_woord:
            print(letter, end=" ")
        print()
    if "_" not in geraden_woord:
        print(f"Goedzo! Het woord was {woord_te_raden}.")
    else:
        for line in hangman_art[fouten]:
            print(line)
        print(f"Je hebt het woord niet geraden, het woord was {woord_te_raden}.")