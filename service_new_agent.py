import pymongo 
import json
import uuid
import os
import jsonpickle



class Sessions:
    def __init__(self,_name):
        self.name=_name
        self.store = ''
        self.temp = ''
        self.model = ''
        self.uid=''


class AgentStore(object):
    def __init__(self,_name):
        self.name = _name
        self._id= _name
        self.uid=''
        self.sessions = [] 
    


def make_directories(agent):
    try:
      os.mkdir('/mindnet/agents/')
    except: pass 
    try:
      os.mkdir('/mindnet/agents/agent_'+agent.uid)
    except: pass 
    for session in agent.sessions:
        try:
         os.mkdir('/mindnet/agents/agent_'+agent.uid+'/project_'+session.uid)
        except: pass 
        try: 
          os.mkdir('/mindnet/agents/agent_'+agent.uid+'/project_'+session.uid+'/store')
        except: pass 
        try:  
          os.mkdir('/mindnet/agents/agent_'+agent.uid+'/project_'+session.uid+'/model')
        except: pass   
        try:  
          os.mkdir('/mindnet/agents/agent_'+agent.uid+'/project_'+session.uid+'/temp')
        except: pass   
        #====
        session.store='/mindnet/agents/agent_'+agent.uid+'/project_'+session.uid+'/store'
        session.model='/mindnet/agents/agent_'+agent.uid+'/project_'+session.uid+'/model'
        session.temp='/mindnet/agents/agent_'+agent.uid+'/project_'+session.uid+'/temp'
    

def load(r):
    return jsonpickle.decode(r)


def check_session_Exists(_session_name,sessions):
    for s in sessions:
        if s.name == _session_name:
            return True
    return False        

def entry(_name,_session):
  MONGO_URL='mongodb://localhost:27017/MINDNET' 
  conn = pymongo.MongoClient(MONGO_URL)     
  db = conn.mindnet
  tb = conn.mindnet['AGENTS'] 
  r=tb.find_one({'name':_name})
  if r != None:
    r1=json.dumps(r)
    #print 'R:',r1
    agent=load(r1)
  else:  
    agent=AgentStore(_name)
    agent.uid=str(uuid.uuid1())
  #==
  if not check_session_Exists(_session,agent.sessions):
   _s1=Sessions(_session) 
   _s1.uid=str(uuid.uuid1())
   agent.sessions.append(_s1)
   make_directories(agent)
   #rp=json.loads(jsonpickle.encode(agent))
   rp=json.loads(jsonpickle.encode(agent))
   tb.remove({'name':_name})
   #==
   #print ('Type:',type(rp).__name__)
   tb.insert_one(rp)
   # gerar mensagem de OK
  else:
    # gerar mensagem de erro que ja existe essa sessao 
    print("This session already exists.")
    pass



#entry('agente2','projeto1')

entry('agente2', 'projeto1')


