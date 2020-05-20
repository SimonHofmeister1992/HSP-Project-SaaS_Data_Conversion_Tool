#KeepServiceAPI
#gkeepapi version 0.11.14
import sys, os
import gkeepapi
path = os.path.abspath(os.getcwd())
path = path.split("\\")
path = path[:len(path)-2]
path = "\\".join(path)
path = path+"\\general"
sys.path.insert(0, path)
#print(sys.path)
from apiBase import apiBase

class KeepServiceAPI (apiBase):
    
    def inject_in_API (self, attributes):
        """function for the injection of given data from JSON into the service"""
        k = self.login()
        for a in attributes:
            gnote = k.createNote(a['title'], a['text'])
            if('created' in a):
                print("inside", ('created' in a))
                gnote.timestamps._created = gnote.timestamps.str_to_dt(a.get('created'))
            if('edited' in a):
                print("inside", ('edited' in a))
                gnote.timestamps._edited = gnote.timestamps.str_to_dt(a.get('edited'))
            k.sync()  
            return gnote
    
    def extract_from_API (self):
        """function for the injection of given data from the service into JSON"""
        k = self.login()
        gnotes = k.find()
        print(gnotes)
        datastore = []
        for n in gnotes:
            keepNote = {
            "title" : n.title, 
            "parent" : n.parent, 
            "id" : n.id, 
            "server_id" : n.server_id, 
            "parent_id" : n.parent_id, 
            "version" : n.version, 
            "text" : n.text, 
            "color" : n._color.name, 
            "archived" : n._archived, 
            "pinned" : n._pinned, 
            "moved" : n._moved, 
            "created" : n.timestamps.dt_to_str(n.timestamps._created), 
            #"deleted" : n.timestamps.dt_to_str(n.timestamps._deleted), 
            "trashed" : n.timestamps.dt_to_str(n.timestamps._trashed), 
            "updated" : n.timestamps.dt_to_str(n.timestamps._updated), 
            "edited" : n.timestamps.dt_to_str(n.timestamps._edited)
            }
            datastore.append(keepNote)
        return datastore
        
    def login (self):
        print("Starting login")
        k = gkeepapi.Keep()
        k.login('thsp006@gmail.com', 'TestHSPT3st534')
        print("login successfull")
        return k


#test = KeepServiceAPI()
#dictionary = {"title" : "test", "text" : "testtext"}
#liste = [dictionary]
#print(test.inject_in_API(liste))
#result = test.extract_from_API()
#for res in result:
    #print(res)
    #print()