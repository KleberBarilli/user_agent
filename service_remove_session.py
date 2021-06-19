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
        self.teste = self.collection_agents['sessions']


    def create_backup(self):
        self.collection_backup = self.db['BACKUP'] #nome da coleção
        all_agents = self.collection_agents.find({})
        a = list(all_agents)
        self.collection_backup.insert_many(a)

    def remove_session(self, _name):
        agents = list(self.collection_agents.find({"name":_name}))
        
        #for agent in agents:
         #   for key,value in agent.items():
          
          #     print(key,value)
       
        

        print(self.collection_agents.find('sessions'[{"name":"projeto1"}]))

        
          
        #self.teste.delete_one({"uid":"291885b1-d0d1-11e9-ae30-f8da0c949941"})
        #print(self.collection_agents['sessions'])
          



     
  

agent = GetAgents()
try:
    agent.create_backup()
    #agent.remove_session('agente2')
except:
    agent.remove_session('projeto1')