import json
import sys
sys.path.append("../")
import dataObject as dataObject
import datastore as datastore

class jsonDatastore(datastore.datastore):
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
        dataObjectAsJson=json.loads(json.dumps(dataObject.__dict__))
        print(dataObjectAsJson)
        return dataObjectAsJson

    def convertJSONToDataObject(self, dataObject):
        '''function to convert json strings into concrete objects. input: class, output: object'''
        # not yet implemented
        return


#TODO: TEST-CODE ONLY, REMOVE BEFORE PRODUCTION USE

#jD=jsonDatastore()
#jD.get(dataObject.dataObject)
#dO=dataObject.dataObject()
#dO.title="Hannibal"
#dO.text="description"
#dOAJ=jD.persist(dO)
#print("return values: ")
#print("title: ", dOAJ["title"])
#print("text: ", dOAJ["text"])
