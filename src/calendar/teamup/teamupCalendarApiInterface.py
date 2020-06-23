import requests
import json
import time
from datetime import datetime

import loginData as crd
import teamupCalendarDataObject as teamupCalendarDataObject


import sys
sys.path.append("../../general/tools/")
import jsonTokenExchanger as jsonTokenExchanger
import bidict as bidict
sys.path.append("../../general/")
import baseApiInterface as baseApiInterface



class teamupCalendarApiInterface(baseApiInterface.baseApiInterface,jsonTokenExchanger.jsonTokenExchanger):
    
    lastValidSubCalendarId=None

    def __init__(self, uniqueCalendarId, subCalendarId):
        self.uniqueCalendarId=uniqueCalendarId
        self.subCalendarId=subCalendarId

    bidirectionalDictionaryOfTokensAPIvsObject = bidict.bidict(
        {
            #name attribute api, name attribute python object
            'title': 'title',
            'notes': 'text',
            'creation_dt': 'created',
            'update_dt' : 'edited',
            'id': 'st_id',
            'version': 'st_version',
           # 'duration': 'ul_duration',
            'subcalendar_id': 'st_subcalendarId',
            'subcalendar_ids': 'st_subcalendarIds',
            'delete_dt': 'st_status',
            'all_day': 'f_endTimeUnspecified',
            'readonly': 'f_guestsCanModify',
            'remote_id': 'st_remoteId',
            'location': 'st_location',
            'tz': 'st_timezone',
            'series_id':'st_recurringEventId'
        }
    ) 
    
    # these fields must appear on the left side in the bd attribute
    fieldsNotToWriteToAPI = list(
        {
           # 'id',
           # 'duration',
            'delete_dt',
            'series_id',
            'rsstart_dt',
            'readonly',
            'creation_dt',
            'update_dt',
            'delete_dt',
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
            for event in responseContentJson['events']:
                parsedEvent = self.convertJSONTokensFromAPIToObjectAsJSON(event)
                eventObject= self.createSingleObjectByJSON(parsedEvent)
                self.persist(eventObject)
            return
    
    def injectInAPI (self, dictionary):
        adaptedDictionary=self.adaptDictionaryForAPI(dictionary)
        #if adaptedDictionary != None:
        #    print(adaptedDictionary)
        #    response = requests.post('https://api.teamup.com/' + self.uniqueCalendarId + '/events', headers={
        #        'Teamup-Token': crd.teamupApiKey,
        #    }, json=adaptedDictionary)
        #    print(response.text)
        return

    def adaptDictionaryForAPI(self, dictionary):
        newdict= dict()
        ##### subcalendar to write to #####
        if not hasattr(dictionary, 'st_subcalendarId'):
            newdict['subcalendar_id'] = dictionary['st_subcalendarId']
            self.lastValidSubCalendarId=dictionary['st_subcalendarId']
        elif not hasattr(dictionary, 'st_subcalendarIds'):
            newdict['subcalendar_id'] = dictionary['st_subcalendarIds'].split(',')[0]
            self.lastValidSubCalendarId=dictionary['st_subcalendarIds'][0].split(',')[0]
        elif self.subCalendarId != None:
            newdict['subcalendar_id'] = self.subCalendarId
            self.lastValidSubCalendarId=self.subCalendarId
        elif self.lastValidSubCalendarId != None:
            newdict['subcalendar_id'] = self.lastValidSubCalendarId
        else:
            ### remove event if no subcalendar is known where to write the event data ### 
            return None
        ##### start date #######
        startDate=datetime.fromisoformat(dictionary['dt_startTime']['st_date']+'T'+dictionary['dt_startTime']['st_time']+dictionary['dt_startTime']['st_timezone'])
        now=datetime.utcnow()
        now=str(now.year)+'-'+str("{:02d}".format(now.month))+'-'+str("{:02d}".format(now.day))+'T'+str("{:02d}".format(now.hour))+':'+str("{:02d}".format(now.minute))+':'+str("{:02d}".format(now.second))+'+00:00'
        now=datetime.fromisoformat(now)
            ### filter and remove past events ###
        if not now < startDate:
            return None
        newdict['dt_start'] = startDate
        ##### end date ####
        if 'dt_endTime' in dictionary:
            newdict['end_dt'] = datetime.fromisoformat(dictionary['dt_endTime']['st_date']+'T'+dictionary['dt_endTime']['st_time']+dictionary['dt_endTime']['st_timezone'])
        
        ###### trivial attributes ######
        newdict['title'] = dictionary['title']
        newdict['notes'] = dictionary['text']
        print(newdict)
        return newdict

    def timeConverterApiToObject(datetime):
        if datetime != None:
            dt=teamupCalendarDataObject.teamupCalendarDataObject.datetime()
            date=datetime.split("T")
            dt["st_date"]=date[0]
            dt["st_time"]=date[1][:8]
            dt["st_timezone"]=date[1][8:]
            return dt

    def createSingleObjectByJSON(self, parsedEvent):
        dataObject = teamupCalendarDataObject.teamupCalendarDataObject()
        dataObject.title=parsedEvent["title"]
        if parsedEvent["text"] != None:
            dataObject.text=parsedEvent["text"].replace("<p>","",1).replace("</p>","",1)
        dataObject.created=parsedEvent["created"]
        dataObject.edited=parsedEvent["edited"]
        dataObject.st_version=parsedEvent["st_version"]
        #dataObject.ul_duration=parsedEvent["ul_duration"]
        dataObject.st_subcalendarId=parsedEvent["st_subcalendarId"]
        dataObject.st_subcalendarIds=parsedEvent["st_subcalendarIds"]
        dataObject.f_endTimeUnspecified=parsedEvent["f_endTimeUnspecified"]
        dataObject.f_guestsCanModify=parsedEvent["f_guestsCanModify"]
        dataObject.st_recurringEventId=parsedEvent["st_recurringEventId"]
        dataObject.st_remoteId=parsedEvent["st_remoteId"]
        dataObject.st_location=parsedEvent["st_location"]
        dataObject.st_timezone=parsedEvent["st_timezone"]
        if parsedEvent["st_status"] != None:
            dataObject.st_status='cancelled'
        else:
            dataObject.st_status='confirmed'
        for attendee in parsedEvent["who"].split("; "):
            att=teamupCalendarDataObject.teamupCalendarDataObject.attendee()
            att["st_email"]=attendee
            dataObject.rg_attendees.append(att)
        dataObject.dt_endTime=teamupCalendarApiInterface.timeConverterApiToObject(parsedEvent["end_dt"])
        dataObject.dt_startTime=teamupCalendarApiInterface.timeConverterApiToObject(parsedEvent["start_dt"])
        dataObject.dt_originalStartTime=teamupCalendarApiInterface.timeConverterApiToObject(parsedEvent["rsstart_dt"])
        dataObject._id = dataObject.id_tag + dataObject.st_id
        if dataObject._id == dataObject.id_tag:
            dataObject._id = dataObject.id_tag + "altKey_" + str(dataObject.st_subcalendarIds[0]) + '_' + parsedEvent["start_dt"] + '_' + dataObject.title
        return dataObject
#TODO: TEST-CODE ONLY, REMOVE BEFORE PRODUCTION USE

ti=teamupCalendarApiInterface('kst496bmane3rty9b7', None)
#parsedEvents=ti.extractFromApi()
events=ti.requestInjectionInAPI(teamupCalendarDataObject.teamupCalendarDataObject,teamupCalendarDataObject.teamupCalendarDataObject().id_tag.split('#')[0])

