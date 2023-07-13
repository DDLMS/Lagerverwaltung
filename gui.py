"""Frontend GUI welches durch tkinter realisiert wird. Bietet eine einfache Oberfläche zum Benutzen der Software."""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import scanner_handle as scanner
import data_handle as data

class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Donnjer Development Life Management System - Lagerverwaltung")
        #self.geometry("500x500")
        self.resizable(False, False)
        self.createFrames()
        self.createWidgets()

    def createFrames(self) -> None:
        self.mainframe = ttk.Frame(self)
        self.mainframe.pack(expand=True, fill="both")

        self.product_frame = ttk.Frame(self.mainframe)
        self.product_frame.grid(row=0, column=0, sticky="nsew")

        self.item_frame = ttk.Frame(self.mainframe)
        self.item_frame.grid(row=0, column=1, sticky="nsew")

        self.scan_frame = ttk.Frame(self.mainframe)
        self.scan_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")

    def createWidgets(self) -> None:
        self.createProductFrameWidgets()
        self.createItemFrameWidgets()
        self.createScanFrameWidgets()

    def createProductFrameWidgets(self) -> None:
        """Erstellt die Widgets für das Produkt Frame.
           Hier werden alle Metainformationen zu einem Produkt angezeigt.
           Die eigenrliche Lagerverwaltung findet in einem separaten Frame statt.
        """
        
        self.product_name_label = ttk.Label(self.product_frame, text="Produktname:")
        self.product_name_label.grid(row=0, column=0, sticky="e")

        self.product_name_entry = ttk.Entry(self.product_frame)
        self.product_name_entry.grid(row=0, column=1)

        self.product_weight_label = ttk.Label(self.product_frame, text="Gewicht:")
        self.product_weight_label.grid(row=1, column=0, sticky="e")

        self.product_weight_entry = ttk.Entry(self.product_frame)
        self.product_weight_entry.grid(row=1, column=1)

        self.product_size_label = ttk.Label(self.product_frame, text="Größe:")
        self.product_size_label.grid(row=2, column=0, sticky="e")

        self.product_size_entry = ttk.Entry(self.product_frame)
        self.product_size_entry.grid(row=2, column=1)

        self.product_manufacturer_label = ttk.Label(self.product_frame, text="Hersteller:")
        self.product_manufacturer_label.grid(row=3, column=0, sticky="e")

        self.product_manufacturer_entry = ttk.Entry(self.product_frame)
        self.product_manufacturer_entry.grid(row=3, column=1)

        self.product_category_label = ttk.Label(self.product_frame, text="Kategorie:")
        self.product_category_label.grid(row=4, column=0, sticky="e")

        self.product_category_entry = ttk.Entry(self.product_frame)
        self.product_category_entry.grid(row=4, column=1)

        self.product_packaging_label = ttk.Label(self.product_frame, text="Verpackung:")
        self.product_packaging_label.grid(row=5, column=0, sticky="e")

        self.product_packaging_entry = ttk.Entry(self.product_frame)
        self.product_packaging_entry.grid(row=5, column=1)

        self.product_description_label = ttk.Label(self.product_frame, text="Beschreibung:")
        self.product_description_label.grid(row=6, column=0, sticky="e")

        self.product_description_entry = ttk.Entry(self.product_frame)
        self.product_description_entry.grid(row=6, column=1)

        self.product_amount_label = ttk.Label(self.product_frame, text="Menge:")
        self.product_amount_label.grid(row=7, column=0, sticky="e")
        
        self.product_amount_entry = ttk.Entry(self.product_frame)
        self.product_amount_entry.grid(row=7, column=1)

        self.product_amount_unit_label = ttk.Label(self.product_frame, text="Einheit:")
        self.product_amount_unit_label.grid(row=8, column=0, sticky="e")

        self.product_amount_unit_entry = ttk.Entry(self.product_frame)
        self.product_amount_unit_entry.grid(row=8, column=1)


    def createItemFrameWidgets(self) -> None:
        """Erstellt die Widgets für das Item Frame.
           Hier werden alle Metainformationen zu einem Item im Lager angezeigt.
        """
        self.item_buy_date_label = ttk.Label(self.item_frame, text="Kaufdatum:")
        self.item_buy_date_label.grid(row=0, column=0, sticky="e")

        self.item_buy_date_entry = ttk.Entry(self.item_frame)
        self.item_buy_date_entry.grid(row=0, column=1)

        self.item_buy_price_label = ttk.Label(self.item_frame, text="Kaufpreis:")
        self.item_buy_price_label.grid(row=1, column=0, sticky="e")

        self.item_buy_price_entry = ttk.Entry(self.item_frame)
        self.item_buy_price_entry.grid(row=1, column=1)

        self.item_buy_place_label = ttk.Label(self.item_frame, text="Kaufort:")
        self.item_buy_place_label.grid(row=2, column=0, sticky="e")

        self.item_buy_place_entry = ttk.Entry(self.item_frame)
        self.item_buy_place_entry.grid(row=2, column=1)

        self.item_mhd_label = ttk.Label(self.item_frame, text="MHD:")
        self.item_mhd_label.grid(row=3, column=0, sticky="e")

        self.item_mhd_entry = ttk.Entry(self.item_frame)
        self.item_mhd_entry.grid(row=3, column=1)

    def createScanFrameWidgets(self) -> None:
        """Erstellt die Widgets für das Scan Frame.
           Hier wird die Scanfunktion angezeigt.
        """
        self.scan_label = ttk.Label(self.scan_frame, text="Scan:")
        self.scan_label.grid(row=0, column=0, sticky="e")

        self.scan_entry = ttk.Entry(self.scan_frame)
        self.scan_entry.grid(row=0, column=1)

        self.scan_button = ttk.Button(self.scan_frame, text="Bestätigen", command=self.scanButtonClicked)
        self.scan_button.grid(row=0, column=2)

    def scanButtonClicked(self) -> None:
        #Überprüfen ob der eingegebene Barcode gültig ist
        if scanner.isInternal(self.scan_entry.get()):
        else:
            if data.productExists(self.scan_entry.get()):
                self.product = data.getProduct(self.scan_entry.get())
                self.update_product_frame()
                self.update_item_frame()

if __name__ == "__main__":
    app = App()
    app.mainloop()