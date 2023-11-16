from flask import Flask, render_template, request, jsonify
from main import get_database_connection, get_valid_rasse, query_database
from rasse_enum import Rasse, rasse_mapping

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', data=None)

@app.route('/abfrage', methods=['GET'])
def abfrage():
    rasse_input = request.args.get('rasse')

    connection = get_database_connection()
    selected_rasse = get_valid_rasse(rasse_input, rasse_mapping)

    if selected_rasse is not None:
        if selected_rasse == Rasse.Terraner:
            rasse = 'Terraner'
        elif selected_rasse == Rasse.Zerg:
            rasse = 'Zerg'
        elif selected_rasse == Rasse.Protoss:
            rasse = 'Protoss'

        results = query_database(connection, rasse)

        if results is not None:
            column_names = ["ID", "Name", "Kosten_Mineralien", "Kosten_Vespingas", "Sonstiges", "Rasse", "Versorgung", "Bauzeit", "Ausbildungsort", "Trefferpunkte", "Energie", "Panzerung", "Begrenzte_Lebensdauer", "Typ"]
            extracted_data = [dict(zip(column_names, row)) for row in results]
            return render_template('index.html', data=extracted_data)

    return render_template('index.html', data=None)

if __name__ == '__main__':
    app.run(debug=True)
