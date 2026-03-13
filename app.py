from flask import Flask, render_template, request, redirect, session
import mysql.connector
from model.requisitos import recuperar_requisitos, update
from model.requisitos import inserir_dados
from model.requisitos import excluir_descricao


app = Flask (__name__)

@app.route("/")
def pag_principal():

    # mostrando pag
    return render_template("index.html")

@app.route("/requisitos", methods = ["GET"])
def pag_requisitos():
    requisitos = recuperar_requisitos()
    return render_template("requisitos.html", requisitos = requisitos )

# botao de marcar como resolvido/pendente

@app.route("/cadastrar", methods = ["POST"])
def pag_cadastrar():
    descricao = request.form.get("descricao")
    nivel = request.form.get("nivel")
    valor =  request.form.get("valor")
    inserir_dados(descricao, nivel, valor)
    return redirect("/requisitos")

@app.route("/requisitos/delete/<codigo>")
def deletar_registros(codigo):
    excluir_descricao(codigo)
    return redirect("/requisitos")

@app.route("/requisitos/status/<codigo>/<status>")
def status(codigo, status):
    update(codigo, status)
    return redirect("/requisitos")


# rodando
if __name__ == "__main__":
    app.run(debug=True)
