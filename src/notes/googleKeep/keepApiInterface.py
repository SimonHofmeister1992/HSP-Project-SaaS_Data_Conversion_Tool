#KeepServiceAPI
#gkeepapi version 0.11.14
import sys
import os
import gkeepapi
sys.path.append("../../general/")
from baseApiInterface import baseApiInterface
from keepDataObject import keepDataObject

class keepApiInterface (baseApiInterface):
    
    def injectiInAPI (self, dataObjects):
        """function for the injection of given data from JSON into the service"""
        k = self.login()
        for dataObject in dataObjects:
            gnote = k.createNote(dataObject.title, dataObject.text)
            gnote.timestamps._created = dataObject.created
            gnote.timestamps._edited = dataObject.edited
            k.sync()  
            return gnote
    
    def extractFromAPI (self):
        """function for the injection of given data from the service into JSON"""
        k = self.login()
        gnotes = k.find()
        print(gnotes)
        objectStore = []
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
            print(keepNote)
            print()
            
            dataObject = keepDataObject()
            dataObject.title = n.title
            dataObject.text = n.text
            dataObject.edited = n.timestamps.dt_to_str(n.timestamps._edited)
            dataObject.created = n.timestamps.dt_to_str(n.timestamps._created)
            dataObject.parent_id = n.parent_id
            dataObject.id = n.id
            dataObject.version = n.version
            dataObject.color = n._color.name
            dataObject.trashed = n.timestamps.dt_to_str(n.timestamps._trashed)
            dataObject.updated = n.timestamps.dt_to_str(n.timestamps._updated)
            
            objectStore.append(dataObject)
            
        return objectStore
        
    def login (self):
        print("Starting login")
        k = gkeepapi.Keep()
        k.login('thsp006@gmail.com', 'TestHSPT3st534')
        print("login successfull")
        return k


test = keepApiInterface()
#dictionary = {"title" : "test", "text" : "testtext"}
#liste = [dictionary]
#print(test.inject_in_API(liste))
result = test.extractFromAPI()
for res in result:
    print(res)
    print()