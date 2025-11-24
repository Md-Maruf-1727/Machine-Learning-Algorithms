from flask import Flask, render_template, request

app = Flask(__name__, template_folder="tamplate")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def pred():
    data = float(request.form.get("height"))
    feature = [[data]]

if __name__ == ("__main__"):
    app.run(debug=True)