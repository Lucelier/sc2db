import psycopg2
from rasse_enum import Rasse, rasse_mapping


def get_database_connection():
    dbname = "SC2"
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

        query = """
                SELECT 
                    e.id AS einheiten_id,
                    e.name AS einheiten_name,
                    r.rassen_name,
                    g_prod.gebaeude_name AS produktions_gebaeude,
                    g_benoetigt.gebaeude_name AS benoetigtes_gebaeude,
                    e.kosten_mineralien,
                    e.kosten_vespingas,
                    e.kosten_energie,
                    e.ausbildungsdauer,
                    e.versorgung,
                    e.trefferpunkte,
                    e.schild,
                    e.panzerung,
                    e.energie_minimum,
                    e.energie_maximum,
                    e.is_psionisch,
                    e.is_heroisch,
                    kag1.kat_ground_air_name AS ground_air,
                    kbm.kat_bio_mech_name AS bio_mech,
                    klgm.kat_leicht_gepanzert_massiv_name AS leicht_gepanzert_massiv,
                    e.lebensdauer,
                    e.sicht,
                    e.tempo,
                    e.attack_damage,
                    e.attack_attacks,
                    kag2.kat_ground_air_name AS attack_target,
                    e.attack_cooldown,
                    e.attack_range
                FROM 
                    einheiten e
                LEFT JOIN rassen r ON e.rasse = r.rassen_id
                LEFT JOIN gebaeude g_prod ON e.produktion = g_prod.gebaeude_id
                LEFT JOIN gebaeude g_benoetigt ON e.benoetigt = g_benoetigt.gebaeude_id
                LEFT JOIN kat_ground_air kag1 ON e.is_ground_air = kag1.kat_ground_air_id
                LEFT JOIN kat_bio_mech kbm ON e.is_bio_mech = kbm.kat_bio_mech_id
                LEFT JOIN kat_leicht_gepanzert_massiv klgm ON e.is_leicht_gepanzert_massiv = klgm.kat_leicht_gepanzert_massiv_id
                LEFT JOIN kat_ground_air kag2 ON e.attack_target = kag2.kat_ground_air_id
                WHERE r.rassen_name = %s;
                """
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
