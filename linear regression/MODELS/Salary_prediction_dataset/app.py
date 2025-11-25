from flask import Flask, render_template, request
import pickle

app = Flask(__name__, template_folder="template")
model = pickle.load(open("linear regression/MODELS/Salary_prediction_dataset/age.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def pred():
    experience = float(request.form.get("experience"))
    age = float(request.form.get("age"))
    education = float(request.form.get("education"))
    feature = [[experience, age, education]]
    prediction = model.predict(feature)[0]
    prediction = float(prediction)
    return render_template("index.html", Predicted_Data= round(prediction, 2))

if __name__ == "__main__":
    app.run(debug=True)
