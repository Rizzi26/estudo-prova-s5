# app.py
from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB

app = Flask(__name__)

db = TinyDB("posts.json")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sobre", methods=["GET", "POST"])
def sobre(nome=None):
    if request.method == "POST":
        nome = request.form.get("nome")
        db.insert({"nome": nome})
    posts = db.all()
    return render_template("sobre.html", nome=nome, posts=posts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)