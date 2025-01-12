import customtkinter
from PIL import Image
from raadnummer import play_guess_number
from galgje import play_hangman
import json
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("1920x1080")
root.title("Steam App")

VALID_USERNAMES = {"Marvin", "Levi", "Mashal", "Abdullah"}
VALID_PASSWORD = "pixelpros123"

current_user = None
main_frame = None

def clear_main_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

def logout():
    global current_user
    current_user = None
    for widget in root.winfo_children():
        widget.destroy()
    create_login_page()

def show_mvp_games():
    def apply_filter():
        selected_filter = filter_dropdown.get()
        key_mapping = {
            "Name": "name",
            "Price": "price",
            "Owners": "owners",
            "Positive Ratings": "positive_ratings",
            "Negative Ratings": "negative_ratings",
        }
        key = key_mapping.get(selected_filter, "name")

        try:
            if key == "owners":
                sorted_games = sorted(games_data, key=lambda x: int(x[key].split(" - ")[0]))
            else:
                sorted_games = sorted(games_data, key=lambda x: x.get(key, 0))
        except Exception as e:
            print(f"Error during sorting: {e}")
            sorted_games = games_data

        display_games(sorted_games)

    def display_games(games):
        """
        Clears the current game display and shows games in the given order.
        """
        for widget in main_frame.winfo_children():
            widget.destroy()

        # Re-add the title and filter UI
        title_label = customtkinter.CTkLabel(
            main_frame, text="MVP Games", font=("Helvetica", 20, "bold")
        )
        title_label.pack(pady=10)

        filter_frame.pack(fill="x", padx=10, pady=5)

        # Add game entries
        for game in games[:50]:  # Display only the first 50 games
            game_frame = customtkinter.CTkFrame(main_frame, corner_radius=10)
            game_frame.pack(fill="x", padx=10, pady=5)

            title = game.get("name", "Unknown Game")
            price = game.get("price", "Unknown Price")
            genres = game.get("genres", "Unknown Genres")
            positive_ratings = game.get("positive_ratings", 0)
            negative_ratings = game.get("negative_ratings", 0)

            title_label = customtkinter.CTkLabel(
                game_frame, text=f"Name: {title}", font=("Helvetica", 14, "bold")
            )
            title_label.pack(anchor="w", padx=10, pady=2)

            price_label = customtkinter.CTkLabel(
                game_frame, text=f"Price: ${price:.2f}", font=("Helvetica", 12)
            )
            price_label.pack(anchor="w", padx=10, pady=2)

            genres_label = customtkinter.CTkLabel(
                game_frame, text=f"Genres: {genres}", font=("Helvetica", 12)
            )
            genres_label.pack(anchor="w", padx=10, pady=2)

            ratings_label = customtkinter.CTkLabel(
                game_frame,
                text=f"Ratings: {positive_ratings} Positive, {negative_ratings} Negative",
                font=("Helvetica", 12),
            )
            ratings_label.pack(anchor="w", padx=10, pady=2)
    clear_main_frame()
    file = open("steam.json", "r")
    games_data = json.load(file)
    file.close()
    title_label = customtkinter.CTkLabel(
        main_frame, text="MVP Games", font=("Helvetica", 20, "bold")
    )
    title_label.pack(pady=10)

    for game in games_data[:50]:
        game_frame = customtkinter.CTkFrame(main_frame, corner_radius=10)
        game_frame.pack(fill="x", padx=10, pady=5)

        title = game.get("name", "Unknown Game")
        price = game.get("price", "Unknown Price")
        genres = game.get("genres", "Unknown Genres")

        title_label = customtkinter.CTkLabel(
            game_frame, text=f"Name: {title}", font=("Helvetica", 14, "bold")
        )
        title_label.pack(anchor="w", padx=10, pady=2)

        price_label = customtkinter.CTkLabel(
            game_frame, text=f"Price: ${price:.2f}", font=("Helvetica", 12)
        )
        price_label.pack(anchor="w", padx=10, pady=2)

        genres_label = customtkinter.CTkLabel(
            game_frame, text=f"Genres: {genres}", font=("Helvetica", 12)
        )
        genres_label.pack(anchor="w", padx=10, pady=2)

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

def toggle_mode():
    mode = "dark"
    if mode == "dark":
        mode = "light"
        customtkinter.set_appearance_mode(mode)
    if mode == "light":
        mode = "dark"
        customtkinter.set_appearance_mode(mode)

def show_settings():
    clear_main_frame()
    toggle_button = customtkinter.CTkButton(

        main_frame,
        text="Toggle Light mode",
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

def show_games():
    clear_main_frame()  # Clear the current frame content
    label = customtkinter.CTkLabel(
        main_frame,
        text="Games",
        font=("Helvetica", 30, "bold")
    )
    label.pack(pady=10)

    hangman_button = customtkinter.CTkButton(
        main_frame,
        text="Play Hangman",
        command=lambda: play_hangman(main_frame)  # Pass main_frame
    )
    hangman_button.pack(pady=10)

    guess_number_button = customtkinter.CTkButton(
        main_frame,
        text="Play Guess the Number",
        command=lambda: play_guess_number(main_frame)  # Pass main_frame
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

    mvp_button = customtkinter.CTkButton(
        top_menu,
        text="MVP Games",
        command=show_mvp_games,
        corner_radius=10,
        height=70,
        font=("Helvetica", 20, "bold")
    )
    mvp_button.pack(side="left", padx=10, pady=10)

    games_button = customtkinter.CTkButton(
        top_menu,
        text="Nano Games (L)",
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

    show_mvp_games()

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

    steam_image = customtkinter.CTkImage(
        light_image=Image.open("steamlogo.png"),
        dark_image=Image.open("steamlogo.png"),
        size=(100, 100)
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
