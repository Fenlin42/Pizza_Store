from src.data_access.repository import get_all_pizzas, find_by_name, find_by_toppings



def main():

    while True:
        print("\n=== Pizza Store ===")
        print("1) Alle Pizzen anzeigen")
        print("2) Nach Belägen suchen")
        print("3) Pizza wählen & Preis anzeigen (ohne Rabattlogik)")
        print("0) Beenden")
        choice = input("> ").strip()

        if choice == "1":
            for p in get_all_pizzas():
                print(p)

        elif choice == "2":
            text = input("Beläge (durch Leerzeichen trennen): ")
            words = text.split()
            result = find_by_toppings(words)
            for p in result:
                print(p)

        elif choice == "0":
            print("Tschüss 👋")
            break

        else:
            print("Ungültige Eingabe.")

if __name__ == "__main__":
    main()
