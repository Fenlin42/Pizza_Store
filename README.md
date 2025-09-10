# 🍕 Pizza Store

#Ein interaktives Python-Programm zur Verwaltung einer Pizzakarte.
#Erstellt als Projekt für das Modul *Anwendungsentwicklung mit Python.

## Start
```bash
python -m src.ui.userstory

"""
✨ Funktionen

Alle Pizzen anzeigen

Nach Belägen suchen (z. B. Eingabe Schinken Ananas → zeigt Hawai)

Pizza nach Namen auswählen und Preis anzeigen

Mit Gutscheincode PIZZA10 → 10 % Rabatt

Bei falschem Code → Hinweis „Ungültiger Gutscheincode“

Beenden

🧪 Testeingaben

Menüpunkt 1: Alle Pizzen anzeigen
- Erwartung: Liste aller 4 Pizzen mit Namen, Belägen und Preisen.

Menüpunkt 2: Nach Belägen suchen
- Eingabe: `Schinken Ananas`  
  → Erwartung: Pizza *Hawai*  
- Eingabe: `Banane`  
  → Erwartung: "Keine Treffer."

Menüpunkt 3: Pizza wählen & Preis anzeigen
- Eingabe: `Hawai`, Gutscheincode: `PIZZA10`  
  → Erwartung: Rabatt, Preis = 16.20 CHF  
- Eingabe: `Hawai`, Gutscheincode: `FALSCH`  
  → Erwartung: Hinweis "Ungültiger Gutscheincode – normaler Preis wird berechnet."  
- Eingabe: `Hawai`, Gutscheincode leer (Enter)  
  → Erwartung: Normaler Preis 18.00 CHF

Menüpunkt 0: Beenden
- Erwartung: Programm gibt "Tschüss 👋" aus und stoppt.


🗂️ Projektstruktur

src/model/pizza.py → Pizza-Klasse (Attribute, Rabattlogik, str)

src/database/fake_db.py → Fake-Datenbank mit vordefinierten Pizzen

src/data_access/repository.py → Zugriff auf Pizzaliste (suchen, filtern)

src/business_logic/service.py → Eingaben verarbeiten, Preise berechnen, Ausgabe formatieren

src/ui/userstory.py → Benutzeroberfläche (CLI-Menü)

📦 Anforderungen

Python 3.10+ (keine externen Libraries notwendig)

📹 Abgabe

GitHub-Link: [https://github.com/Fenlin42/Pizza_Store]

Video-Link:[https://tube.switch.ch/videos/YEk23hP1r4]
""""""
