from flask import Flask, render_template, request;

app = Flask(__name__)

@app.route("/commissions")
def commissions():
    return render_template("commissions.html")
