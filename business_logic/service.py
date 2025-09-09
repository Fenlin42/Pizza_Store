from src.data_access.repository import (
    get_all_pizzas,
    find_by_name,
    find_by_toppings,
)

def transform_toppings_input(text: str) -> list[str]:

    #Wandelt den Rohtext des Benutzers in eine saubere Liste um.

    return [w.strip().casefold() for w in text.split() if w.strip()]

def search_pizzas_by_toppings_input(text: str):

    #Verarbeitet den User-Text und gibt die passenden Pizzen zurück.

    words = transform_toppings_input(text)
    return find_by_toppings(words)

def get_price_with_code(pizza_name: str, code: str):

    #Liefert den (evtl. rabattierten) Preis einer Pizza oder None, wenn sie nicht existiert.

    pizza = find_by_name(pizza_name)
    if not pizza:
        return None
    return pizza.price_with_code(code)

def format_pizza_list(pizzas) -> str:
    #Schöne Textausgabe für mehrere Pizzen.

    if not pizzas:
        return "Keine Treffer."
    return "\n".join(str(p) for p in pizzas)

def list_all_pizzas_text() -> str:

    #Holt alle Pizzen aus dem Repository und formatiert sie für die Ausgabe.

    return format_pizza_list(get_all_pizzas())

