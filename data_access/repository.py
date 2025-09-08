
from src.database.fake_db import pizzas

#alle_pizzen_liste :Gibt alle Pizzen zurück
def get_all_pizzas():
    return pizzas

#pizza_eingegeben_name : Sucht Pizza nach Name  und gibt Pizza objekt oder none zurück
def find_by_name(name: str):
    name_pizza = name.strip().lower()
    for pizza in pizzas:
        if pizza.name.lower() == name_pizza:
            return pizza
    return None

#pizza_eingegeben_belaegen sucht Pizzen,die ALLE angegebenen Beläge enthalten.
    #Gibt Liste von Pizzen zurück
def find_by_toppings(words: list[str]):
    words_norm = [w.strip().lower() for w in words if w.strip()] # w sind die einzelnen Objekte aus der Liste
    result = []
    for pizza in pizzas:
        toppings_norm = [t.casefold() for t in pizza.toppings]
        if all(w in toppings_norm for w in words_norm):
            result.append(pizza)
    return result

