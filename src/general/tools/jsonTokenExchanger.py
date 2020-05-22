import bidict as bidict

class jsonTokenExchanger:
    bidirectionalDictionaryOfTokensAPIvsObject = bidict.bidict(
        {
            #name attribute api, name attribute python object
            '': '',
        }
    ) 
    
    # these fields must appear on the left side in the bd attribute
    fieldsNotToWriteToAPI = list(
        {
            '',
        }
    )
    
    def convertJSONTokensFromAPIToObjectAsJSON(self, jsonobject):
        for key in self.bidirectionalDictionaryOfTokensAPIvsObject:
            value = jsonobject.pop(key)
            jsonobject[self.bidirectionalDictionaryOfTokensAPIvsObject[key]] = value
        return jsonobject
    
    def convertJSONTokensFromObjectAsJSONToAPI(self, jsonobject):
        listOfNonExistingKeys = dict()
        for key in self.bidirectionalDictionaryOfTokensAPIvsObject.inverse:
            value = jsonobject.pop(key)
            jsonobject[self.bidirectionalDictionaryOfTokensAPIvsObject.inverse[key][0]] = value
        i=0
        for key in jsonobject:
            if key not in self.bidirectionalDictionaryOfTokensAPIvsObject:
                listOfNonExistingKeys[i] = key
                i = i+1
        for key in listOfNonExistingKeys:
            jsonobject.pop(listOfNonExistingKeys[key])
        for key in self.fieldsNotToWriteToAPI:
            jsonobject.pop(key)
        return jsonobject

