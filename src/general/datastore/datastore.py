import sys
sys.path.append("../../general/")
import dataObject as dataObject

"""interface to persist and request persisted objects"""
class datastore:
    def persist(self, dataObject):
        """abstract function to persist data objects in a concrete datastore"""
        return     

    def get(self, substrIdTag, serviceObject, filterOptions, transformationOptions, addAggOptions):
        """abstract function to get persisted objects in a concrete datastore. Returns a list of dataObjects"""
        return
