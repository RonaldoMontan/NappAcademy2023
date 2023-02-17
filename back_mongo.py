import requests
import json
from bson.objectid import ObjectId

class Mongo:

    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': '', 
        }

    def find_one_quadra(self, documents):
        url = "https://data.mongodb-api.com/app/data-ouyxz/endpoint/data/v1/action/find"

        payload = json.dumps({
            "collection": "quadra",
            "database": "flask",
            "dataSource": "Flask-bd",
            "filter": {"_id": documents["_id"]}
        })

        response = requests.request("POST", url, headers=self.headers, data=payload).json()

        return response

    def insert_many_quadra(self, documents):

        url = "https://data.mongodb-api.com/app/data-ouyxz/endpoint/data/v1/action/insertMany"
        payload = json.dumps({
            "collection": "quadra",
            "database": "flask",
            "dataSource": "Flask-bd",
            "documents": documents
        })

        response = requests.request("POST", url, headers=self.headers, data=payload).json()

        return response

    def update_mongo_quadra(self, documents):
        url = 'https://data.mongodb-api.com/app/data-ouyxz/endpoint/data/v1/action/updateOne'
        print({documents['_id']})

        payload = json.dumps({
            "collection": "quadra",
            "database": "flask",
            "dataSource": "Flask-bd",
            "filter": {"_id": {
                "$oid":f"{documents['_id']}" }
                },
            "update": {
                "$set": { "disponivel": documents["disponivel"],
                        "horario": documents["horario"],
                        "reservado_por": documents["reservado_por"]}
            }
        })

        response = requests.request("POST", url=url , headers=self.headers, data=payload).json()
        return response

    def delete_mongo_quadra(self, documents):

        url = 'https://data.mongodb-api.com/app/data-ouyxz/endpoint/data/v1/action/deleteOne'

        payload = json.dumps({
            "collection": "quadra",
            "database": "flask",
            "dataSource": "Flask-bd",
            "filter": {"_id": documents["_id"]}
        })
        response = requests.request("POST", url=url, headers=self.headers, data=payload).json()

        return response


    def inser_many_cliente(self, documents):

        url = "https://data.mongodb-api.com/app/data-ouyxz/endpoint/data/v1/action/insertMany"
        payload = json.dumps({
            "collection": "cliente",
            "database": "flask",
            "dataSource": "Flask-bd",
            "documents": documents
        })

        response = requests.request("POST", url, headers=self.headers, data=payload).json()
        return response

    def find_one_cliente(self, documents):

        url = "https://data.mongodb-api.com/app/data-ouyxz/endpoint/data/v1/action/findOne"
        payload = json.dumps({
            "collection": "cliente",
            "database": "flask",
            "dataSource": "Flask-bd",
            "filter": {"_id": documents["_id"]}
        })
                
        response = requests.request("POST", url, headers=self.headers, data=payload).json()
        print(response)
        return response

    def delete_mongo_cliente(self, documents):

        url = 'https://data.mongodb-api.com/app/data-ouyxz/endpoint/data/v1/action/deleteOne'

        payload = json.dumps({
            "collection": "cliente",
            "database": "flask",
            "dataSource": "Flask-bd",
            "filter": {"_id": documents["_id"]}
        })
        response = requests.request("POST", url=url, headers=self.headers, data=payload).json()
        return response

    def update_mongo_cliente(self, documents):
        print(documents)
        url = 'https://data.mongodb-api.com/app/data-ouyxz/endpoint/data/v1/action/updateOne'

        payload = json.dumps({
            "collection": "cliente",
            "database": "flask",
            "dataSource": "Flask-bd",
            "filter": {"_id": documents['_id']},
            "update": {
                "$set": {"horario": documents["horario"],
                        "quadra": documents["quadra"],
                        "reservado_por": documents["reservado_por"]}
            }
        })
        response = requests.request("POST", url=url, headers=self.headers, data=payload).json()
        return response






