from flask import Flask

app = Flask(__name__)

@app.route("/")
def wel():
    return "Welcome in my home"

@app.route("/home")
def home():
    return "This is my homeland"

if __name__ == "__main__":
    app.run(debug=True)