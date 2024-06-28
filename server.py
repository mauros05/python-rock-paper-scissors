from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def receive_data():
    error = None
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["pass"]

    return f"<h1>Your email is:{email}, your password is: {password}</h1>"


if __name__ == "__main__":
    app.run(debug=True)