import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Header(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
    # Create the header card.
        header_card = tk.Frame(
            self,
            bg="white",
            highlightbackground="#dddddd",
            highlightthickness=1
        )
        header_card.pack(fill="x", padx=30, pady=(20, 10))

        header_card.columnconfigure(0, weight=1)
        header_card.columnconfigure(1, weight=1)
        header_card.columnconfigure(2, weight=1)

        # Left section: logo and title.
        left = tk.Frame(header_card, bg="white")
        left.grid(row=0, column=0, sticky="w", padx=20, pady=10)

        image = Image.open("Assets/logo.png")
        image = image.resize((60, 60))
        self.logo_image = ImageTk.PhotoImage(image)

        tk.Label(
            left,
            image=self.logo_image,
            bg="white"
        ).pack(side="left", padx=(0, 10))

        tk.Label(
            left,
            text="Expense Tracker",
            bg="white",
            fg="#222222",
            font=("URW Chancery L", 18, "bold")
        ).pack(side="left")

        # Center tagline.
        tk.Label(
            header_card,
            text="Track your every expenses",
            bg="white",
            fg="#777777",
            font=("URW Chancery L", 18)
        ).grid(row=0, column=1, pady=15)