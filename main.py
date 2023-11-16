import psycopg2
from rasse_enum import Rasse, rasse_mapping


def get_database_connection():
    dbname = "Test"
    user = "postgres"
    password = "postgres"
    host = "localhost"
    port = "5432"

    return psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )


def get_valid_rasse(input_str, mapping):
    return mapping.get(input_str)


def query_database(connection, rasse):
    try:
        cursor = connection.cursor()

        query = "SELECT * FROM sc_2_einheiten WHERE \"Rasse\" = %s"
        cursor.execute(query, (rasse,))

        results = cursor.fetchall()

        return results  # Hier geben wir die Ergebnisse zurück

    finally:
        connection.close()


if __name__ == "__main__":
    connection = get_database_connection()

    rasse_input = input("Welche Rasse möchtest du anzeigen (Terraner, Zerg, Protoss)? ").strip().lower()
    selected_rasse = get_valid_rasse(rasse_input, rasse_mapping)

    if selected_rasse is not None:
        if selected_rasse == Rasse.Terraner:
            rasse = 'Terraner'
        elif selected_rasse == Rasse.Zerg:
            rasse = 'Zerg'
        elif selected_rasse == Rasse.Protoss:
            rasse = 'Protoss'

        results = query_database(connection, rasse)

        if results:
            for row in results:
                print(row)
        else:
            print(f"Es wurden keine Einträge für die Rasse '{rasse}' gefunden.")
    else:
        print("Ungültige Eingabe. Bitte gebe Terraner, Zerg oder Protoss ein.")
