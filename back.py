from flask import Flask, request
from flask_cors import CORS
from back_mongo import Mongo
from datetime import datetime
import json


classe = Mongo()

app = Flask(__name__)
cors = CORS(app)


#===QUADRA===

@app.route("/inf_quadra", methods=['POST'])
def inf_quadra():

    data = json.loads(request.data)
    chamada = classe.find_one_quadra(data)
    return chamada

@app.route("/quadra", methods=['POST'])
def quadra():
    data = [json.loads(request.data)]
    chamada = classe.insert_many_quadra(data)
    return chamada

@app.route("/del_quadra", methods=['POST'])
def del_quadra():

    data = json.loads(request.data)
    chamada = classe.delete_mongo_quadra(data)
    return chamada

@app.route("/up_quadra", methods=['POST'])
def up_quadra():
    data = json.loads(request.data)
    chamada = classe.delete_mongo_quadra(data)
    return chamada


#===CLIENTE===


@app.route("/cliente", methods=['POST'])
def cliente():

    data = [json.loads(request.data)]
    chamada = classe.inser_many_cliente(data)    
    return chamada


@app.route("/inf_cliente",  methods=['POST'])
def inf_cliente():

    data = json.loads(request.data)
    chamada = classe.find_one_cliente(data)
    return (chamada)


@app.route("/del_cliente", methods=["POST"])
def del_cliente():

    data = json.loads(request.data)
    chamada = classe.delete_mongo_cliente(data)
    return chamada


@app.route("/up_cliente", methods=["POST"])
def up_cliente():

    data = json.loads(request.data)
    chamada = classe.update_mongo_cliente(data)
    return chamada



# ====quadra-cliente=====
@app.route("/solicitacao-quadra", methods=["PUT"])
def solicitacao_quadra():
    id_cliente = json.loads(request.data)

    print(f"[ID_CLIENTE] {id_cliente}")
    document = classe.find_one_cliente(id_cliente)['document']
    print(f"[DOCUMENTS] {document}")

    classe.update_mongo_quadra_cliente(documents_client=document, documents_quadra=id_cliente)

    return {'porra':'nenhuma'}

app.run(port=3030)