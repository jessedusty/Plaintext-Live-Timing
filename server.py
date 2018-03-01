from flask import Flask, jsonify

app = Flask(__name__)
from parse_scores import *


@app.route("/teams/<team>/<int:race_id>")
def team_results(team, race_id):
    return stringify_racers(show_team(retrieve_times(race_id), team))


@app.route("/scores/<int:race_id>")
def race_results(race_id):
    return stringify_racers(retrieve_times(race_id))


def pebblify(content):
    return jsonify({
        "content": content,
        "refresh": 300,
        "vibrate": 0,
        "font": 4,
        "theme": 0,
        "scroll": 0,
        "light": 1,
        "blink": 1,
        "updown": 0,
        "auth": "salt"
    })


# Use https://github.com/bahbka/pebble-my-data for displaying information on Pebble

@app.route("/p/teams/<team>/<int:race_id>")
def p_team_results(team, race_id):
    return pebblify(team_results(team, race_id))


@app.route("/p/scores/<int:race_id>")
def p_race_results(race_id):
    return pebblify(race_results(race_id))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=8080)
