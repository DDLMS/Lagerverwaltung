"""Frontend GUI welches durch tkinter realisiert wird. Bietet eine einfache Oberfläche zum Benutzen der Software."""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Donnjer Development Life Management System - Lagerverwaltung")
        #self.geometry("500x500")
        self.resizable(False, False)
        self.createFrames()
        self.createWidgets()
        

    def createFrames(self):
        self.product_frame = ttk.Frame(self)
        self.product_frame.grid(row=0, column=0, sticky="nsew")

    def createWidgets(self):
        self.createProductFrameWidgets()

    def createProductFrameWidgets(self) -> None:
        """
           Erstellt die Widgets für das Produkt Frame.
           Hier werden alle Metainformationen zu einem Produkt angezeigt.
           Die eigenrliche Lagerverwaltung findet in einem separaten Frame statt.
        """
        
        self.product_name_label = ttk.Label(self.product_frame, text="Produktname:")
        self.product_name_label.grid(row=0, column=0)

        self.product_name_entry = ttk.Entry(self.product_frame)
        self.product_name_entry.grid(row=0, column=1)

        self.product_weight_label = ttk.Label(self.product_frame, text="Gewicht:")
        self.product_weight_label.grid(row=1, column=0)

        self.product_weight_entry = ttk.Entry(self.product_frame)
        self.product_weight_entry.grid(row=1, column=1)

        self.product_size_label = ttk.Label(self.product_frame, text="Größe:")
        self.product_size_label.grid(row=2, column=0)

        self.product_size_entry = ttk.Entry(self.product_frame)
        self.product_size_entry.grid(row=2, column=1)

        self.product_manufacturer_label = ttk.Label(self.product_frame, text="Hersteller:")
        self.product_manufacturer_label.grid(row=3, column=0)

        self.product_manufacturer_entry = ttk.Entry(self.product_frame)
        self.product_manufacturer_entry.grid(row=3, column=1)

        self.product_category_label = ttk.Label(self.product_frame, text="Kategorie:")
        self.product_category_label.grid(row=4, column=0)

        self.product_category_entry = ttk.Entry(self.product_frame)
        self.product_category_entry.grid(row=4, column=1)

    




if __name__ == "__main__":
    app = App()
    app.mainloop()