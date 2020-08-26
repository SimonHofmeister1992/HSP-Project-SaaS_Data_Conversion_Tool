import sys
from dataObject import dataObject
from datastore.mongodbDatastore import mongodbDatastore
import logging

class baseApiInterface:

    logger=logging.basicConfig(filename='not.log',level=logging.INFO)
    db = mongodbDatastore()
    id_tag = ""
    nrToInsert=0
    nrInsertedSuccessfully=0
    nrNotNeededToInsert=0
    name= ""
    correspondingDataObjectClass=None
    
    def __init__(self):
        logging.basicConfig(filename='not.log',level=logging.INFO)
        self.logger=logging.getLogger(__name__)
    
    def requestInjectionInAPI (self, substrIdTag = None, filterOptions=[], transformationOptions=[], addAggOptions=[]):
        """requests the data for Injection into the service and provides the methode to do so"""
        #usually called to request data (calendarEvents, notes) from the database and persist it in the service api
        nrToInsert=0
        if substrIdTag  is None:
            substrIdTag = self.id_tag
        self.get(substrIdTag, self, filterOptions, transformationOptions, addAggOptions)
        print("Datasets to be inserted into the api: ", self.nrToInsert)
        print("Datasets successfully inserted into the api: ", self.nrInsertedSuccessfully)
        print("Datasets not needed to insert into the api: ", self.nrNotNeededToInsert)
        print("Datasets failed to insert into the api: ", self.nrToInsert-self.nrInsertedSuccessfully-self.nrNotNeededToInsert)
    
    def injectInAPI (self, dictionary):
        """function for the injection of given data from dict into the service"""
        #defines the logic how the dataObject is transformed and persisted in the service api, called automatically by wrapper methods
        #get attribute data from JSON and inject it into the service
        print(dictionary)
        return     
    
    def extractFromAPI (self):
        """function for the injection of given data from the service into dataObject"""
        #get attribute data from service and convert it to JSON
        return 
        
    def persist(self, dataObject):
        """function for the injection of given dataObject into database"""
        self.db.persist(dataObject)
         
    def get(self, substrIdTag, serviceObject, filterOptions, transformationOptions, addAggOptions):
        """function for the extraction of data from database into a dataObject"""
        return self.db.get(substrIdTag, serviceObject, filterOptions, transformationOptions, addAggOptions)

