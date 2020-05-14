#KeepServiceAPI
#gkeepapi version 0.11.14
import sys, os
from notion.client import NotionClient
from notion.block import TodoBlock
from notion.collection import Collection
path = os.path.abspath(os.getcwd())
path = path.split("\\")
path = path[:len(path)-2]
path = "\\".join(path)
path = path+"\\general"
sys.path.insert(0, path)
from apiBase import apiBase

class NotionServiceAPI (apiBase):
    
    def inject_in_API (self, attributes):
        """function for the injection of given data from JSON into the service"""
        client = self.login()
        page = client.get_collection_view("https://www.notion.so/4d9514bea6a74f68963116dd7824aa38?v=32c0ab4841714d09a01ee13be1565047")
        #for a in attributes:
            
               
    
    def extract_from_API (self):
        """function for the injection of given data from the service into JSON"""
        client = self.login()
        page = client.get_collection_view("https://www.notion.so/4d9514bea6a74f68963116dd7824aa38?v=32c0ab4841714d09a01ee13be1565047")
        
        datastore = []
        result = page.default_query().execute()
        for row in result:
            note = client.get_block(row.id)
            data = note._get_record_data()
            text =""
            for textline in note.children:
                text = text + " " + textline.title
            notionNote = {
            "title" : note.title,
            "text" : text,
            "edited" : data.get('last_edited_time'), 
            "created" : data.get('created_time'),
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
            datastore.append(notionNote)
        return datastore
        
    def login (self):
        print("Starting login")
        client = NotionClient(token_v2="2ba3f0ef5acbfc6296cda29c01958e6ce8558cc6386ce6bc823b6ec952fa63082898567715b0013359a7f60dc7664b8f7acab4988105eb3d68c9e5951349ef6da8bd073d00735102cfbd79ba18de")
        print("login successfull")
        return client


test = NotionServiceAPI()
#dictionary = {"title" : "test", "text" : "testtext"}
#liste = [dictionary]
#print(test.inject_in_API(liste))
print(test.extract_from_API())