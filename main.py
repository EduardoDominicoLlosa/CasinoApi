from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# casino data array
rngData = []

# GET method
@app.route('/api/rng', methods=['GET'])
def getRng():
    return jsonify({"rng": rngData})


# POST method
@app.route('/api/rng', methods=['POST'])
def addRngItem():
    data = request.get_json()

    if not data or "rngModifier" not in data:
        return jsonify({"message": "Invalid data"}), 400

    # Modifier
    rngModifier = data["rngModifier"]
    rng = random.randint(1, rngModifier)

    # Winning odds
    winningOdds = (rngModifier - rng + 1) / rngModifier * 100

    # Jackpot hit if 1
    is_jackpot = rng == 1

    # parameters
    newData = {
        "id": len(rngData) + 1,
        "rng": rng,
        "rngModifier": rngModifier,
        "is_jackpot": is_jackpot,
        "winningOdds": winningOdds
    }

    rngData.append(newData)

    return jsonify({"message": "Data added successfully", "rngData": newData}), 201


if __name__ == '__main__':
    app.run(debug=True)
