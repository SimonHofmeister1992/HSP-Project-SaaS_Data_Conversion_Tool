import requests
import json

import sys
import loginData as crd
import teamupCalendarDataObject as teamupCalendarDataObject
sys.path.append("../../general/tools/")
import jsonTokenExchanger as jsonTokenExchanger
import bidict as bidict
sys.path.append("../../general/")
import baseApiInterface as baseApiInterface

class teamupCalendarApiInterface(baseApiInterface.baseApiInterface,jsonTokenExchanger.jsonTokenExchanger):
    uniqueCalendarId='kst496bmane3rty9b7'
    
    bidirectionalDictionaryOfTokensAPIvsObject = bidict.bidict(
        {
            #name attribute api, name attribute python object
            'title': 'title',
            'notes': 'text',
            'creation_dt': 'created',
            'update_dt' : 'edited',
            'id': 'st_id',
            'version': 'st_version',
        }
    ) 
    
    # these fields must appear on the left side in the bd attribute
    fieldsNotToWriteToAPI = list(
        {
            'id',
            'version',
        }
    )
    
    def extractFromApi(self):
        response = requests.get('https://api.teamup.com/' + self.uniqueCalendarId + '/events?startDate=2017-08-01&endDate=2021-08-01', headers={
            'Teamup-Token': crd.teamupApiKey
        })
        if not response:
            return 'an error occured requesting the teamup api'
        if response:
            responseContentPlain = response.text
            responseContentJson = json.loads(responseContentPlain)
            events = responseContentJson['events'][0]
            parsedEvents = self.convertJSONTokensFromAPIToObjectAsJSON(events)
            return parsedEvents
            # TODO: convert to object
            #return response_content_json['events']
    
    def injectInApi(self, jsonobject):
        reparsedJSON = self.convertJSONTokensFromObjectAsJSONToAPI(jsonobject)
        #TODO: logic to write into the api
        return reparsedJSON

ti = teamupCalendarApiInterface()
parsedEvents=ti.extractFromApi()
print(parsedEvents)

dataObject = teamupCalendarDataObject.teamupCalendarDataObject()
dataObject.title=parsedEvents["title"]
print("content title: ",dataObject.title)

reparsedEvents=ti.injectInApi(parsedEvents)
print(reparsedEvents)

