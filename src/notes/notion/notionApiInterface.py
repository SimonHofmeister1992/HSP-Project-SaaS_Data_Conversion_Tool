#NotionServiceAPI
#User Name: hspSaaS@gmx.de
#Password: hspTest354

import sys
from datetime import datetime
from notion.client import NotionClient
from notion.block import TextBlock
from notion.block import PageBlock
from notion.collection import Collection
sys.path.append("../../general/")
from notionDataObject import notionDataObject
from baseApiInterface import baseApiInterface


class notionApiInterface (baseApiInterface):
    
    token = ""
    errorCount = 0
    successCount = 0
    client = None
    
    def __init__(self, token):
        """provide the login information with object generation"""
        self.token = token
        self.id_tag = "notes#" + notionApiInterface.__name__ + "#" 
        
    def requestInjection (self, substrIdTag = None):
        """requests the data for Injection into the service and keeps track of the results"""
        
        self.errorCount = 0
        self.successCount = 0
        self.requestInjectionInAPI(notionDataObject, substrIdTag)
        print()
        print("Results: ")
        print("Notes failed to inject: ", self.errorCount)
        print("Notes successfully injected: ", self.successCount)
    
    def injectInAPI (self, dataObject):
        """function for the injection of given data from dict into the service"""
        
        if dataObject != None:
            client = self.login()
            try:
                notionId = dataObject["_id"].split("#")[2]
                #print(keepId)
                notes = client.get_block("d04fb298-0f05-451f-b42c-35f623042d2d")
                note = None
                for child in notes.children:
                    if child.id == notionId:
                        note = child
                        break
                        
                if note is not None:
                    print("Found preexisting Note")
                    note.title = dataObject["title"]
                else:
                    print("Not found. Creating new note")
                    note = notes.children.add_new(PageBlock, title=dataObject["title"])
                
                for child in note.children:
                    child.remove()
                note.children.add_new(TextBlock, title=dataObject["text"])
                
                with note._client.as_atomic_transaction():
                    if hasattr(note, "created_time"):
                        setattr(note, "created_time", datetime.timestamp(datetime.strptime(dataObject["created"], "%Y-%m-%dT%H:%M:%S.%fZ")))
                    if hasattr(note, "last_edited_time"):
                        setattr(note, "last_edited_time", datetime.timestamp(datetime.strptime(dataObject["edited"], "%Y-%m-%dT%H:%M:%S.%fZ")))         
                    if "last_edited_by" in dataObject:
                        if hasattr(note, "last_edited_by"):
                            setattr(note, "last_edited_by", dataObject["last_edited_by"])
                    if "created_by_table" in dataObject:
                        if hasattr(note, "created_by_table"):
                            setattr(note, "created_by_table", dataObject["created_by_table"])
                    if "created_by_id" in dataObject:
                        if hasattr(note, "created_by_id"):
                            setattr(note, "created_by_id", dataObject["created_by_id"])
                    if "last_edited_by_id" in dataObject:
                        if hasattr(note, "last_edited_by_id"):
                            setattr(note, "last_edited_by_id", dataObject["last_edited_by_id"])
                
                self.successCount += 1                 
                return note
            except Exception as exception:
                print("Unexpected error:", sys.exc_info())
                self.errorCount += 1
        else:
            print("No dataObject given")        
    
    def extractFromAPI (self):
        """function for the injection of given data from the service into JSON"""
        client = self.login()
        objectStore = []
        result = client.get_block("d04fb298-0f05-451f-b42c-35f623042d2d")
        for note in result.children:
            data = note._get_record_data()
            text =""
            for textline in note.children:
                text = text + "\n " + textline.title
            notionNote = {
            "title" : note.title,
            "text" : text,
            "edited" : datetime.fromtimestamp(data.get('last_edited_time')/1e3).strftime("%Y-%m-%dT%H:%M:%S.%fZ"), 
            "created" : datetime.fromtimestamp(data.get('created_time')/1e3).strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            "version" : data.get('version'),
            "type" : data.get('type'),
            "parent" : data.get('parent_id'), 
            "parent_table" : data.get('parent_table'),
            "last_edited_by" : data.get('last_edited_by'),
            "alive" : data.get('alive'), 
            "created_by_table" : data.get('created_by_table'), 
            "created_by_id" : data.get('created_by_id'), 
            "last_edited_by_id" : data.get('last_edited_by_id'),
            "id" : data.get('id'), 
            }
            print(notionNote)
            print()
            
            dataObject = notionDataObject()
            dataObject.title = note.title
            dataObject.text = text
            dataObject.edited = datetime.fromtimestamp(data.get('last_edited_time')/1e3).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            dataObject.created = datetime.fromtimestamp(data.get('created_time')/1e3).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            dataObject.version = data.get('version')
            dataObject.type = data.get('type')
            dataObject.parent = data.get('parent_id')
            dataObject.parent_table = data.get('parent_table')
            dataObject.last_edited_by = data.get('last_edited_by')
            dataObject.alive = data.get('alive')
            dataObject.created_by_table = data.get('created_by_table')
            dataObject.created_by_id = data.get('created_by_id')
            dataObject.last_edited_by_id = data.get('last_edited_by_id')
            dataObject._id = self.id_tag + str(data.get('id'))
            
            objectStore.append(dataObject)
            self.persist(dataObject)
            
        return objectStore
        
    def login (self):
        print("Starting login")
        if self.client is None:
            self.client = NotionClient(token_v2=self.token)
        print("login successfull")
        return self.client


test = notionApiInterface("2ba3f0ef5acbfc6296cda29c01958e6ce8558cc6386ce6bc823b6ec952fa63082898567715b0013359a7f60dc7664b8f7acab4988105eb3d68c9e5951349ef6da8bd073d00735102cfbd79ba18de")
#result = test.extractFromAPI()   
test.requestInjection("notes#notionApiInterface#")