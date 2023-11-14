from flask import Flask, request, jsonify
from main import get_database_connection, get_valid_rasse, query_database
from rasse_enum import Rasse, rasse_mapping

app = Flask(__name__)

@app.route('/abfrage', methods=['GET'])
def abfrage():
    rasse_input = request.args.get('rasse')

    print(f"Received rasse_input: {rasse_input}")

    connection = get_database_connection()
    selected_rasse = get_valid_rasse(rasse_input, rasse_mapping)

    print(f"Selected Rasse: {selected_rasse}")

    if selected_rasse is not None:
        if selected_rasse == Rasse.Terraner:
            rasse = 'Terraner'
        elif selected_rasse == Rasse.Zerg:
            rasse = 'Zerg'
        elif selected_rasse == Rasse.Protoss:
            rasse = 'Protoss'

        results = query_database(connection, rasse)

        # Korrigierte Reihenfolge der Spaltennamen
        column_names = [
            "ID", "Name", "Kosten Mineralien", "Kosten Vespingas",
            "Sonstiges", "Rasse", "Versorgung", "Bauzeit",
            "Ausbildungsort", "Trefferpunkte", "Energie", "Panzerung",
            "Begrenzte Lebensdauer", "Typ"
        ]

        # Extrahiere die relevanten Informationen aus den Ergebnissen
        if results is not None:
            extracted_data = [dict(zip(column_names, row)) for row in results]
        else:
            extracted_data = []

        return jsonify({"data": extracted_data})
    else:
        return jsonify({"message": f"Ungültige Rasse. rasse_input: {rasse_input}"})

if __name__ == '__main__':
    app.run(debug=True)
