from pprint import pprint
from pymongo import MongoClient
from pymongo import ReturnDocument
from bson.objectid import ObjectId
import json
import jsonpickle
from bson import json_util

class GetAgents:
    def __init__(self):
        self.client = MongoClient('localhost',27017)
        self.db = self.client['mindnet'] #nome do banco
        self.collection_agents = self.db['AGENTS'] #nome da coleção



    def create_backup(self):
        self.collection_backup = self.db['BACKUP'] #nome da coleção
        all_agents = self.collection_agents.find({})
        a = list(all_agents)
        self.collection_backup.insert_many(a)

    def remove_agent(self, _name):
        self.collection_agents.delete_one({"name":_name})


agent = GetAgents()
try:
    agent.create_backup()
    agent.remove_agent('agente2')
except:
    agent.remove_agent('agente2')