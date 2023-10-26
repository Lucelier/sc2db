import psycopg2

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

    # Mapping von Eingabe zu tatsächlicher Rasse
    rasse_mapping = {
        'terraner': 'Terraner',
        't': 'Terraner',
        'teraner': 'Terraner',
        'Teraner': 'Terraner',
        'T': 'Terraner',
        'te': 'Terraner',
        'ter': 'Terraner',
        'terr': 'Terraner',
        'terra': 'Terraner',
        'terran': 'Terraner',
        'terrane': 'Terrnaer',
        'tera': 'Terraner',
        'teran': 'Terraner',
        'terane': 'Terraner',
        'Te': 'Terraner',
        'Ter': 'Terraner',
        'Terr': 'Terraner',
        'Terra': 'Terraner',
        'Terran': 'Terraner',
        'Terrane': 'Terrnaer',
        'Tera': 'Terraner',
        'Teran': 'Terraner',
        'Terane': 'Terraner',
        'zerg': 'Zerg',
        'zwerg': 'Zerg',
        'Zwerg': 'Zerg',
        'z': 'Zerg',
        'Z': 'Zerg',
        'ze': 'Zerg',
        'zer': 'Zerg',
        'Ze': 'Zerg',
        'Zer': 'Zerg',
        'protoss': 'Protoss',
        'Protos': 'Protoss',
        'protos': 'Protoss',
        'p': 'Protoss',
        'P': 'Protoss',
    }

    # Überprüfen, ob die Eingabe in der Rasse-Mapping-Tabelle existiert
    if rasse_input in rasse_mapping:
        rasse = rasse_mapping[rasse_input]
    else:
        print("Ungültige Eingabe. Bitte gebe Terraner, Zerg oder Protoss ein.")
        connection.close()
        exit()

    # Sucht Daten in der Datenbank
    query = "SELECT * FROM sc_2_einheiten WHERE \"Rasse\" = %s"

    # SQL-Abfrage ausführen und Ergebnisse speichern
    cursor.execute(query, (rasse,))

    # Ergebnisse abrufen
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

print("hoi, hoi, hoi, hoi")
