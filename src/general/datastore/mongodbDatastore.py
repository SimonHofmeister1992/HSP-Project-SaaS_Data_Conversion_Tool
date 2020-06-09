import sys
import pymongo
sys.path.append("../")
from dataObject import dataObject
from datastore import datastore
import re

class mongodbDatastore(datastore.datastore):

    def persist(self, dataObject):
        """abstract function to persist data objects in a concrete datastore"""
        
        db = self.login()
        collection = db.SaaSCollection
        dictObject = dataObject.__dict__
        collection.replace_one({'_id': dataObject._id}, dictObject, True)

    def get(self, dataObjectClass, substrIdTag):
        """abstract function to get persisted objects in a concrete datastore. Returns a list of dataObjects"""
        # filteredIdTag is a substring of the id_tag value, like a split to the first or second # to retrieve all entries of a category like calendar / notes or of a concrete service
        db = self.login()
        collection=db.SaaSCollection
        filterOption=re.compile("^" + substrIdTag, re.IGNORECASE)
        entries = collection.find({'id_tag': {'$regex':filterOption}})
        return entries
        
        
    def login(self):
        """create a database Object for localhost mongoDB and returning it"""
        
        client = pymongo.MongoClient("localhost", 27017)
        db = client.SaaS
        return db
