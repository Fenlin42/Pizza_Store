# Pizza- Klasse
#Attribute:
#name
#toppings
#price
#METHODEN
#price_with_discount

class Pizza:
    def __init__(self, name, toppings, price):
        # Name: strip() (Leerzeichen entfernen)
        self.name = name.strip()
        if not self.name:
            raise ValueError("Name darf nicht leer sein")

        # Toppings: isistance: kontrolliert ob es eine liste ist & (kleinbuchstaben, Leerstrings raus)
        if not isinstance(toppings, list):
            raise ValueError("Toppings müssen eine Liste sein")
        self.toppings = [t.strip().lower() for t in toppings if t.strip()]

        # Preis: in float umwandeln und prüfen
        self.price = float(price)
        if self.price <= 0:
            raise ValueError("Preis muss größer als 0 sein")


#Methoden

def price_with_code(self, code)
    discount_code = code.strip().upper()
    if discount_code == "PIZZA10":
        return round(self.price * 0.9, 2)
    return self.price

#preis_mit_rabatt


#


