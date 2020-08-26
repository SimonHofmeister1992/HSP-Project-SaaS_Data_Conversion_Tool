import requests
import json
import time
from datetime import datetime, timezone
import sys

sys.path.append("../../calendar/teamup/")
import loginData as crd
import teamupCalendarDataObject as teamupCalendarDataObject

sys.path.append("../../general/tools/")
import jsonTokenExchanger as jsonTokenExchanger
from idTable import idTable as idTable
import bidict as bidict
sys.path.append("../../general/")
import baseApiInterface as baseApiInterface



class teamupCalendarApiInterface(baseApiInterface.baseApiInterface,jsonTokenExchanger.jsonTokenExchanger):
    
    lastValidSubCalendarId=None
    idTable=idTable()
    authInfo = {"teamupApiKey" : "", "calendarId" : ""}
    id_tag = "calendar#teamupCalendarApiInterface#"
    name = "Teamup" 
    correspondingDataObjectClass = teamupCalendarDataObject.teamupCalendarDataObject()

    def __init__(self, uniqueCalendarId=None, subCalendarId=None):
        
        super().__init__()
        self.uniqueCalendarId=uniqueCalendarId
        self.subCalendarId=subCalendarId
        self.idTable=idTable()
        self.teamupApiKey = crd.teamupApiKey
        self.id_tag = "calendar#" + self.__class__.__name__ + "#"
        self.correspondingDataObjectClass = teamupCalendarDataObject.teamupCalendarDataObject()

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
    
    def extractFromAPI(self, shallPersist=True):
        if self.authInfo["teamupApiKey"] != "" and self.authInfo["teamupApiKey"] != None:
            self.teamupApiKey = self.authInfo["teamupApiKey"]
        if self.authInfo["calendarId"] != "" and self.authInfo["calendarId"] != None:
            self.uniqueCalendarId = self.authInfo["calendarId"]

        response = requests.get('https://api.teamup.com/' + self.uniqueCalendarId + '/events?startDate=2017-08-01&endDate=2023-08-01', headers={
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
                if shallPersist:
                    self.persist(eventObject)
                self.idTable.appendPrefetchedIdSet(eventObject._id)
            return

    
    def injectInAPI (self, dictionary):
        if self.authInfo["teamupApiKey"] != "" and self.authInfo["teamupApiKey"] != None:
            self.teamupApiKey = self.authInfo["teamupApiKey"]
        if self.authInfo["calendarId"] != "" and self.authInfo["calendarId"] != None:
            self.uniqueCalendarId = self.authInfo["calendarId"]
        self.extractFromAPI(shallPersist=False)
        adaptedDictionary=self.adaptDictionaryForAPI(dictionary)
        if adaptedDictionary == None:
            print(dictionary["_id"])
        if adaptedDictionary != None:
            idTag=dictionary["_id"]
            containsId= self.idTable.containsId(idTag)
            if not containsId:
                print("persist in api")
                response = requests.post('https://api.teamup.com/' + self.uniqueCalendarId + '/events', headers={
                    'Teamup-Token': self.teamupApiKey,
                }, json=adaptedDictionary)
                print(response.text)
                self.nrInsertedSuccessfully=self.nrInsertedSuccessfully+1
            else:
                self.logger.info(self.__class__.__name__ + ": calendar already contains event: " + dictionary["_id"])
                self.nrNotNeededToInsert=self.nrNotNeededToInsert+1
        return

    def adaptDictionaryForAPI(self, dictionary):
        newdict= dict()
        ##### subcalendar to write to #####
        if 'st_subcalendarId' in dictionary and dictionary['st_subcalendarId'] != None:
            newdict['subcalendar_id'] = dictionary['st_subcalendarId']
            self.lastValidSubCalendarId=dictionary['st_subcalendarId']
        elif 'st_subcalendarIds' in dictionary and dictionary['st_subcalendarIds'] != None:
            newdict['subcalendar_id'] = dictionary['st_subcalendarIds'].split(',')[0]
            self.lastValidSubCalendarId=dictionary['st_subcalendarIds'][0].split(',')[0]
        elif self.subCalendarId != None:
            newdict['subcalendar_id'] = self.subCalendarId
            self.lastValidSubCalendarId=self.subCalendarId
        elif self.lastValidSubCalendarId != None:
            newdict['subcalendar_id'] = self.lastValidSubCalendarId
        else:
            ### remove event if no subcalendar is known where to write the event data ### 
            self.logger.info(self.__class__.__name__ + ": calendar event cannot be inserted in unknown subcalendar: " + dictionary["_id"])
            return None
        ##### start date #######
        startDate=datetime.fromisoformat(dictionary['dt_startTime']['st_date']+'T'+dictionary['dt_startTime']['st_time']+dictionary['dt_startTime']['st_timezone'])
        now=datetime.utcnow()
        now=str(now.year)+'-'+str("{:02d}".format(now.month))+'-'+str("{:02d}".format(now.day))+'T'+str("{:02d}".format(now.hour))+':'+str("{:02d}".format(now.minute))+':'+str("{:02d}".format(now.second))
        nowDt=datetime.fromisoformat(now)

        newdict['start_dt'] = dictionary['dt_startTime']['st_date']+'T'+dictionary['dt_startTime']['st_time']+dictionary['dt_startTime']['st_timezone']
        ##### end date ####
        if 'dt_endTime' in dictionary and dictionary['dt_endTime'] != None:
            newdict['end_dt'] = dictionary['dt_endTime']['st_date']+'T'+dictionary['dt_endTime']['st_time']+dictionary['dt_endTime']['st_timezone']
        ##### 
        if 'f_status' in dictionary and dictionary['f_status'] != None:
            self.logger.info(self.__class__.__name__ + ": calendar event is marked as deleted: " + dictionary["_id"])
            return None
        if 'rg_attendees' in dictionary and dictionary['rg_attendees'] != None:
            who=''
            for attendee in dictionary['rg_attendees']:
                who=who+','+attendee['st_email'].replace(',','')
            newdict['who']=who
        if 'dt_originalStartTime' in dictionary and dictionary['dt_originalStartTime'] != None:
            newdict['rsstart_dt'] = datetime.fromisoformat(dictionary['dt_originalStartTime']['st_date']+'T'+dictionary['dt_originalStartTime']['st_time']+dictionary['dt_originalStartTime']['st_timezone'])
            newdict['tz'] = dictionary['dt_originalStartTime']['st_timezone']
        ###### trivial attributes ######
        if 'title' in dictionary and dictionary['title'] != None:
            newdict['title'] = dictionary['title']
        if 'text' in dictionary and dictionary['text'] != None:
            newdict['notes'] = dictionary['text']
        if 'st_subcalendarIds' in dictionary and dictionary['st_subcalendarIds'] != None:
            newdict['subcalendar_ids'] = dictionary['st_subcalendarIds']
        if 'st_seriesId' in dictionary and dictionary['st_seriesId'] != None:
            newdict['series_id'] = dictionary['st_seriesId']
        if 'f_endTimeUnspecified' in dictionary and dictionary['f_endTimeUnspecified'] != None:
            newdict['all_day'] = dictionary['f_endTimeUnspecified']
        if 'created' in dictionary and dictionary['created'] != None:
            newdict['creation_dt'] = dictionary['created'].replace(tzinfo=timezone.utc).isoformat()
        if 'edited' in dictionary and dictionary['edited'] != None:
            newdict['update_dt'] = dictionary['edited'].replace(tzinfo=timezone.utc).isoformat()
        if 'f_guestsCanModify' in dictionary and dictionary['f_guestsCanModify'] != None:
            newdict['readonly'] = dictionary['f_guestsCanModify']
        if 'st_location' in dictionary and dictionary['st_location'] != None:
            newdict['location'] = dictionary['st_location']


            ### filter and remove past events ###
        try:
            if not nowDt < startDate:
                self.logger.info(self.__class__.__name__ + ": calendar event is in the past: " + dictionary["_id"])
                self.nrNotNeededToInsert=self.nrNotNeededToInsert+1
                return None
        except:
            now = now + '+00:00'
            nowDt=datetime.fromisoformat(now)
            if not nowDt < startDate:
                self.logger.info(self.__class__.__name__ + ": calendar event is in the past: " + dictionary["_id"])
                self.nrNotNeededToInsert=self.nrNotNeededToInsert+1
                return None
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
        dataObject.created=datetime.fromisoformat(str(parsedEvent["created"])).replace(tzinfo=timezone.utc)
        if parsedEvent["edited"] != None:
            dataObject.edited=datetime.fromisoformat(str(parsedEvent["edited"])).replace(tzinfo=timezone.utc)
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
            att["st_email"]=attendee.replace(',','')
            dataObject.rg_attendees.append(att)
        dataObject.dt_endTime=teamupCalendarApiInterface.timeConverterApiToObject(parsedEvent["end_dt"])
        dataObject.dt_startTime=teamupCalendarApiInterface.timeConverterApiToObject(parsedEvent["start_dt"])
        dataObject.dt_originalStartTime=teamupCalendarApiInterface.timeConverterApiToObject(parsedEvent["rsstart_dt"])
        dataObject._id = self.id_tag + dataObject.st_id
        if dataObject._id == self.id_tag:
            dataObject._id = self.id_tag + "altKey_" + str(dataObject.st_subcalendarIds[0]) + '_' + parsedEvent["start_dt"] + '_' + dataObject.title
        return dataObject
#TODO: TEST-CODE ONLY, REMOVE BEFORE PRODUCTION USE

#ti=teamupCalendarApiInterface('kst496bmane3rty9b7', None)
#parsedEvents=ti.extractFromAPI()
#events=ti.requestInjectionInAPI(teamupCalendarDataObject.teamupCalendarDataObject().id_tag.split('#')[0])





