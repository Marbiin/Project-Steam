import customtkinter
import random
from PIL import Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("1920x1080")
root.title("Steam App")

VALID_USERNAMES = {"Marvin", "Levi", "Mashal", "Abdullah"}
VALID_PASSWORD = "pixelpros123"

galgje_state = {}
raadnummer_state = {}

current_user = None
main_frame = None

def toggle_mode():
    current_mode = customtkinter.get_appearance_mode()
    new_mode = "light" if current_mode == "dark" else "dark"
    customtkinter.set_appearance_mode(new_mode)

def clear_main_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

def logout():
    global current_user
    current_user = None
    for widget in root.winfo_children():
        widget.destroy()
    create_login_page()

def show_friends():
    clear_main_frame()

    profile_image = customtkinter.CTkImage(
        dark_image=Image.open("pfpicon.jpg"),
        size=(30, 30)
    )

    label = customtkinter.CTkLabel(
        main_frame,
        text="Friends List",
        font=("Helvetica", 30, "bold")
    )
    label.pack(pady=10)

    friends = [user for user in VALID_USERNAMES if user != current_user]
    for friend in friends:
        friend_frame = customtkinter.CTkFrame(master=main_frame, fg_color="transparent")
        friend_frame.pack(pady=5, padx=20, anchor="w")

        friend_icon_label = customtkinter.CTkLabel(
            friend_frame,
            image=profile_image,
            text=""
        )
        friend_icon_label.pack(side="left", padx=5)

        friend_label = customtkinter.CTkLabel(
            friend_frame,
            text=friend,
            font=("Arial", 18)
        )
        friend_label.pack(side="left", padx=10)

def show_settings():
    clear_main_frame()
    toggle_button = customtkinter.CTkButton(
        main_frame,
        text="Toggle Light/Dark Mode",
        command=toggle_mode,
        corner_radius=10
    )
    toggle_button.pack(pady=20)
    logout_button = customtkinter.CTkButton(
        main_frame,
        text="Log Out",
        command=logout,
        corner_radius=10
    )
    logout_button.pack(pady=20)

def play_hangman():
    global galgje_state
    clear_main_frame()

    woordenlijst = ["telefoon", "water", "continent", "laptop", "python", "alfabet"]
    woord_te_raden = random.choice(woordenlijst)
    galgje_state = {
        "woord": woord_te_raden,
        "geraden_woord": ["_"] * len(woord_te_raden),
        "fouten": 0,
        "max_fouten": 6
    }

    canvas = customtkinter.CTkCanvas(main_frame, width=300, height=400, bg="#0B0F1D", highlightthickness=0)
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

    word_label = customtkinter.CTkLabel(main_frame, text=" ".join(galgje_state["geraden_woord"]), font=("Courier", 18))
    word_label.pack(pady=20)

    input_entry = customtkinter.CTkEntry(main_frame, placeholder_text="Enter a letter")
    input_entry.pack(pady=10)

    submit_button = customtkinter.CTkButton(main_frame, text="Submit Letter", command=submit_letter)
    submit_button.pack(pady=10)

    result_label = customtkinter.CTkLabel(main_frame, text="", font=("Arial", 14))
    result_label.pack(pady=10)

def play_guess_number():
    global raadnummer_state
    clear_main_frame()

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

    input_entry = customtkinter.CTkEntry(main_frame, placeholder_text="Enter your guess")
    input_entry.pack(pady=10)

    submit_button = customtkinter.CTkButton(main_frame, text="Submit Guess", command=submit_guess)
    submit_button.pack(pady=10)

    result_label = customtkinter.CTkLabel(main_frame, text="", font=("Arial", 14))
    result_label.pack(pady=10)

def show_games():
    clear_main_frame()
    label = customtkinter.CTkLabel(
        main_frame,
        text="Games",
        font=("Helvetica", 30, "bold")
    )
    label.pack(pady=10)
    hangman_button = customtkinter.CTkButton(
        main_frame,
        text="Play Hangman",
        command=play_hangman
    )
    hangman_button.pack(pady=10)
    guess_number_button = customtkinter.CTkButton(
        main_frame,
        text="Play Guess the Number",
        command=play_guess_number
    )
    guess_number_button.pack(pady=10)

def create_dashboard():
    global main_frame
    top_menu = customtkinter.CTkFrame(master=root, height=100)
    top_menu.pack(fill="x")

    profile_image = customtkinter.CTkImage(
        dark_image=Image.open("pfpicon.jpg"),
        size=(30, 30)
    )
    profile_frame = customtkinter.CTkFrame(master=top_menu, fg_color="transparent")
    profile_frame.pack(side="right", padx=10)

    profile_icon_label = customtkinter.CTkLabel(
        profile_frame,
        image=profile_image,
        text=""
    )
    profile_icon_label.pack(side="left", padx=5)

    profile_label = customtkinter.CTkLabel(
        profile_frame,
        text=current_user,
        font=("Arial", 16)
    )
    profile_label.pack(side="left", padx=5)

    main_frame = customtkinter.CTkFrame(master=root)
    main_frame.pack(fill="both", expand=True)

    games_button = customtkinter.CTkButton(
        top_menu,
        text="Games",
        command=show_games,
        corner_radius=10,
        height=70,
        font=("Helvetica", 20, "bold")
    )
    games_button.pack(side="left", padx=10, pady=10)

    friends_button = customtkinter.CTkButton(
        top_menu,
        text="Friends",
        command=show_friends,
        corner_radius=10,
        height=70,
        font=("Helvetica", 20, "bold")
    )
    friends_button.pack(side="left", padx=10, pady=10)

    settings_button = customtkinter.CTkButton(
        top_menu,
        text="Settings",
        command=show_settings,
        corner_radius=10,
        height=70,
        font=("Helvetica", 20, "bold")
    )
    settings_button.pack(side="left", padx=10, pady=10)

    show_games()

def login():
    username = entry1.get()
    password = entry2.get()

    if username in VALID_USERNAMES and password == VALID_PASSWORD:
        global current_user
        current_user = username

        for widget in root.winfo_children():
            widget.destroy()

        create_dashboard()
    else:
        error_label.configure(text="Invalid username or password!", text_color="red")

def show_forgot_password_popup():
    popup = customtkinter.CTkToplevel(root)
    popup.geometry("400x200")
    popup.title("Forgot Password")
    popup.transient(root)
    popup.grab_set()

    popup_label = customtkinter.CTkLabel(
        popup,
        text="Usernames: Levi, Mashal, Marvin & Abdullah\nPassword: pixelpros123",
        font=("Arial", 14),
        justify="center"
    )
    popup_label.pack(expand=True, padx=20, pady=20)

    ok_button = customtkinter.CTkButton(
        popup,
        text="OK",
        command=popup.destroy
    )
    ok_button.pack(pady=20)
    popup.wait_window()

def create_login_page():
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    # Load and display the Steam logo above the header
    steam_image = customtkinter.CTkImage(
        light_image=Image.open("steamlogo.png"),  # Ensure the path is correct
        dark_image=Image.open("steamlogo.png"),
        size=(100, 100)  # Adjust the size as needed
    )
    logo_label = customtkinter.CTkLabel(master=frame, image=steam_image, text="")
    logo_label.pack(pady=(20, 10))

    header_label = customtkinter.CTkLabel(
        master=frame,
        text="Steam",
        font=("Helvetica", 50, "bold")
    )
    header_label.pack(pady=(10, 20))

    global entry1, entry2, error_label
    entry1 = customtkinter.CTkEntry(
        master=frame,
        placeholder_text="Username"
    )
    entry1.pack(pady=12, padx=10)

    entry2 = customtkinter.CTkEntry(
        master=frame,
        placeholder_text="Password",
        show="*"
    )
    entry2.pack(pady=12, padx=10)

    button = customtkinter.CTkButton(
        master=frame,
        text="Login",
        command=login
    )
    button.pack(pady=12, padx=10)

    checkbox_frame = customtkinter.CTkFrame(master=frame, fg_color="transparent")
    checkbox_frame.pack(pady=10, fill="x")

    checkbox = customtkinter.CTkCheckBox(
        master=checkbox_frame,
        text="Remember Me"
    )
    checkbox.pack(side="left", padx=(700, 0))

    forgot_password = customtkinter.CTkLabel(
        master=checkbox_frame,
        text="Forgot password?",
        font=("Arial", 12, "underline"),
        text_color="#A0A0A0",
        cursor="hand2"
    )
    forgot_password.pack(side="right", padx=(0, 700))
    forgot_password.bind("<Button-1>", lambda e: show_forgot_password_popup())

    error_label = customtkinter.CTkLabel(
        master=frame,
        text="",
        font=("Arial", 12)
    )
    error_label.pack(pady=12)

create_login_page()
root.mainloop()