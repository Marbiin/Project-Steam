import random
from customtkinter import CTkLabel, CTkEntry, CTkButton

def play_guess_number(main_frame):
    for widget in main_frame.winfo_children():
        widget.destroy()
    raadnummer_state = {
        "nummer": random.randint(1, 20),
        "pogingen": 0,
        "max_pogingen": 5
    }

    def submit_guess():
        guess = input_entry.get().strip()
        input_entry.delete(0, 'end')

        if not guess.isdigit():
            result_label.configure(text="Enter a valid number.")
            return

        guess = int(guess)
        raadnummer_state["pogingen"] += 1

        if guess < raadnummer_state["nummer"]:
            result_label.configure(text="Higher!")
        elif guess > raadnummer_state["nummer"]:
            result_label.configure(text="Lower!")
        else:
            result_label.configure(text=f"Correct! The number was {raadnummer_state['nummer']}.")
            submit_button.configure(state="disabled")
            return

        if raadnummer_state["pogingen"] >= raadnummer_state["max_pogingen"]:
            raadnummer_state["nummer"] = random.randint(1, 20)
            raadnummer_state["pogingen"] = 0
            result_label.configure(text="Out of tries! The number has been reset.")

    input_entry = CTkEntry(main_frame, placeholder_text="Enter your guess")
    input_entry.pack(pady=10)

    submit_button = CTkButton(main_frame, text="Submit Guess", command=submit_guess)
    submit_button.pack(pady=10)

    result_label = CTkLabel(main_frame, text="", font=("Arial", 14))
    result_label.pack(pady=10)
