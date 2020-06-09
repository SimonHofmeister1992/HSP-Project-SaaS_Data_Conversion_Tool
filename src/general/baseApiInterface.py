import sys
from dataObject import dataObject
from datastore.mongodbDatastore import mongodbDatastore

class baseApiInterface:

    db = mongodbDatastore()
    
    def injectInAPI (self):
        """function for the injection of given data from dataObject into the service"""
        #get attribute data from JSON and inject it into the service
        return     
    
    def extractFromAPI (self):
        """function for the injection of given data from the service into dataObject"""
        #get attribute data from service and convert it to JSON
        return 
        
    def persist(self, dataObject):
        """function for the injection of given dataObject into database"""
        self.db.persist(dataObject)
         
    def get(self, dataObjectClass, substrIdTag):
        """function for the extraction of data from database into a dataObject"""
        return self.db.get(dataObjectClass, substrIdTag)
