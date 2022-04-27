from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/createPods", methods=["POST"])
def createPods():
    
    players = request.form.getlist('arrPlayers[]')
    return jsonify(randomize(players))

def randomize(players):
    import random
    import math
    
    random.shuffle(players)

    numOfPlayers = len(players)
    numOfTables = math.ceil(numOfPlayers / 4)

    table = 0
    spot = 0
    pods = [[0 for x in range(4)] for y in range(numOfTables)]
    for p in players:
        pods[table][spot] = p

        if (table < numOfTables - 1):
            table += 1
        else:
            table = 0
            spot += 1

    return pods

if __name__ == "__main__":
    app.run(debug=True)
