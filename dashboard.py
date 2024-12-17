from tkinter import *

def som():
    getal1 = int(entry1.get())
    getal2 = int(entry2.get())
    som = getal1 + getal2
    label["text"] = f'De som van {getal1} + {getal2} is {som}'

def onclick():
    getal = int(entry1.get())
    kwadraat = getal * getal
    label["text"] = f'Het kwadraat van {getal} is {kwadraat}'

    # naam = entry1.get()
    # label["text"] = "Hallo " + naam
    # print("klik")

root = Tk()

label = Label(master = root, text = "Hallo")
label.pack(pady = 10)

button = Button(master = root, text = "klik", command = som)
button.pack(pady = 10)

entry1 = Entry(master = root)
entry1.pack(pady = 10, padx = 10)

entry2 = Entry(master = root)
entry2.pack(pady = 10, padx = 10)

root.geometry("600x300")
root.mainloop()