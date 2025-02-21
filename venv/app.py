from flask import Flask, render_template, request
import os
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    bmi = None
    category = None

    if request.method == "POST":
        weight = float(request.form["weight"])
        height = float(request.form["height"]) / 100  # Convert cm to meters
        bmi = round(weight / (height ** 2), 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

    return render_template("index.html", bmi=bmi, category=category)
port=int(os.environ.get("PORT",10000)
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=port)
