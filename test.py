from pprint import pprint
from pymongo import MongoClient
from pymongo import ReturnDocument
from bson.objectid import ObjectId
import json
class DaoAgents:
    def __init__(self):
        self.client = MongoClient('localhost',27017)
        self.db = self.client['agents'] #nome do banco
        self.collection_student = self.db['projects'] #nome da coleção
        self.agent=Agents()
    def insert_into_db(self):
        datastore = json.load(self.agent.toJSON())
        #new_students = self.collection_student.insert_many([datastore])
        print(datastore)

class Agents:
    def __init__(self):
        self.name = ''
        self.services = []


    def toJSON(self):
        return json.dumps(self, default=lambda o: o._dict_,sort_keys=True, indent=4)

class Services:
    def __init__(self):
        self.name = ''
        self.sessions = []
    

class Sessions:
    def __init__(self):
        self.knowledge = ''
        self.temp = ''
        self.code = ''

    


def entry(naome,sessao):
  agente=Agents()
  service=Services()
  sessao=Sessions()
  service.sessions.append(sessao)
  agente.services.append(service) 

