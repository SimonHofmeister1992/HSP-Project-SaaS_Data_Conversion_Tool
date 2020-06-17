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

    def get(self, dataObjectClass, substrIdTag, serviceObject):
        """abstract function to get persisted objects in a concrete datastore. Returns a list of dataObjects"""
        # filteredIdTag is a substring of the id_tag value, like a split to the first or second # to retrieve all entries of a category like calendar / notes or of a concrete service
        db = self.login()
        collection=db.SaaSCollection
        filterOption=re.compile("^" + substrIdTag, re.IGNORECASE)
        entries = collection.find({'_id': {'$regex':filterOption}})
        print("filterOption: ", filterOption, "substrIdTag: ", substrIdTag, "entries: ", entries)
        print("Class: ", dataObjectClass, "serviceObject: ", serviceObject)
        print("start")
        for entry in entries:
            #print("first loop")
            #print(entry)
            entry['id'] = entry.pop('_id')
            obj=json.loads(json.dumps(entry),object_hook=self.jsonObjectHook)
            print("obj: ", obj)
            i=0
            print("dataObject: ", dataObjectClass)
            # go dataObject hierarchy upwards until the id_tags at the viewed position matches, or at a maximum up to the dataObject class, to know the least common interface to fill in the data
            while '#'.join(reversed(obj._id.split('#')))[1:].split('#')[i] != '#'.join(reversed(dataObjectClass()._id.split('#')))[1:].split('#')[i]:
                dataObjectClass=dataObjectClass.__mro__[i]
                i=i+1
                if dataObjectClass.__name__ == "dataObject":
                    #break;
            #print(dataObjectClass)
            dO = dataObjectClass()
            #print(type(dO))
            #dO.__dict__ = entry.copy()
            dO.copyValues(entry)
            dO=dO.execCorrectSubclassCastsByNamedTuple(dO)
            dO._id = obj[-1]
            dO.__dict__.pop('id')
            #print("dataObject: ", type(dO), "do: ", dO)
            #print("values: ")
            #print(dO._id)
            #print(dO.text)
            #print(dO.title)
            #print(dO.created)
            #print(dO.edited)
            #print(dO.version)
            #print(dO.color)
            #print(dO.parent_id)
            
            serviceObject.injectInAPI(dO)
        return
        
        
    def login(self):
        """create a database Object for localhost mongoDB and returning it"""
        
        client = pymongo.MongoClient("localhost", 27017)
        db = client.SaaS
        return db
