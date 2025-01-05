from tkinter import *
import random

galgje_state = {}
raadnummer_state = {}

def verwijderen_main_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

def play_hangman():
    global galgje_state
    verwijderen_main_frame()

    woordenlijst = ["telefoon", "water", "continent", "laptop", "python", "alfabet"]
    woord_te_raden = random.choice(woordenlijst)
    galgje_state = {
        "woord": woord_te_raden,
        "geraden_woord": ["_"] * len(woord_te_raden),
        "fouten": 0,
        "max_fouten": 6
    }

    def submit_letter():
        letter = input_entry.get().strip().lower()
        input_entry.delete(0, END)

        if letter in galgje_state["woord"]:
            for i, char in enumerate(galgje_state["woord"]):
                if char == letter:
                    galgje_state["geraden_woord"][i] = letter
            result_label.config(text="Goedzo!")
        else:
            galgje_state["fouten"] += 1
            result_label.config(text=f"Fout! Nog {galgje_state['max_fouten'] - galgje_state['fouten']} kansen.")

        word_label.config(text=" ".join(galgje_state["geraden_woord"]))

        if "_" not in galgje_state["geraden_woord"]:
            result_label.config(text=f"Gewonnen! Het woord was '{galgje_state['woord']}'.")
            submit_button.config(state=DISABLED)
        elif galgje_state["fouten"] >= galgje_state["max_fouten"]:
            result_label.config(text=f"Verloren! Het woord was '{galgje_state['woord']}'.")
            submit_button.config(state=DISABLED)

    word_label = Label(main_frame, text=" ".join(galgje_state["geraden_woord"]), font=("Courier", 18), bg="#0B0F1D", fg="white")
    word_label.pack(pady=20)

    input_entry = Entry(main_frame, font=("Arial", 16))
    input_entry.pack(pady=10)

    submit_button = Button(
        main_frame, text="Submit Letter", command=submit_letter,
        bg="#1C2A3A", fg="white", font=("Arial", 16)
    )
    submit_button.pack(pady=10)

    result_label = Label(main_frame, text="", font=("Arial", 14), bg="#0B0F1D", fg="white")
    result_label.pack(pady=10)


def play_guess_number():
    global raadnummer_state
    verwijderen_main_frame()

    raadnummer_state = {
        "nummer": random.randint(1, 20),
        "pogingen": 0,
        "max_pogingen": 5
    }

    def submit_guess():
        guess = input_entry.get().strip()
        input_entry.delete(0, END)

        if not guess.isdigit():
            result_label.config(text="Voer een geldig getal in.")
            return

        guess = int(guess)
        raadnummer_state["pogingen"] += 1

        if guess < raadnummer_state["nummer"]:
            result_label.config(text="Hoger!")
        elif guess > raadnummer_state["nummer"]:
            result_label.config(text="Lager!")
        else:
            result_label.config(text=f"Goedzo! Het nummer was {raadnummer_state['nummer']}.")
            submit_button.config(state=DISABLED)
            return

        if raadnummer_state["pogingen"] >= raadnummer_state["max_pogingen"]:
            raadnummer_state["nummer"] = random.randint(1, 20)
            raadnummer_state["pogingen"] = 0
            result_label.config(text="Je kansen zijn op! Het nummer is veranderd.")

    # UI for Guess the Number
    input_entry = Entry(main_frame, font=("Arial", 16))
    input_entry.pack(pady=10)

    submit_button = Button(
        main_frame, text="Submit Guess", command=submit_guess,
        bg="#1C2A3A", fg="white", font=("Arial", 16)
    )
    submit_button.pack(pady=10)

    result_label = Label(main_frame, text="", font=("Arial", 14), bg="#0B0F1D", fg="white")
    result_label.pack(pady=10)


def show_games():
    verwijderen_main_frame()
    label = Label(main_frame, text="Games", bg="#0B0F1D", fg="white", font=("Arial", 20))
    label.pack(pady=10)
    hangman_button = Button(
        main_frame,
        text="Play Hangman",
        command=play_hangman,
        bg="#1C2A3A",
        fg="white",
        font=("Arial", 16),
        padx=10,
        pady=10,
        relief="flat"
    )
    hangman_button.pack(pady=10)
    guess_number_button = Button(
        main_frame,
        text="Play Guess the Number",
        command=play_guess_number,
        bg="#1C2A3A",
        fg="white",
        font=("Arial", 16),
        padx=10,
        pady=10,
        relief="flat"
    )
    guess_number_button.pack(pady=10)


def show_friends():
    verwijderen_main_frame()
    label = Label(main_frame, text="Friends List", bg="#0B0F1D", fg="white", font=("Arial", 20))
    label.pack(pady=10)

def show_configurations():
    verwijderen_main_frame()
    label = Label(main_frame, text="Settings", bg="#0B0F1D", fg="white", font=("Arial", 20))
    label.pack(pady=10)

root = Tk()
root.title("Steam Dashboard")
root.geometry("800x600")

top_menu = Frame(root, bg="#0A0E1A", height=50)
top_menu.pack(fill="x")

button_style = {
    'bg': "#1C2A3A",
    'fg': "white",
    'padx': 20,
    'pady': 10,
    'borderwidth': 0,
    'activebackground': "#3A506B",
    'relief': "flat"
}

games_button = Button(top_menu, text="Games", command=show_games, **button_style)
games_button.pack(side="left", padx=5, pady=5)

friends_button = Button(top_menu, text="Friends", command=show_friends, **button_style)
friends_button.pack(side="left", padx=5, pady=5)

config_button = Button(top_menu, text="Settings", command=show_configurations, **button_style)
config_button.pack(side="left", padx=5, pady=5)

main_frame = Frame(root, bg="#0B0F1D")
main_frame.pack(fill="both", expand=True)

show_games()

root.geometry("1920x1080")
root.mainloop()