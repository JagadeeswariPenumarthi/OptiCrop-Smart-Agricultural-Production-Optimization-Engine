import pickle

import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

MODEL_PATH = "model.pkl"

with open(MODEL_PATH, "rb") as f:
    saved = pickle.load(f)

model = saved["model"]
FEATURE_ORDER = saved["features"]  # e.g. ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/findyourcrop")
def findyourcrop():
    return render_template("findyourcrop.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        values = {feature: [float(request.form.get(feature, ""))] for feature in FEATURE_ORDER}
        input_df = pd.DataFrame(values, columns=FEATURE_ORDER)
        prediction = model.predict(input_df)[0]

        return render_template(
            "findyourcrop.html",
            prediction_text=f"Best crop for the given conditions is {prediction.capitalize()}.",
        )

    except (ValueError, TypeError):
        return render_template(
            "findyourcrop.html",
            prediction_text="Please enter valid numeric values for all fields.",
        )
    except Exception as exc:  # pragma: no cover - safety net for unexpected errors
        return render_template(
            "findyourcrop.html",
            prediction_text=f"Something went wrong while predicting: {exc}",
        )


if __name__ == "__main__":
    app.run(debug=True)
