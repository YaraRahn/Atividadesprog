from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
import json

path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'pessoa.db')

from flask_cors import CORS 
app = Flask(__name__)
CORS(app)

#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# se quiser usar mysql:
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://discente:informatica2022@191.52.7.110/pgm_dois"

db = SQLAlchemy(app)

from datetime import date # tratamento de data

class Pessoa(db.Model):
    __tablename__ = "pessoa_alana_yara"
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.Text) # chave id inteira é melhor, deixa incluir repetido :-) , primary_key=True)
    habilidades = db.Column(db.Text)
    time = db.Column(db.Integer)
    nasci_brasil = db.Column(db.Boolean)
    filho_unico = db.Column (db.Boolean)
    turno = db.Column(db.Integer)
    viajou_fora_sc = db.Column(db.Text)
    foi_na_praia = db.Column(db.Text)
    restricao = db.Column(db.Text)
    expectativa_vida = db.Column(db.Integer)
    cor_preferida = db.Column(db.Text)
    musicas_preferidas = db.Column(db.Text)
    livros_por_ano = db.Column(db.Integer)
    
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

@app.route("/listar")
def listar():
    pessoas = db.session.query(Pessoa).all()
    lista = []
    for p in pessoas:
        lista.append(p.json())
    resposta = jsonify(lista)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

# teste da rota: 
# curl -d '{"email":"soueu@gmail.com","habilidades":"tocar teclado\r\n nadar os quatro estilos\r\n jogar fluft","time":"2","nasci_brasil":"True","turno":"2","viajou_fora_sc":"on","foi_na_praia":"on","restricao":"Vegana","expectativa_vida":"67","cor_preferida":"verde","musicas_preferidas":"haleluia \r\n xote dos milagres","livros_por_ano":"2"}' -X POST -H "Content-Type:application/json" localhost:5000/incluir
@app.route("/incluir", methods=['post'])
def incluir():
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json()

    # tratamento de dados especiais
    
    #partes = dados['dtnasc'].split("-")
    # substituir o item original do dicionário por um valor do python
    #dados['dtnasc'] = date(int(partes[0]), int(partes[1]), int(partes[2]))

    subst_checkbox(dados, 'nasci_brasil')
    subst_checkbox(dados, 'viajou_fora_sc')
    subst_checkbox(dados, 'filho_unico')
    subst_checkbox(dados, 'foi_na_praia')

    try:  
        nova = Pessoa(**dados)
        db.session.add(nova)
        db.session.commit()
    except Exception as e: 
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
    
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

def subst_checkbox(dados, id_check):

    if dados[id_check] == '1':
        dados[id_check] = True
    else:
        dados[id_check] = False

app.run(debug=True)
