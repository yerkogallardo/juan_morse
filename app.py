from flask import Flask, render_template, request, flash
from morse_encoder import traductor_morse

app = Flask(__name__)
app.secret_key="noMad_pYth0n"

@app.route("/")
def index():
    flash("Ingresa palabra a traducir a morse")
    return render_template("index.html")

@app.route("/encode", methods=["POST", "GET"])
def encode():
    val = traductor_morse(str(request.form['word_input']))
    flash(str(request.form['word_input']) + ", se codifica a morse como:")
    flash(val)
    return render_template("index.html")
