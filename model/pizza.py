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
    #discount "Pizza 10"
    def price_with_code(self, code: str) -> float:
        code_norm = str(code).strip().upper()
        if code_norm == "PIZZA10":
            return round(self.price * 0.9, 2)
        return self.price

    #damit es wie ein code rauskommt und nicht als code
    def __str__(self) -> str:
        toppings_str = ", ".join(self.toppings)
        return f"{self.name}: {toppings_str} – {self.price:.2f} CHF"


#


