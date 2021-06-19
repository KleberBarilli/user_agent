from pprint import pprint
from pymongo import MongoClient
from pymongo import ReturnDocument
from bson.objectid import ObjectId
import json

class GetAgents:
    def __init__(self):
        self.client = MongoClient('localhost',27017)
        self.db = self.client['mindnet'] #nome do banco
        self.collection_agents = self.db['AGENTS'] #nome da coleção


    def find_all(self):
        all_agents = self.collection_agents.find({})
        lista = []
        for agents in all_agents:
            lista.append(agents)
        
        return json.dumps(lista)
        


agent = GetAgents()

agent.find_all()