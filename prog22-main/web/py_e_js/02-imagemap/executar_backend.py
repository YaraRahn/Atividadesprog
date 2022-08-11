# importações
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os

# configurações
app = Flask(__name__)

# caminho do arquivo de banco de dados
path = os.path.dirname(os.path.abspath(__file__)) 
arquivobd = os.path.join(path, 'pessoa.db')

# sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # remover warnings
db = SQLAlchemy(app)

class Pessoa(db.Model):
    # atributos da pessoa
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    telefone = db.Column(db.String(254))

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return self.nome + "[id="+str(self.id)+ "], " +\
            self.email + ", " + self.telefone
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone
        }

@app.route("/")
def inicio():
    return 'backend ok'

@app.route("/criar_tabelas")
def criar():
    db.create_all()
    
    p1 = Pessoa(nome = "João da Silva", email = "josilva@gmail.com", 
    telefone = "47 99012 3232")
    p2 = Pessoa(nome = "Maria Oliveira", email = "molive@gmail.com", 
        telefone = "47 98822 2531")        
    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()
    return "tabelas criadas, dados inseridos"

@app.route("/listar_pessoas")
def listar():
    # obter dados
    dados = db.session.query(Pessoa).all()
    # converter dados para json
    lista_jsons = [ x.json() for x in dados ]
    # montar a resposta
    retorno = {"resultado":"ok"}
    retorno.update({"detalhes":lista_jsons})
    # converter resposta para resposta http
    resposta = jsonify(retorno)
    # permitir resposta para outros domínios
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

app.run(debug=True)