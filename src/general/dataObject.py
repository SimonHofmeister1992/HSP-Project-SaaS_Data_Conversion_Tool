from copy import deepcopy

class dataObject(object):
    def copyValues(self, other):
        self.__dict__=other._asdict().copy()
    def execCorrectSubclassCastsByNamedTuple(self, dataObject):
        return dataObject
    #attributes may be added or removed
    #attributes = data for database
    title=""
    text=""
    created=""
    edited=""
    _id=""
