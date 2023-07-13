import database as DB

db = DB.Database("ean")

def addProduct(barcode: str, barcode_type: str, name: str, weigth: int, width: int, height: int, depth:int , manufacturer: str, category: str, packaging: str, amount: int, amount_unit: str, description="") -> None:
    """Fügt ein neues Produkt zur Datenbank hinzu."""
    
    # Erstellt ein neues Produkt-Objekt
    product_data = {
        "barcode": barcode,
        "barcode_type": barcode_type,
        "name": name,
        "weigth": weigth,
        "size": {
            "width": width,
            "height": height,
            "depth": depth
        },
        "manufacturer": manufacturer,
        "category": category,
        "packaging": packaging,
        "amount": amount,
        "amount_unit": amount_unit,
        "description": description
    }

    # Fügt das Produkt zur Datenbank hinzu
    db.set(barcode, product_data)

    
    
    

def addItem(barcode: str, price: float, buyplace: str, buydate, mhd: str, ) -> int:
    """Fügt ein neues Item zur Datenbank hinzu.
    
    Returns:
        int: Die ID des Items
    """
    

   