import customtkinter
from PIL import Image
from raadnummer import play_guess_number
from galgje import play_hangman
import json

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("1920x1080")
root.title("Steam App")

VALID_USERNAMES = {"Levi", "Abdullah"}
VALID_PASSWORD = "pixelpros123"
mode = "dark"

def clear_main_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

def show_health_warning():
    popup = customtkinter.CTkToplevel(root)
    popup.geometry("400x200")
    popup.title("Health Warning")
    popup.transient(root)
    popup.grab_set()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 400
    window_height = 200
    position_x = (screen_width - window_width) // 2
    position_y = (screen_height - window_height) // 2
    popup.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

    warning_label = customtkinter.CTkLabel(
        popup,
        text="You've been in front of the screen for over 15 minutes.\nConsider taking a break for your own health!",
        font=("Arial", 14),
        justify="center"
    )
    warning_label.pack(expand=True, padx=20, pady=20)

    ok_button = customtkinter.CTkButton(
        popup,
        text="OK",
        command=popup.destroy
    )
    ok_button.pack(pady=20)
    popup.wait_window()

def show_mvp_games():
    clear_main_frame()

    file = open("steam.json", "r")
    games_data = json.load(file)
    file.close()

    games_per_page = 50
    total_pages = (len(games_data) + games_per_page - 1) // games_per_page
    current_page = [1]
    current_sort = ["Alphabetical Order"]

    def load_page(page, sort_by):
        current_page[0] = page
        current_sort[0] = sort_by

        if sort_by == "Owners":
            sorted_games = sorted(games_data, key=lambda x: x.get("owners", 0), reverse=True)
        elif sort_by == "Release Date":
            sorted_games = sorted(games_data, key=lambda x: x.get("release_date", ""), reverse=True)
        else:
            sorted_games = sorted(
                [game for game in games_data if game.get("name", "").lower().startswith("a")],
                key=lambda x: x.get("name", "").lower()
            )

        clear_main_frame()

        title_label = customtkinter.CTkLabel(
            main_frame, text="MVP Games", font=("Helvetica", 20, "bold")
        )
        title_label.pack(pady=10)

        filter_frame = customtkinter.CTkFrame(main_frame)
        filter_frame.pack(fill="x", pady=10, padx=10)

        sort_label = customtkinter.CTkLabel(
            filter_frame, text="Filter by:", font=("Helvetica", 14)
        )
        sort_label.pack(side="left", padx=5)

        sort_options = ["Alphabetical Order", "Owners", "Release Date"]
        sort_dropdown = customtkinter.CTkOptionMenu(
            filter_frame,
            values=sort_options,
            command=lambda choice: load_page(1, choice)
        )
        sort_dropdown.set(current_sort[0])
        sort_dropdown.pack(side="right", padx=5)

        scrollable_frame = customtkinter.CTkScrollableFrame(master=main_frame)
        scrollable_frame.pack(fill="both", expand=True, padx=10, pady=5)

        start_index = (page - 1) * games_per_page
        end_index = start_index + games_per_page

        for game in sorted_games[start_index:end_index]:
            game_frame = customtkinter.CTkFrame(scrollable_frame, corner_radius=10)
            game_frame.pack(fill="x", padx=10, pady=5)

            title = game.get("name")
            price = game.get("price")
            genres = game.get("genres")
            owners = game.get("owners")
            release_date = game.get("release_date")

            title_label = customtkinter.CTkLabel(
                game_frame, text=f"{title}", font=("Helvetica", 14, "bold")
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

            owners_label = customtkinter.CTkLabel(
                game_frame, text=f"Owners: {owners}", font=("Helvetica", 12)
            )
            owners_label.pack(anchor="w", padx=10, pady=2)

            release_date_label = customtkinter.CTkLabel(
                game_frame, text=f"Release Date: {release_date}", font=("Helvetica", 12)
            )
            release_date_label.pack(anchor="w", padx=10, pady=2)

        pagination_frame = customtkinter.CTkFrame(master=main_frame, fg_color="transparent")
        pagination_frame.pack(pady=10)

        if current_page[0] > 1:
            prev_button = customtkinter.CTkButton(
                pagination_frame,
                text="< Previous",
                command=lambda: load_page(current_page[0] - 1, current_sort[0])
            )
            prev_button.pack(side="left", padx=5)

        page_label = customtkinter.CTkLabel(
            pagination_frame,
            text=f"Page {current_page[0]} of {total_pages}",
            font=("Helvetica", 14)
        )
        page_label.pack(side="left", padx=10)

        if current_page[0] < total_pages:
            next_button = customtkinter.CTkButton(
                pagination_frame,
                text="Next >",
                command=lambda: load_page(current_page[0] + 1, current_sort[0])
            )
            next_button.pack(side="left", padx=5)
    load_page(current_page[0], current_sort[0])

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
    global mode
    if mode == "dark":
        mode = "light"
    else:
        mode = "dark"
    customtkinter.set_appearance_mode(mode)

def logout():
    for widget in root.winfo_children():
        widget.destroy()
    create_login_page()

def show_settings():
    clear_main_frame()
    toggle_button = customtkinter.CTkButton(
        main_frame,
        text="Toggle Light/Dark mode",
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
        command=lambda: play_hangman(main_frame)
    )
    hangman_button.pack(pady=10)

    guess_number_button = customtkinter.CTkButton(
        main_frame,
        text="Play Guess the Number",
        command=lambda: play_guess_number(main_frame)
    )
    guess_number_button.pack(pady=10)

def create_dashboard():
    global main_frame
    top_menu = customtkinter.CTkFrame(master=root, height=100)
    top_menu.pack(fill="x")
    middle_grey = "#404040"

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
        font=("Helvetica", 20, "bold"),
        fg_color=middle_grey
    )
    mvp_button.pack(side="left", padx=10, pady=10)

    games_button = customtkinter.CTkButton(
        top_menu,
        text="Nano Games (L)",
        command=show_games,
        corner_radius=10,
        height=70,
        font=("Helvetica", 20, "bold"),
        fg_color=middle_grey
    )
    games_button.pack(side="left", padx=10, pady=10)

    friends_button = customtkinter.CTkButton(
        top_menu,
        text="Friends",
        command=show_friends,
        corner_radius=10,
        height=70,
        font=("Helvetica", 20, "bold"),
        fg_color=middle_grey
    )
    friends_button.pack(side="left", padx=10, pady=10)

    settings_button = customtkinter.CTkButton(
        top_menu,
        text="Settings",
        command=show_settings,
        corner_radius=10,
        height=70,
        font=("Helvetica", 20, "bold"),
        fg_color=middle_grey
    )
    settings_button.pack(side="left", padx=10, pady=10)

    root.after(900000, show_health_warning)
    
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
