import data_handle as dataHandle
import scanner_handle as scannerHandle



def main():
    while True:
        print("1. Produkt anlegen")
        print("2. Produkt bearbeiten")
        print("3. Produkt löschen")
        print("4. Produkt anzeigen")
        print("5. Item anlegen")
        print("6. Item bearbeiten")
        print("7. Item löschen")
        print("8. Item anzeigen")
        print("9. Beenden")

        choice = input("Auswahl: ")

        if choice == "1":
            createProduct()

def createProduct():
    name = input("Name: ")
    barcode = input("Barcode: ")
    barcode_type = scannerHandle.getBarcodeType(barcode)
    weigth = input("Gewicht: ")
    width = input("Breite: ")
    height = input("Höhe: ")
    depth = input("Tiefe: ")
    manufacturer = input("Hersteller: ")
    category = input("Kategorie: ")
    packaging = input("Verpackung: ")
    amount = input("Menge: ")
    amount_unit = input("Mengeneinheit: ")
    description = input("Beschreibung: ")


    dataHandle.addProduct(barcode, barcode_type, name, weigth, width, height, depth, manufacturer, category, packaging, amount, amount_unit, description)

    print(f"Das Produkt {name} wurde unter {barcode} angelegt.")

def createItem():
    barcode = input("Barcode: ")
    if scannerHandle.isOfficial(barcode):
        pass
    else:
        print("Du hast einen internen Code gescannt, der Bereits einem Item zugewiesen ist.")
        print("Bitte scanne einen offiziellen Code, wie z.B. einen EAN-Code.")
        return
    
        

if __name__ == "__main__":
    main()