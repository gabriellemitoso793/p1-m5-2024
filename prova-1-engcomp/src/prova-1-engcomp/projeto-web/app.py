from flask import Flask, render_template, request, jsonify
from tinydb import TinyDB, Query

app = Flask(__name__)
db = TinyDB("caminhos.json")

@app.route("/")
def index():
    return render_template("novo.html")

@app.route("/novo", methods=["POST"])
def cadastrar_pontos():
    data = request.get_json()
    pontos_id = db.insert(data)
    return jsonify({"message": f"Ponto cadastrado ID: {pontos_id}"}), 201

@app.route("/pegar_caminho/<int:caminho_id>")
def pegar_pontos(caminho_id):
    pontos = db.get(doc_id=caminho_id)
    if pontos:
        return jsonify(pontos)
    else:
        return jsonify({"error": "Caminho não encontrado"}), 404

@app.route("/listar_caminhos")
def listar_caminhos():
    caminhos = db.all()
    return jsonify(caminhos)

@app.route("/deletar/<int:caminho_id>", methods=["DELETE"])
def deletar_caminho(caminho_id):
    db.remove(doc_ids=[caminho_id])
    return jsonify({"message": f"Caminho ID: {caminho_id} deletado"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
