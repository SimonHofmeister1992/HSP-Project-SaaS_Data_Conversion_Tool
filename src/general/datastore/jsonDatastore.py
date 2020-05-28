import json
from collections import namedtuple
import sys
sys.path.append("../")
import dataObject as dataObject
import datastore as datastore

class jsonDatastore(datastore.datastore):
    def jsonObjectHook(self, d): 
        return namedtuple('X', d.keys())(*d.values())

    def persist(self, dataObject):
        """abstract function to persist data objects in a concrete datastore"""
        return convertObjectToJSON(dataObject)

    def get(self, dataObject):
        """abstract function to get persisted objects in a concrete datastore. Returns a list of dataObjects"""
        #TODO: implement real functionality, not test functions
        # yet only playing how to pass a class / constructor to be able to create objects out of json
        dO=dataObject()
        dO.title="blablubb"
        print(dO.title)
        dataO=dataObject()
        dataO.title="biba"
        print(dataO.title)
        return

    def convertDataObjectToJSON(self, dataObject):
        '''function to convert an object into json. input: object, output: json-string'''
        dataObjectAsJson=json.dumps(dataObject.__dict__, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        print(dataObjectAsJson)
        return dataObjectAsJson

    def convertJSONToDataObject(self, jsonObjects, dataObjectClass):
        '''function to convert json strings into concrete objects. input: class, output: object'''
        dataObjects=list()
        for jsonObject in jsonObjects:
            obj=json.loads(jsonObject,object_hook=self.jsonObjectHook)
            dO=dataObjectClass()
            dO.copyValues(obj)
            dO=dO.execCorrectSubclassCastsByNamedTuple(dO)
            dataObjects.append(dO)
        return dataObjects
