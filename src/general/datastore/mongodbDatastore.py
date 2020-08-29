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

    def get(self, substrIdTag, serviceObject, filterOptions, transformationOptions, addAggOptions):
        """abstract function to get persisted objects in a concrete datastore. Returns a list of dataObjects
        Also filters and transforms the data according to the given filter and transformation options.
        filterOptions = list with filter expressions
        transformationOptions = list with transformation expressions ($set)
        addAggOptions = list with all additional stages for the aggregation (example: $unset)"""
        # filteredIdTag is a substring of the id_tag value, like a split to the first or second # to retrieve all entries of a category like calendar / notes or of a concrete service
        db = self.login()
        collection=db.SaaSCollection
        print("substringIdTag: "+ substrIdTag)
        idFilter=re.compile("^" + substrIdTag, re.IGNORECASE)
        pipeline = [
            {'$match': {'_id': {'$regex':idFilter}}},
        ]
        #add filterOptions
        print("given filOps: ", filterOptions)
        for filOp in filterOptions:
            print("filOp: ", filOp)
            pipeline.append({'$match':  filOp })
            
        #add transformationOptions
        print("given transOps: ", transformationOptions)
        for transOp in transformationOptions:
            pipeline.append({'$set':  transOp })
        #add additional pipeline stages
        print("given addOps: ", addAggOptions)
        for addOp in addAggOptions:
            pipeline.append(addOp)
        
        print("pipeline: ", pipeline)
        print()
        entries = collection.aggregate(pipeline)
        

        for entry in entries:
            serviceObject.nrToInsert=serviceObject.nrToInsert+1
            #print(entry)
            try:
                serviceObject.injectInAPI(entry)
            except:
                print(str(sys.exc_info()[1]))

        print()
        print("Finished Task")
        return
        
        
    def login(self):
        """create a database Object for localhost mongoDB and returning it"""
        
        client = pymongo.MongoClient("localhost", 27017)
        db = client.SaaS
        return db
