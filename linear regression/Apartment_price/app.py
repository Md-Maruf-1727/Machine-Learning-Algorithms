from flask import Flask, render_template, request
import pickle

app = Flask(__name__, template_folder="template")
model = pickle.load(open("linear regression/Apartment_price/area.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def pred():
    area = float(request.form.get("area"))
    bedrooms = float(request.form.get("bedrooms"))
    feature = [[area,bedrooms]]
    prediction = model.predict(feature)[0]
    prediction = float(prediction)
    return render_template("index.html", Predicted_Data= round(prediction, 2))

if __name__ == "__main__":
    app.run(debug=True)