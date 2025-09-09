from src.data_access.repository import get_all_pizzas, find_by_name, find_by_toppings

def main():
    while True:
        print("\n=== Fenlins Pizza Store ===")
        print("1) Alle Pizzen anzeigen")
        print("2) Nach Belägen suchen")
        print("3) Pizza wählen & Preis anzeigen (ohne Rabattlogik)")
        print("0) Beenden")
        choice = input("> ").strip()

        if choice == "1":
            # Alle Pizzen anzeigen
            for p in get_all_pizzas():
                print(p)

        elif choice == "2":
            # Pizzen nach Belägen suchen
            text = input("Beläge (durch Leerzeichen trennen): ")
            words = text.split()  # User-Input in Liste zerlegen
            result = find_by_toppings(words)
            if result:
                for p in result:
                    print(p)
            else:
                print("Keine Pizza mit diesen Belägen gefunden.")



        elif choice == "3":
            name = input("Pizza-Name: ")
            pizza = find_by_name(name)
            if pizza:
                code = input("Gutscheincode (Enter für keinen): ").strip()
                preis = pizza.price_with_code(code)
                # Rabatt angewendet?
                if code and preis == pizza.price:
                    print("Ungültiger Gutscheincode – normaler Preis wird berechnet.")
                print(pizza, "Preis:", f"{preis:.2f} CHF")

            else:

                print("Pizza nicht gefunden.")


        elif choice == "0":
            print("Tschüss 👋")
            break

        else:
            print("Ungültige Eingabe.")

if __name__ == "__main__":
    main()
