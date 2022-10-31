from flask import Flask, flash, render_template, request, redirect, url_for;
import re;

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/commissions",methods=["POST","GET"])
def commissions():
    return render_template("commissions.html")

mail_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


@app.route("/commissions_sent",methods=["POST","GET"])
def send_commissions():
    mail = request.form.get("mail")
    commissions = request.form.get("commissions")
    if commissions == "":
        flash("Pas de commissions envoyés")
        return redirect(url_for('commissions'))
    return render_template("success.html")
