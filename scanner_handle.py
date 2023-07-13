def decode(code: str) -> tuple:
    """Dekodiert den Typ des Codes der gescannt wurde und gibt diesen zurück
    
    Args:
        code (str): Der gescannte Code
        
    Returns:
        tuple: Der Typ des Codes und ob dieser offiziell ist

        """
    if code.isdigit:
        if len(code) == 13:
            return "EAN13", "official"
        elif len(code) == 8:
            return "EAN8", "official"
        elif len(code) == 12:
            return "UPCA", "official"

    elif "DD" in code:
        return "DDLMS", "internal"
    
def getBarcodeType(code: str) -> str:
    """Gibt den Typ des Barcodes zurück.
    
    Args:
        code (str): Der gescannte Code
        
    Returns:
        str: Der Typ des Codes

        """
    return decode(code)[0]

def isOfficial(code: str) -> bool:
    """Gibt zurück, ob der gescannte Code offiziell ist.
    
    Args:
        code (str): Der gescannte Code
        
    Returns:
        bool: True, wenn der Code offiziell ist, sonst False

        """
    return decode(code)[1] == "official"

