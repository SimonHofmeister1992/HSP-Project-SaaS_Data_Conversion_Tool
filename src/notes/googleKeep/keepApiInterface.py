#KeepServiceAPI
#gkeepapi version 0.11.16
#Keep User Name: thsp006@gmail.com
#Password: TestHSPT3st534

import sys
import os
import gkeepapi
import traceback
import time
sys.path.append("../../general/")
from baseApiInterface import baseApiInterface
from keepDataObject import keepDataObject

class keepApiInterface (baseApiInterface):

    username = ""
    password = ""
    errorCount = 0
    successCount = 0
    
    def __init__(self, username, password):
        """provide the login information with object generation"""
        self.username = username
        self.password = password
        self.id_tag = "notes#" + keepApiInterface.__name__ + "#"
        
    def requestInjection (self, substrIdTag = None):
        """requests the data for Injection into the service and keeps track of the result"""
        
        self.errorCount = 0
        self.successCount = 0
        self.requestInjectionInAPI(keepDataObject, substrIdTag)
        print()
        print("Results: ")
        print("Notes failed to inject: ", self.errorCount)
        print("Notes successfully injected: ", self.successCount)
        
    def idCheck(self, keepId):
        """checks the length off the id and cuts everything beyond 50 chars"""
            
        if(len(keepId) > 50):
            keepId = keepId[0:50]
        return keepId
    
    def injectInAPI (self, dataObject):
        """function for the injection of given data from dict into the service"""
        
        if dataObject != None:
            k = self.login()
            #print(dataObject)
            #try:
            keepId = dataObject["_id"].split("#")[2]
            keepId = self.idCheck(keepId)
            service = dataObject["_id"].split("#")[1]
            #print(keepId)
            #gnote = k.find(func = lambda x: x.id == keepId)
            gnote = None
            note = k.get(keepId)
            if note is not None:
                print("Found preexisting Note")
                gnote = note
                gnote.title = dataObject["title"]
                gnote.text = dataObject["text"]
            else:
                print("Not found. Creating new note")
                gnote = k.createNote(dataObject["title"])
                gnote.id = keepId
                gnote.text = dataObject["text"]
            
            gnote.timestamps._created = gnote.timestamps.str_to_dt(dataObject["created"])
            gnote.timestamps._edited = gnote.timestamps.str_to_dt(dataObject["edited"])   
            if "color" in dataObject:
                gnote._color = gkeepapi.node.ColorValue[dataObject["color"]]
            if "parent" in dataObject:
                gnote.parent = dataObject["parent"]
            if "parent_id" in dataObject:
                gnote.parent_id = dataObject["parent_id"]
            if "trashed" in dataObject:
                gnote.timestamps._trashed = gnote.timestamps.str_to_dt(dataObject["trashed"])
            if "updated" in dataObject:
                gnote.timestamps._updated = gnote.timestamps.str_to_dt(dataObject["updated"])
            
            """print(gnote.type, ", ", type(gnote))
            keepNote = {
            "title" : gnote.title, 
            "parent" : gnote.parent, 
            "id" : gnote.id, 
            "server_id" : gnote.server_id, 
            "parent_id" : gnote.parent_id, 
            "version" : gnote.version, 
            "text" : gnote.text, 
            "color" : gnote._color.name, 
            "archived" : gnote._archived, 
            "pinned" : gnote._pinned, 
            "moved" : gnote._moved, 
            "created" : gnote.timestamps.dt_to_str(gnote.timestamps._created), 
            #"deleted" : gnote.timestamps.dt_to_str(gnote.timestamps._deleted), 
            "trashed" : gnote.timestamps.dt_to_str(gnote.timestamps._trashed), 
            "updated" : gnote.timestamps.dt_to_str(gnote.timestamps._updated), 
            "edited" : gnote.timestamps.dt_to_str(gnote.timestamps._edited),
            "parent" : gnote.parent, 
            "children" : gnote._children
            }
            #print(gnote)
            print(keepNote)
            #print()"""
            k.sync()
            self.successCount += 1     
            time.sleep(10)
            #except Exception as exception:
                #traceback.print_exc()
                #self.errorCount += 1
        else:
            print("No dataObject given")
    
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
            dataObject._id = self.id_tag + str(n.id)
            dataObject.version = n.version
            dataObject.color = n._color.name
            dataObject.trashed = n.timestamps.dt_to_str(n.timestamps._trashed)
            dataObject.updated = n.timestamps.dt_to_str(n.timestamps._updated)
            
            objectStore.append(dataObject)
            self.persist(dataObject)
            
        return objectStore
        
    def login (self):
        print("Starting login")
        k = gkeepapi.Keep()
        k.login(self.username, self.password)
        print("login successfull")
        return k


test = keepApiInterface('thsp006@gmail.com', 'TestHSPT3st534')
#result = test.extractFromAPI()
test.requestInjection("notes")#oneNoteApiInterface#")