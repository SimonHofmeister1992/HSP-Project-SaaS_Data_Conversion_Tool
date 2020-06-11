import sys
from dataObject import dataObject
from datastore.mongodbDatastore import mongodbDatastore

class baseApiInterface:

    db = mongodbDatastore()
    
    def requestInjectionInAPI (self, dataObject ,substrIdTag = None):
        """requests the data for Injection into the service and provides the methode to do so"""
        #usually called to request data (calendarEvents, notes) from the database and persist it in the service api
        if substrIdTag  is None:
            substrIdTag = serviceObject.id_tag
        self.get(dataObject, substrIdTag, self)
    
    def injectInAPI (self, dataObject):
        """function for the injection of given data from dataObject into the service"""
        #defines the logic how the dataObject is transformed and persisted in the service api, called automatically by wrapper methods
        #get attribute data from JSON and inject it into the service
        print("hello")
        return     
    
    def extractFromAPI (self):
        """function for the injection of given data from the service into dataObject"""
        #get attribute data from service and convert it to JSON
        return 
        
    def persist(self, dataObject):
        """function for the injection of given dataObject into database"""
        self.db.persist(dataObject)
         
    def get(self, dataObjectClass, substrIdTag, serviceObject):
        """function for the extraction of data from database into a dataObject"""
        return self.db.get(dataObjectClass, substrIdTag, serviceObject)
