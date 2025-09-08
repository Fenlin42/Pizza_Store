# Pizza- Klasse
#Attribute:
#name
#toppings
#price
#METHODEN
#price_with_discount

class Pizza:
    def __init__(self, name, toppings, price):
        # Name: trimmen (Leerzeichen entfernen)
        self.name = name.strip()
        if not self.name:
            raise ValueError("Name darf nicht leer sein")

        # Toppings: Liste bereinigen (kleinbuchstaben, Leerstrings raus)
        if not isinstance(toppings, list):
            raise ValueError("Toppings müssen eine Liste sein")
        self.toppings = [t.strip().lower() for t in toppings if t.strip()]

        # Preis: in float umwandeln und prüfen
        self.price = float(price)
        if self.price <= 0:
            raise ValueError("Preis muss größer als 0 sein")




#alle_pizzen_liste
#pizza_eingegeben_belaegen
#pizza_eingegeben_name
#preis_mit_rabatt
#


