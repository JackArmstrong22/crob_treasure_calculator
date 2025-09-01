from flask import Flask, request, jsonify
from flask_cors import CORS
from treasure_calculator.playtime_calc import playtime_calc

app = Flask(__name__)
CORS(app)


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    level = data.get("level")
    time_in_sec = data.get("time_in_sec")

    if level is None or time_in_sec is None:
        return jsonify({"error": "Missing level or time_in_sec"}), 400

    try:
        result = playtime_calc(level, time_in_sec)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
