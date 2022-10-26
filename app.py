from flask import Flask, render_template, request;
import re;

app = Flask(__name__)

@app.route("/commissions")
def commissions():
    return render_template("commissions.html")

mail_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


@app.route("/commissions_sent")
def send_commissions():
    if not re.fullmatch(mail_regex, request.form.get("mail")) or request.form.get("commissions") == "":
        return render_template("failure.html")
    return render_template("success.html")
