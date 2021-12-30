from flask import Flask, render_template, redirect, url_for

__winc_id__ = "9263bbfddbeb4a0397de231a1e33240a"
__human_name__ = "templates"

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', title='Index')

@app.route("/home")
def home():
    return redirect(url_for('index'))

@app.route("/contact")
def contact():
    return render_template('contact.html', title="Contact")

@app.route("/about")
def about():
    return render_template('about.html', title="About")