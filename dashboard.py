from tkinter import *

def verwijderen_main_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

def show_games():
    verwijderen_main_frame()
    label = Label(main_frame, text="Games", bg="#0B0F1D", fg="white", font=("Arial", 20))
    label.pack(pady=10)
    # Create labels for each game in the Games view
    # for i in range(5):
    #     game_label = Label(main_frame, text=f"Game {i + 1}", bg="#1C2A3A", fg="white", font=("Arial", 16), padx=10,
    #                        pady=10)
    #     game_label.pack(pady=5, padx=10, fill="x")  # Position each game label with padding and fill the x-axis

def show_friends():
    verwijderen_main_frame()
    label = Label(main_frame, text="Friends List", bg="#0B0F1D", fg="white", font=("Arial", 20))
    label.pack(pady=10)
    # Create labels for each friend in the Friends view
    # for i in range(5):
    #     friend_label = Label(main_frame, text=f"Friend {i + 1}", bg="#1C2A3A", fg="white", font=("Arial", 16), padx=10,
    #                          pady=10)
    #     friend_label.pack(pady=5, padx=10, fill="x")  # Position each friend label with padding and fill the x-axis

def show_configurations():
    verwijderen_main_frame()
    label = Label(main_frame, text="Settings", bg="#0B0F1D", fg="white", font=("Arial", 20))
    label.pack(pady=10)
    # Create labels for each configuration option
    # for i in range(3):
    #     config_label = Label(main_frame, text=f"Option {i + 1}", bg="#1C2A3A", fg="white", font=("Arial", 16), padx=10,
    #                          pady=10)
    #     config_label.pack(pady=5, padx=10,
    #                       fill="x")  # Position each configuration label with padding and fill the x-axis

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
    'borderwidth': 10,
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

root.geometry("1920x1080")
root.mainloop()