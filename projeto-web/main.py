from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB

app = Flask(__name__)

db = TinyDB("caminhos.json")

# rota para a página inicial
@app.route("/")
def index():
    return render_template("index.html")

# rota para cadastrar novas posições
@app.route("/cadastro_new", methods=["POST"])
def cadastro_new():
    if request.method == "POST":
        position_x = request.form.get("position_x")
        position_y = request.form.get("position_y")
        position_z = request.form.get("position_z")
        position_r = request.form.get("position_r")
        db.insert({"position_x": position_x, "position_y": position_y, "position_z": position_z, "position_r": position_r})
        print("Caminho cadastrado com sucesso!")
    return redirect(url_for('index'))

# rota para mostrar todas as posições cadastradas
@app.route("/home")
def home():
    caminhos = db.all()
    return render_template("home.html", caminhos=caminhos)

# rota para deletar um grupo de posição
@app.route("/delete/<int:id>")
def delete(id):
    db.remove(doc_ids=[id])
    return redirect(url_for('home'))

# rota para atualizar um grupo de posição
@app.route("/update/<int:id>")
def update(id):
    caminho = db.get(doc_id=id)
    return render_template("update.html", caminho=caminho)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
