import sys
sys.path.append("../")
import dataObject as dataObject
import datastore as datastore

class jsonDatastore(datastore.datastore):
    def persist(self, dataObject):
        """abstract function to persist data objects in a concrete datastore"""
        return     

    def get(self, dataObject):
        """abstract function to get persisted objects in a concrete datastore. Returns a list of dataObjects"""
        #TODO: implement real functionality, not test functions
        dO=dataObject()
        dO.title="blablubb"
        print(dO.title)
        dataO=dataObject()
        dataO.title="biba"
        print(dataO.title)
        return

jD=jsonDatastore()
jD.get(dataObject.dataObject)
