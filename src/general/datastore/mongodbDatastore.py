import sys
import pymongo
sys.path.append("../")
from dataObject import dataObject
from datastore import datastore
import re
import json
from collections import namedtuple

class mongodbDatastore(datastore.datastore):

    def jsonObjectHook(self, d): 
        return namedtuple('X', d.keys())(*d.values())

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
        objectList = list()
        for entry in entries:
            entry['id'] = entry.pop('_id')
            obj=json.loads(json.dumps(entry),object_hook=self.jsonObjectHook)
            dO=dataObjectClass()
            dO.copyValues(obj)
            dO=dO.execCorrectSubclassCastsByNamedTuple(dO)
            print(dO.__dict__)
            dO._id=entry["id"]
            dO.__dict__.pop('id')
            objectList.append(dO)
        return objectList
        
        
    def login(self):
        """create a database Object for localhost mongoDB and returning it"""
        
        client = pymongo.MongoClient("localhost", 27017)
        db = client.SaaS
        return db
