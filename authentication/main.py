import os
from types import MethodDescriptorType

from flask import Flask, redirect, render_template, request, session, url_for
from helpers import get_users, hash_password

__winc_id__ = "8fd255f5fe5e40dcb1995184eaa26116"
__human_name__ = "authentication"

app = Flask(__name__)

app.secret_key = os.urandom(16)


@app.route("/home")
def redirect_index():
    return redirect(url_for("index"))


@app.route("/")
def index():
    return render_template("index.html", title="Index")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/lon")
def lon():
    return render_template("lon.html", title="League of Nations")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template("login.html", title="Login form", error=request.args.get('error'))
    if request.method == 'POST':
        users = get_users()
        if request.form['username'] in users and users[request.form['username']] == hash_password(request.form['password']):
            return redirect(url_for("dashboard", user=request.form['username']))
        else:
            return redirect(url_for('login', error=True))



@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if request.method == 'GET':
        return render_template("dashboard.html", title="Login form", user=request.args.get('user'))
    elif request.method == 'POST':
        return redirect(url_for('logout'))


@app.route("/logout", methods=["GET", "POST"])
def logout():
    return redirect(url_for('index'))
