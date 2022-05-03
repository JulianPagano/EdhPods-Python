from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

import json

with open('config.json') as config_file:
    config = json.load(config_file)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/createPods", methods=["POST"])
def generate():
    players = request.json["players"] #.getlist('arrPlayers[]')
    x = {
        "pods": randomize(players)
    }
    return jsonify(x)


def randomize(players):
    import random
    import math
    
    pod_names = config["pod_names"]
    
    random.shuffle(pod_names)
    random.shuffle(players)

    num_of_pods = math.ceil(len(players) / 4)

    pod = 0
    spot = 0
    pods = [[0 for x in range(4)] for y in range(num_of_pods)]
    for p in players:
        pods[pod][spot] = p

        if (pod < num_of_pods - 1):
            pod += 1
        else:
            pod = 0
            spot += 1

    pods_json = []
    for i in range(len(pods)):
        if 0 in pods[i]: pods[i].remove(0)
        p = {
            "pod_name": pod_names[i],
            "players": pods[i]
        }
        pods_json.append(p)

    return list(pods_json)


if __name__ == "__main__":
    app.run(debug=True)
