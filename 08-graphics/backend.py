from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
import json

path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'dados.db')

from flask_cors import CORS 
app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# se quiser usar mysql:
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://usuario:senha@localhost/meubd"

db = SQLAlchemy(app)

from datetime import date # tratamento de data

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.Text)
    qtde = db.Column(db.Integer)


    def json(self):
        base = {}
        for key, value in self.__dict__.items(): # percorrer nomes dos atributos
            if key != "_sa_instance_state": # nome de atributo doido que eu não quero
                base.update({key: value})
        #print(base)            
        return base

@app.route("/")
def ola():
    return "Servidor backend operante"

@app.route("/criar_tabelas")
def criar_tabelas():
    db.create_all()
    return "tabelas criadas :-)"

@app.route("/criar_animais")
def criar_animais():
    b = Animal(nome = "girafa", qtde = 5)
    c = Animal(nome = "macaco", qtde = 7)
    d = Animal(nome = "oragotango", qtde = 9)

    db.session.add(b)
    db.session.add(c)
    db.session.add(d)
    db.session.commit()
    return "ok"

@app.route("/obter_dados")
def obter_dados():
    animais = db.session.query(Animal).all()
    listax = []
    listay = []
    for a in animais:
        listax.append(a.nome)
        listay.append(a.qtde)

    dados = {
        "x": listax,
        "y": listay,
        "type": "bar"
    }
    retorno = {"resultado":"ok"}
    retorno.update({"detalhes":dados});
    resposta = jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta
    return "ok"

app.run(debug=True)
