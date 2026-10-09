from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

def estimate_trip(distance, mpg, price, extra=0):
    if distance <= 0 or mpg <= 0 or price < 0 or extra < 0:
        raise ValueError("Distance and MPG must be greater than zero. Costs cannot be negative.")
    gallons = distance / mpg
    fuel_cost = gallons * price
    total = fuel_cost + extra
    return {
        "distance": round(distance, 2),
        "mpg": round(mpg, 2),
        "gallons": round(gallons, 2),
        "fuel_cost": round(fuel_cost, 2),
        "extra": round(extra, 2),
        "total": round(total, 2),
        "cost_per_mile": round(total / distance, 2)
    }

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/calculate", methods=["POST"])
def calculate():
    data = request.get_json(silent=True) or {}
    try:
        distance = float(data.get("distance", 0))
        mpg = float(data.get("mpg", 0))
        price = float(data.get("price", -1))
        extra = float(data.get("extra", 0))
        if not all(map(lambda x: x == x and abs(x) != float("inf"), [distance, mpg, price, extra])):
            raise ValueError("Please enter valid finite numbers.")
        result = estimate_trip(distance, mpg, price, extra)
        return jsonify({"ok": True, "result": result})
    except (ValueError, TypeError):
        return jsonify({"ok": False, "error": "Enter valid numbers. Distance and MPG must be above zero; gas price and extra expenses cannot be negative."}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
