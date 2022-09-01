from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
# https://dev.to/thetrebelcc/how-to-run-a-flask-app-over-https-using-waitress-and-nginx-2020-235c
from waitress import serve

path = os.path.dirname(os.path.abspath(__file__)) 
arquivobd = os.path.join(path, 'pessoa.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

cont = 0

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    telefone = db.Column(db.String(254))

    def __str__(self):
        return self.nome + "[id="+str(self.id)+ "], " +\
            self.email + ", " + self.telefone

    def json(self):
        return { "id": self.id, 
                 "nome": self.nome, 
                 "email": self.email, 
                 "telefone": self.telefone
               }

@app.route("/")
def ola():
    return "Servidor backend operante"

@app.route("/listar")
def listar():
    pessoas = db.session.query(Pessoa).all()
    lista = []
    for p in pessoas:
        lista.append(p.json())
    resposta = jsonify(lista)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/operacao")
def operacao():
    global cont
    cont += 1
    print("contador: ", cont)
    return "A operação foi executada, e o contador foi incrementado"

@app.route("/contador")
def contador():
    return str(cont)

@app.route("/rota1")
def rota1():
    resposta = jsonify({"mensagem":"esta é a primeira rota"})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/rota2")
def rota2():
    resposta = jsonify({"mensagem":"rota dois na área"})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/rota3")
def rota3():
    resposta = jsonify({"mensagem":"opa temos uma terceira rota"})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/rota4")
def rota4():
    resposta = jsonify({"mensagem":"Alana, Manu, Lari, Liriel, Yara"})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta


#app.run(debug=True)
serve(app, host='0.0.0.0', port=5000)

# teste: curl localhost:5000/listar