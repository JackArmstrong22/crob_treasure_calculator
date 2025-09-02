from flask import Flask, request, jsonify
from flask_cors import CORS
from treasure_calculator.playtime_calc import playtime_calc

app = Flask(__name__)
CORS(app)
BONUS_TIME_LENGTH = 20


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    level = data.get("level")
    time_in_sec = data.get("time_in_sec")
    is_bonus_time = data.get("is_bonus_time")

    if level is None or time_in_sec is None:
        return jsonify({"error": "Missing level or time_in_sec"}), 400
    elif is_bonus_time:
        time_in_sec -= BONUS_TIME_LENGTH

    try:
        result = playtime_calc(level, time_in_sec)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
