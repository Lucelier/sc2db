import psycopg2
from rasse_enum import Rasse, rasse_mapping

# Verbindungsparameter
dbname = "Test"
user = "postgres"
password = "postgres"
host = "localhost"
port = "5432"

# Verbindung zur Datenbank herstellen
connection = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port=port
)

try:
    # Cursor (Konzept um Ergebnisse zu verwalten) erstellen
    cursor = connection.cursor()

    # Benutzer nach der gewünschten Rasse fragen
    rasse_input = input("Welche Rasse möchtest du anzeigen (Terraner, Zerg, Protoss)? ").strip().lower()

    # Funktion zur Überprüfung der Eingabe
    def get_valid_rasse(input_str, mapping):
        return mapping.get(input_str)


    # Überprüfen, ob die Eingabe in der Rasse-Mapping-Tabelle existiert
    selected_rasse = get_valid_rasse(rasse_input, rasse_mapping)

    if selected_rasse is not None:
        # Gültige Rasse gefunden, fortfahren
        if selected_rasse == Rasse.Terraner:
            rasse = 'Terraner'
        elif selected_rasse == Rasse.Zerg:
            rasse = 'Zerg'
        elif selected_rasse == Rasse.Protoss:
            rasse = 'Protoss'
        # ...
    else:
        print("Ungültige Eingabe. Bitte gebe Terraner, Zerg oder Protoss ein.")
        connection.close()
        exit()

    # Sucht Daten in der Datenbank
    query = "SELECT * FROM sc_2_einheiten WHERE \"Rasse\" = %s"

    # SQL-Abfrage ausführen  Ergebnisse speichern
    cursor.execute(query, (rasse,))

    # Ergebnisse speichern und Ergebnisse abrufen
    results = cursor.fetchall()

    if results:
        # Ergebnisse anzeigen
        for row in results:
            print(row)
    else:
        print(f"Es wurden keine Einträge für die Rasse '{rasse}' gefunden.")

finally:
    # Verbindung zur Datenbank schließen
    connection.close()

print("hoi, hoi, hoi")
