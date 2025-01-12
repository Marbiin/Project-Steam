import random
from customtkinter import CTkLabel, CTkEntry, CTkButton, CTkCanvas

def play_hangman(main_frame):
    for widget in main_frame.winfo_children():
        widget.destroy()

    woordenlijst = ["telefoon", "water", "continent", "laptop", "python", "alfabet"]
    woord_te_raden = random.choice(woordenlijst)
    galgje_state = {
        "woord": woord_te_raden,
        "geraden_woord": ["_"] * len(woord_te_raden),
        "fouten": 0,
        "max_fouten": 6
    }

    canvas = CTkCanvas(main_frame, width=300, height=400, bg="#0B0F1D", highlightthickness=0)
    canvas.pack(pady=20)

    canvas.create_line(50, 350, 250, 350, fill="white", width=3)
    canvas.create_line(150, 350, 150, 50, fill="white", width=3)
    canvas.create_line(150, 50, 200, 50, fill="white", width=3)
    canvas.create_line(200, 50, 200, 100, fill="white", width=3)

    def draw_stickman():
        parts = [
            lambda: canvas.create_oval(180, 100, 220, 140, outline="white", width=3),
            lambda: canvas.create_line(200, 140, 200, 220, fill="white", width=3),
            lambda: canvas.create_line(200, 220, 170, 260, fill="white", width=3),
            lambda: canvas.create_line(200, 220, 230, 260, fill="white", width=3),
            lambda: canvas.create_line(200, 160, 170, 200, fill="white", width=3),
            lambda: canvas.create_line(200, 160, 230, 200, fill="white", width=3),
        ]
        if galgje_state["fouten"] <= len(parts):
            parts[galgje_state["fouten"] - 1]()

    def submit_letter():
        letter = input_entry.get().strip().lower()
        input_entry.delete(0, 'end')

        if letter in galgje_state["woord"]:
            for i, char in enumerate(galgje_state["woord"]):
                if char == letter:
                    galgje_state["geraden_woord"][i] = letter
            result_label.configure(text="Good job!")
        else:
            galgje_state["fouten"] += 1
            draw_stickman()
            result_label.configure(text=f"Wrong! {galgje_state['max_fouten'] - galgje_state['fouten']} tries left.")

        word_label.configure(text=" ".join(galgje_state["geraden_woord"]))

        if "_" not in galgje_state["geraden_woord"]:
            result_label.configure(text=f"You won! The word was '{galgje_state['woord']}'.")
            submit_button.configure(state="disabled")
        elif galgje_state["fouten"] >= galgje_state["max_fouten"]:
            result_label.configure(text=f"You lost! The word was '{galgje_state['woord']}'.")
            submit_button.configure(state="disabled")

    word_label = CTkLabel(main_frame, text=" ".join(galgje_state["geraden_woord"]), font=("Courier", 18))
    word_label.pack(pady=20)

    input_entry = CTkEntry(main_frame, placeholder_text="Enter a letter")
    input_entry.pack(pady=10)

    submit_button = CTkButton(main_frame, text="Submit Letter", command=submit_letter)
    submit_button.pack(pady=10)

    result_label = CTkLabel(main_frame, text="", font=("Arial", 14))
    result_label.pack(pady=10)
