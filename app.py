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
            column_names = ["id", "name", "rasse", "produktion", "benoetigt", "kosten_mineralien", "kosten_vespingas", "kosten_energie", "ausbildungsdauer", "versorgung", "trefferpunkte", "schild", "panzerung", "energie_minimum", "energie_maximum", "is_psionisch", "is_heroisch", "is_ground_air", "is_bio_mech", "is_leicht_gepanzert_massiv", "lebensdauer", "sicht", "tempo", "attack_damage", "attack_attacks", "attack_target", "attack_cooldown", "attack_range"]
            extracted_data = [dict(zip(column_names, row)) for row in results]
            return render_template('index.html', data=extracted_data)

    return render_template('index.html', data=None)

if __name__ == '__main__':
    app.run(debug=True)
