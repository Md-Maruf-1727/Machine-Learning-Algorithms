from flask import Flask, render_template, request
import pickle

app = Flask(__name__, render_template="tamplate")
main_model = pickle.load("tamplate/area")

@app.route("/")
def home():
    return "Hello"

@app.route("/wel")
def wel():
    return "welcome"

if __name__ == "__main__":
    app.run(debug=True)