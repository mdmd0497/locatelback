import math
import os
from pprint import pprint
from pymongo import MongoClient
from api.src.models import Account

class Queryset:
    def __init__(self): 
        self.client = MongoClient(os.getenv('MONGO_URI') or 'mongodb://localhost:27017/prueba') 
    

    def validate_account(self,account):
        
        db = self.client.prueba
        collection = db.account
        cursor = collection.find_one({"account": account})
        pprint(cursor)
        
        return  bool(collection.find_one({"account": account}))


    def create_account(self,account:Account):
        db = self.client.prueba
        collection = db.account
        collection.insert_one(account.to_dict())
        return account.to_dict()

    def update_value_account(self, account: int, value: float):
        db = self.client.prueba
        collection = db.account
        print(account)
        val = collection.find_one({"account": account})
        print(value)
        if val:
            collection.update_one(
                {"account": account},
                {
                    "$set": {
                        "value": value
                    }
                }
            )
            return {
                "status": 200,
                "data": {
                    "message": "valor cambiado con exito" 
                }
            }
        return {
            "status": 409,
            "data": {
                "message": "cuenta no encontrada"
            }
        }



    def consult_account(self, account: int):
        db = self.client.prueba
        collection = db.account
        acc = collection.find_one({"account": account})
        if acc:
            accountobject = Account(account=acc["account"],name=acc["name"],value=acc["value"])
            return {
                "status": 200,
                "data": accountobject.to_dict()
            }
        return {
            "status": 404,
            "data": {
                "message": "no se encontro cuenta"
            }
        }

