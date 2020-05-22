#NotionServiceAPI
import sys, os
from datetime import datetime
from notion.client import NotionClient
from notion.block import TextBlock
from notion.block import PageBlock
from notion.collection import Collection
path = os.path.abspath(os.getcwd())
path = path.split("\\")
path = path[:len(path)-2]
path = "\\".join(path)
path = path+"\\general"
sys.path.insert(0, path)
from baseApiInterface import baseApiInterface
from notionDataObject import notionDataObject

class notionApiInterface (baseApiInterface):
    
    def injectInAPI (self, dataObjects):
        """function for the injection of given data from JSON into the service"""
        client = self.login()
        notes = client.get_block("d04fb298-0f05-451f-b42c-35f623042d2d")
        for objects in dataObjects:
            child = notes.children.add_new(PageBlock, title=objects.title, created_time=objects.created)
            child.created_time = objects.created
            text = objects.text.split("\n")
            for line in text:
                child.children.add_new(TextBlock, title=line)
            
    
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
            "edited" : datetime.fromtimestamp(data.get('last_edited_time')/1e3).strftime("%Y-%m-%dT%H:%M:%S"), 
            "created" : datetime.fromtimestamp(data.get('created_time')/1e3).strftime("%Y-%m-%dT%H:%M:%S"),
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
            dataObject.edited = datetime.fromtimestamp(data.get('last_edited_time')/1e3).strftime("%Y-%m-%dT%H:%M:%S")
            dataObject.created = datetime.fromtimestamp(data.get('created_time')/1e3).strftime("%Y-%m-%dT%H:%M:%S")
            dataObject.version = data.get('version')
            dataObject.type = data.get('type')
            dataObject.parent = data.get('parent_id')
            dataObject.parent_table = data.get('parent_table')
            dataObject.last_edited_by = data.get('last_edited_by')
            dataObject.alive = data.get('alive')
            dataObject.created_by_table = data.get('created_by_table')
            dataObject.created_by_id = data.get('created_by_id')
            dataObject.last_edited_by_id = data.get('last_edited_by_id')
            dataObject.id = data.get('id')
            
            objectStore.append(dataObject)
            
        return objectStore
        
    def login (self):
        print("Starting login")
        client = NotionClient(token_v2="2ba3f0ef5acbfc6296cda29c01958e6ce8558cc6386ce6bc823b6ec952fa63082898567715b0013359a7f60dc7664b8f7acab4988105eb3d68c9e5951349ef6da8bd073d00735102cfbd79ba18de")
        print("login successfull")
        return client


test = notionApiInterface()
#dictionary = {"title" : "test", "text" : "testtext\\n neue Linie", "created" : 1589969512218}
#liste = [dictionary]
#test.injectInAPI(liste)
result = test.extractFromAPI()
for res in result:
    print(res)
    print()