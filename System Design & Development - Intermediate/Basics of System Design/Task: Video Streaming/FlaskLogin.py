from flask import Flask, render_template, request
from LogindataManager.GetLoginData import *
from Detection.FaceDetection import *
from flask import request
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/", methods=["GET", "POST"])
def login():
    return render_template("Login.html")

@app.route("/")
def index():
    return render_template("live_stream.html")


@app.route("/live_stream", methods=["GET", "POST"])
def live_stream():
    if request.method == "POST":
        email_id = request.form.get("email_id")
        password = request.form.get("password")

        if GetLoginData().check_credentials(email_id, password):
            return render_template("live_stream.html")
        else:
            if GetLoginData().check_email_id(email_id):
                return render_template("Login.html", task="Invalid email id")
            if GetLoginData().check_password(password):
                return render_template("Login.html", task="Invalid password")
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5003)
