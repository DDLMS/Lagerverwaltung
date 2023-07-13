"""Eine einfache JSON Datenbank für die Speicherung der Daten."""

import json

class Database:
    def __init__(self, dbname):
        self.db = dbname
        self.setPath()
        self.test

    def test(self):
        try:
            self.read()
        except FileNotFoundError:
            self.data = {}
            self.write()

    def setPath(self):
        self.db = "backend/" + self.db + ".json"    
    
    def read(self):
        with open(self.db, "r") as f:
            self.data = json.load(f)
        
    def write(self):
        with open(self.db, "w") as f:
            json.dump(self.data, f, indent=4)

    def doExists(self, key):
        return key in self.data
    
    def get(self, key):
        return self.data[key]
    
    def set(self, key, value):
        self.data[key] = value
        self.write()

    def delete(self, key):
        del self.data[key]
        self.write()

    def getAll(self):
        return self.data
    
    def clear(self):
        self.data = {}
        self.write()