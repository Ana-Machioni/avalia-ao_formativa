from flask import Flask, render_template, request, redirect, session
import mysql.connector
from model.requisitos import recuperar_requisitos
from model.requisitos import inserir_dados

app = Flask (__name__)

@app.route("/")
def pag_principal():

    # mostrando pag
    return render_template("index.html")

@app.route("/requisitos", methods = ["GET"])
def pag_requisitos():
    requisitos = recuperar_requisitos()
    return render_template("requisitos.html", requisitos = requisitos )

@app.route("/cadastrar")
def pag_cadastrar():
    descricao = request.form.get("descricao")
    nivel = request.form.get("nivel")
    valor =  request.form.get("valor")
    if inserir_dados(descricao, nivel, valor):
        return redirect("/")
    else:
        return "erro ao adicionar dados"
    
# rodando
if __name__ == "__main__":
    app.run(debug=True)