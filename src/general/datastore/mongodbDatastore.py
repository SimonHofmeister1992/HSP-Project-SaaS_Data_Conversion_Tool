import sys
import pymongo
sys.path.append("../")
from dataObject import dataObject
from datastore import datastore
from jsonDatastore import jsonDatastore

class mongodbDatastore(datastore):

    def persist(self, dataObject):
        """abstract function to persist data objects in a concrete datastore"""
        
        db = self.login()
        collection = db.SaaSCollection
        jsonObject = jsonDatastore().convertDataObjectToJSON(dataObject)
        print(type(jsonObject))
        dictObject = dataObject.__dict__
        collection.replace_one({'_id': dataObject._id}, dictObject, True)
        

    def get(self, dataObject):
        """abstract function to get persisted objects in a concrete datastore. Returns a list of dataObjects"""
        
        
        
    def login(self):
        """create a database Object for localhost mongoDB and returning it"""
        
        client = pymongo.MongoClient("localhost", 27017)
        db = client.SaaS
        return db
        
test = mongodbDatastore()
test.persist(dataObject())