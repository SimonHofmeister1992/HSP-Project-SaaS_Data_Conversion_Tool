#!/usr/bin/env python
# coding: utf-8

# In[46]:


import requests
import json

import sys
sys.path.append("../../general/")
import login_data as crd
import tokenExchanger as tokenExchanger
import bidict as bidict

# In[62]:


class teamupCalendarApiInterface(tokenExchanger.tokenExchanger):
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
            'Teamup-Token': crd.teamup_api_key
        })
        if not response:
            return 'an error occured requesting the teamup api'
        if response:
            response_content_plain = response.text
            response_content_json = json.loads(response_content_plain)
            events = response_content_json['events'][0]
            parsedEvents = self.convertJSONTokensFromAPIToObjectAsJSON(events)
            return parsedEvents
            # TODO: convert to object
            #return response_content_json['events']
    
    def injectInApi(self, jsonobject):
        reparsedJSON = self.convertJSONTokensFromObjectAsJSONToAPI(jsonobject)
        #TODO: logic to write into the api
        return reparsedJSON


# In[63]:


ti = teamupCalendarApiInterface()


# In[64]:


parsedEvents=ti.extractFromApi()
print(parsedEvents)


# In[65]:


reparsedEvents=ti.injectInApi(parsedEvents)
print(reparsedEvents)

