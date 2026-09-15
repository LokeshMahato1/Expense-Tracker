import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Header(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):

        #outer rectangle
        header_card=tk.Frame(
            self,
            bg="white",
            highlightbackground="#dddddd",
            highlightthickness=1,
        )
        header_card.pack(fill="x", padx=5, ipady=5)

        header_card.columnconfigure(0, weight=1)
        header_card.columnconfigure(1, weight=1)
        header_card.columnconfigure(2, weight=1)

        #logo
        image=Image.open("Assets/logo.png")
        image=image.resize((60,60))

        self.logo_image=ImageTk.PhotoImage(image)

        logo=tk.Label(header_card, image=self.logo_image, bg="white")
        logo.grid(row=0, column=0, padx=10, pady=10, sticky="w")


        #title
        title=tk.Label(header_card, text="Expense Tracker",bg="white", fg="#222222",
                         font=("Arial", 24, "bold"))
        title.grid(row=0, column=1,padx=10, pady=10, sticky="s")

        #tagline

        tagline=tk.Label(header_card, text="Spend • Plan • Save", bg="white", fg="#777777", font=("Arial", 12))
        tagline.grid(row=0, column=2, padx=5, pady=5,sticky="e")