from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import file_cache

import sys
import pytz
import time
from pytz import timezone as tz
from datetime import datetime, timezone
from dateutil import parser

sys.path.append("../../calendar/google/")
import googleCalendarDataObject as googleCalendarDataObject
sys.path.append('../general/')
import calendarDataObject as calendarDataObject

sys.path.append("../../general/tools/")
from idTable import idTable as idTable

sys.path.append("../../general/")
import baseApiInterface as baseApiInterface

class googleCalendarApiInterface (baseApiInterface.baseApiInterface):

    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/calendar'] # .readonly']
    idTable=idTable()
    authInfo = {"Hint" : "Online-Authentication", "calendarId":"primary"}
    id_tag = "calendar#googleCalendarApiInterface#"
    name = "Google" 
    correspondingDataObjectClass = googleCalendarDataObject.googleCalendarDataObject()
    service=None


    def __init__(self):
        super().__init__()
        self.idTable=idTable()
        self.id_tag = "calendar#" + self.__class__.__name__ + "#"
        self.correspondingDataObjectClass = googleCalendarDataObject.googleCalendarDataObject()
        self.service=self.authenticateOnline()

    def authenticateOnline(self):
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time. credentials.json file and optional token.pickle file (which is also automatically created) required.

        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)

#TODO comment 2 lines with open and pickle.dump
            # Save the credentials for the next run
            # not used here to allow different users to login with the same client
            with open('token.pickle', 'wb') as token:
               pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds, cache_discovery=False)
        return service

    def extractFromAPI(self, shallPersist=True):
        if self.service != None:
            page_token = None
            while True:
                calendar_list = self.service.calendarList().list(pageToken=page_token).execute()
                for calendar_list_entry in calendar_list['items']:
                    if calendar_list_entry["summary"] != "Week Numbers" and calendar_list_entry["summary"] != "Contacts" and calendar_list_entry["summary"] != "Feiertage in Deutschland":
                        print("Calendar: " + calendar_list_entry["summary"])
                        id=calendar_list_entry['id']
                        events_result = self.service.events().list(calendarId=id,# timeMin=now,
                                                    maxResults=None, singleEvents=True,
                                                    orderBy='startTime').execute()
                        events = events_result.get('items', [])
                        if not events:
                            print('    No events found.')
                        for event in events:
                            eventObject = self.parseApiEventToDataObject(event)
                            if shallPersist:
                                self.persist(eventObject)
                            self.idTable.appendPrefetchedIdSet(eventObject._id)
                page_token = calendar_list.get('nextPageToken')
                if not page_token:
                    break

    def injectInAPI (self, dictionary):
        if self.service != None:
            calendarItem = self.adaptDictionaryForAPI(dictionary)
            if calendarItem == None:
                print(dictionary["_id"])
            if calendarItem != None:
                idTag=dictionary["_id"]
                containsId= self.idTable.containsId(idTag)
                if not containsId:
                    calendarItem.pop("_id", None)
                    self.service.events().insert(calendarId=self.authInfo["calendarId"], body=calendarItem).execute()
                    self.nrInsertedSuccessfully=self.nrInsertedSuccessfully+1
                else:
                    self.logger.info(self.__class__.__name__ + ": calendar already contains event: " + dictionary["_id"])
                    self.nrNotNeededToInsert=self.nrNotNeededToInsert+1
            return

    def parseApiEventToDataObject(self, event):
        utctz=tz('Etc/UTC')
        calEvent=googleCalendarDataObject.googleCalendarDataObject()
        #dataObject
        if "summary" in event:
            calEvent.title=event["summary"]
        if "description" in event:
            calEvent.text=event["description"]
        if "created" in event:
            calEvent.created=parser.isoparse(event["created"])
        if "updated" in event:
            calEvent.edited=parser.isoparse(event["updated"])

 

        #calendarDataObject
        if "id" in event:
            calEvent.st_id=event["id"]
            calEvent._id = self.id_tag + event["id"]
        else:
            calEvent._id = self.id_tag + "altKey_" + '_' + str(calEvent.created) + '_' + str(calEvent.title)
        if "endTimeUnspecified" in event:
            calEvent.f_endTimeUnspecified=event["endTimeUnspecified"]
        if "guestsCanModify" in event:
            calEvent.f_guestsCanModify=event["guestsCanModify"]
        if "htmlLink" in event:
            calEvent.st_htmlLink=event["htmlLink"]
        if "iCalUid" in event:
            calEvent.st_iCalUid=event["iCalUid"]
        if "kind" in event:
            calEvent.st_kind=event["kind"]
        if "location" in event:
            calEvent.st_location=event["location"]
        calEvent.f_status=event["status"] if "status" in event else False
        if "transparency" in event:
            calEvent.st_transparency=event["transparency"]
        if "visibility" in event:
            calEvent.st_visibility=event["visibility"]



        if "end" in event:
            calEvent.dt_endTime=calendarDataObject.calendarDataObject.datetime()
            if "date" in event["end"]:
                calEvent.dt_endTime["st_date"]=event["end"]["date"]
            if "dateTime" in event["end"]:
                et=(parser.isoparse(event["end"]["dateTime"])).astimezone(utctz)
                calEvent.dt_endTime["st_date"]=str(et.date())
                calEvent.dt_endTime["st_time"]=str(et.time())
                calEvent.dt_endTime["st_timezone"]='+00:00'

        if "start" in event:
            calEvent.dt_startTime=calendarDataObject.calendarDataObject.datetime()
            if "date" in event["start"]:
                calEvent.dt_startTime["st_date"]=event["start"]["date"]
            if "dateTime" in event["start"]:
                st=(parser.isoparse(event["start"]["dateTime"])).astimezone(utctz)
                calEvent.dt_startTime["st_date"]=str(st.date())
                calEvent.dt_startTime["st_time"]=str(st.time())
                calEvent.dt_startTime["st_timezone"]='+00:00'

        if "originalStartTime" in event:
            calEvent.dt_originalStartTime=calendarDataObject.calendarDataObject.datetime()
            if "date" in event["originalStartTime"]:
                calEvent.dt_originalStartTime["st_date"]=event["originalStartTime"]["date"]
            if "dateTime" in event["originalStartTime"]:
                ot=(parser.isoparse(event["originalStartTime"]["dateTime"])).astimezone(utctz)
                calEvent.dt_originalStartTime["st_date"]=str(ot.date())
                calEvent.dt_originalStartTime["st_time"]=str(ot.time())
                calEvent.dt_originalStartTime["st_timezone"]='+00:00'

        if "recurrence" in event:
            calEvent.rg_recurrence=calendarDataObject.calendarDataObject.recurrence()
            if "recurringEventId" in event["recurrence"]:
                calEvent.rg_recurrence["st_recurringEventId"]=event["recurrence"]["recurringEventId"]


        if "reminders" in event:
            calEvent.rg_reminders=calendarDataObject.calendarDataObject.reminder()
            if "useDefault" in event["reminders"]:
                calEvent.rg_reminder["f_useDefault"]=event["reminders"]["useDefault"]
            if "overrides" in event["reminders"]:
                overrides=[]
                for reminder in event["reminders"]["overrides"]:
                    ovr=calendarDataObject.calendarDataObject.reminder.override()
                    if "minutes" in reminder:
                        ovr["ul_minutes"]=reminder.minutes
                    if "method" in reminder:
                        ovr["st_method"]=reminder.method                        
                    overrides.append(ovr)
                calEvent.rg_reminder["rg_overrides"]=overrides

        if "conferenceData" in event:
            calEvent.rg_conferenceData=calendarDataObject.calendarDataObject.conferenceData()
            if "notes" in event["conferenceData"]:
                calEvent.rg_conferenceData["st_notes"]=event["conferenceData"]["notes"]
            if "signature" in event["conferenceData"]:
                calEvent.rg_conferenceData["st_signature"]=event["conferenceData"]["signature"]
            if "entryPoints" in event["conferenceData"]:
                entryPoints=[]
                for entryPoint in event["conferenceData"]["entryPoints"]:
                    eP=calendarDataObject.calendarDataObject.conferenceData.entryPoint()
                    if "uri" in entryPoint:
                        eP["st_uri"]=entryPoint["uri"]
                    if "accessCode" in entryPoint:
                        eP["st_accessCode"]=entryPoint["accessCode"]
                    if "entryPointType" in entryPoint:
                        eP["st_entryPointType"]=entryPoint["entryPointType"]
                    if "label" in entryPoint:
                        eP["st_label"]=entryPoint["label"]
                    if "meetingCode" in entryPoint:
                        eP["st_meetingCode"]=entryPoint["meetingCode"]
                    if "passcode" in entryPoint:
                        eP["st_passcode"]=entryPoint["passcode"]
                    if "password" in entryPoint:
                        eP["st_password"]=entryPoint["password"]
                    if "pin" in entryPoint:
                        eP["st_pin"]=entryPoint["pin"]
                    entryPoints.append(eP)                       
                calEvent.rg_conferenceData["rg_entryPoints"]=entryPoints

            if "conferenceSolution" in event["conferenceData"]:
                confSolution=calendarDataObject.calendarDataObject.conferenceData.conferenceSolution()
                if "iconUri" in event["conferenceData"]["conferenceSolution"]:
                    confSolution["st_iconUri"]=event["conferenceData"]["conferenceSolution"]["iconUri"]
                if "key" in event["conferenceData"]["conferenceSolution"]:
                    confSolution["rg_key"]=calendarDataObject.calendarDataObject.conferenceData.conferenceSolution.key()
                    if "keyType" in event["conferenceData"]["conferenceSolution"]["key"]:
                        confSolution["rg_key"]["st_keyType"]=event["conferenceData"]["conferenceSolution"]["key"]["keyType"]
                if "name" in event["conferenceData"]["conferenceSolution"]:
                    confSolution["st_name"]=event["conferenceData"]["conferenceSolution"]["name"]                  
                calEvent.rg_conferenceData["rg_conferenceSolution"]=confSolution  

            if "createRequest" in event["conferenceData"]:
                createRequest=calendarDataObject.calendarDataObject.conferenceData.createRequest()
                if "conferenceSolutionKey" in event["conferenceData"]["createRequest"]:
                    createRequest["rg_conferenceSolutionKey"]=calendarDataObject.calendarDataObject.conferenceData.createRequest.conferenceSolutionKey()
                    if "type" in event["conferenceData"]["createRequest"]["conferenceSolutionKey"]:
                        createRequest["rg_conferenceSolutionKey"]["st_type"]=event["conferenceData"]["createRequest"]["conferenceSolutionKey"]["type"]

                if "requestId" in event["conferenceData"]["createRequest"]:
                    createRequest["st_requestId"]=event["conferenceData"]["createRequest"]["requestId"]

                if "status" in event["conferenceData"]["createRequest"]:
                    createRequest["rg_status"]=calendarDataObject.calendarDataObject.conferenceData.createRequest.status()
                    if "statusCode" in event["conferenceData"]["createRequest"]["status"]:
                        createRequest["rg_status"]["st_statusCode"]=event["conferenceData"]["createRequest"]["status"]["statusCode"]                 
 
                calEvent.rg_conferenceData["rg_createRequest"]=createRequest 




        if "attachments" in event:
            calEvent.rg_attachments=[]
            for attachment in event["attachments"]:
                att=calendarDataObject.calendarDataObject.attachment()
                if "title" in attachment:
                    att["st_title"]=attachment["title"]
                if "fileId" in attachment:
                    att["st_fileId"]=attachment["fileId"]
                if "fileUrl" in attachment:
                    att["st_fileUrl"]=attachment["fileUrl"]
                if "iconLink" in attachment:
                    att["st_iconLink"]=attachment["iconLink"]
                if "mimeType" in attachment:
                    att["st_mimeType"]=attachment["mimeType"]
                calEvent.rg_attachments.append(att)

        if "attendees" in event:
            calEvent.rg_attendees=[]
            for attendee in event["attendees"]:
                att=calendarDataObject.calendarDataObject.attendee()
                if "displayName" in attendee:
                    att["st_displayName"]=attendee["displayName"]
                if "email" in attendee:
                    att["st_email"]=attendee["email"]
                if "optional" in attendee:
                    att["f_optional"]=attendee["optional"]
                if "resource" in attendee:
                    att["f_resource"]=attendee["resource"]
                if "displayName" in attendee:
                    att["st_displayName"]=attendee["displayName"]
                if "responseStatus" in attendee:
                    att["st_responseStatus"]=attendee["responseStatus"]
                if "additionalGuests" in attendee:
                    att["ul_additionalGuests"]=attendee["additionalGuests"]
                if "comment" in attendee:
                    att["st_comment"]=attendee["comment"]
                if "id" in attendee:
                    att["st_id"]=attendee["id"]
                if "self" in attendee:
                    att["f_self"]=attendee["self"]
                calEvent.rg_attendees.append(att)

        #googleCalendarDataObject
        if "anyoneCanAddSelf" in event:
            calEvent.f_anyoneCanAddSelf=event["anyoneCanAddSelf"]
        if "attendeesOmitted" in event:
            calEvent.f_attendeesOmitted=event["attendeesOmitted"]
        if "colorId" in event:
            calEvent.st_colorId=event["colorId"]
        if "etag" in event:
            calEvent.st_etag=event["etag"]
        if "guestsCanInviteOthers" in event:
            calEvent.f_guestsCanInviteOthers=event["guestsCanInviteOthers"]
        if "guestsCanSeeOtherGuests" in event:
            calEvent.f_guestsCanSeeOtherGuests=event["guestsCanSeeOtherGuests"]
        if "hangoutLink" in event:
            calEvent.st_hangoutLink=event["hangoutLink"]
        if "locked" in event:
            calEvent.f_locked=event["locked"]
        if "organizer" in event:
            calEvent.rg_organizer=event["organizer"]
        if "privateCopy" in event:
            calEvent.f_privateCopy=event["privateCopy"]
        if "sequence" in event:
            calEvent.ul_sequence=event["sequence"]

        if "creator" in event:
            calEvent.rg_creator=googleCalendarDataObject.googleCalendarDataObject.creator()
            if "displayName" in event["creator"]:
                calEvent.rg_creator["st_displayName"]=event["creator"]["displayName"]
            if "email" in event["creator"]:
                calEvent.rg_creator["st_id"]=event["creator"]["email"]
            if "id" in event["creator"]:
                calEvent.rg_creator["st_id"]=event["creator"]["id"]
            if "self" in event["creator"]:
                calEvent.rg_creator["f_self"]=event["creator"]["self"]

        if "source" in event:
            calEvent.rg_source=googleCalendarDataObject.googleCalendarDataObject.source()
            if "displayName" in event["title"]:
                calEvent.rg_source["st_title"]=event["source"]["title"]
            if "email" in event["url"]:
                calEvent.rg_source["st_url"]=event["source"]["url"]

        if "extendedProperties" in event:
            calEvent.rg_extendedProperties=googleCalendarDataObject.googleCalendarDataObject.extendedProperties()
            if "private" in event["extendedProperties"]:
                calEvent.rg_extendedProperties["rg_private"]=googleCalendarDataObject.googleCalendarDataObject.extendedProperties.key()
                if "(key)" in event["extendedProperties"]["private"]:
                    calEvent.rg_extendedProperties["rg_private"]["st_key"]=event["extendedProperties"]["private"]["(key)"]
            if "shared" in event["extendedProperties"]:
                calEvent.rg_extendedProperties["rg_shared"]=googleCalendarDataObject.googleCalendarDataObject.extendedProperties.key()
                if "(key)" in event["extendedProperties"]["shared"]:
                    calEvent.rg_extendedProperties["rg_shared"]["st_key"]=event["extendedProperties"]["shared"]["(key)"]

        if "gadget" in event:
            calEvent.rg_gadget=googleCalendarDataObject.googleCalendarDataObject.gadget()
            if "preferences" in event["gadget"]:
                calEvent.rg_gadget["rg_preferences"]=googleCalendarDataObject.googleCalendarDataObject.gadget.key()
                if "(key)" in event["gadget"]["preferences"]:
                    calEvent.rg_gadget["rg_preferences"]["st_key"]=event["gadget"]["preferences"]["(key)"]
            if "display" in event["gadget"]:
                calEvent.rg_gadget["st_display"]=event["gadget"]["display"]
            if "height" in event["gadget"]:
                calEvent.rg_gadget["ul_height"]=event["gadget"]["height"]
            if "width" in event["gadget"]:
                calEvent.rg_gadget["ul_width"]=event["gadget"]["width"]
            if "iconLink" in event["gadget"]:
                calEvent.rg_gadget["st_iconLink"]=event["gadget"]["iconLink"]
            if "link" in event["gadget"]:
                calEvent.rg_gadget["st_link"]=event["gadget"]["link"]
            if "title" in event["gadget"]:
                calEvent.rg_gadget["st_title"]=event["gadget"]["title"]
            if "type" in event["gadget"]:
                calEvent.rg_gadget["st_type"]=event["gadget"]["type"]

        return calEvent

    def adaptDictionaryForAPI(self, dictionary):
        if "dt_startTime" in dictionary and "dt_endTime" in dictionary \
            and "st_date" in dictionary["dt_startTime"] and "st_date" in dictionary["dt_endTime"]:
            hasAllTimeValuesStart=True if "st_date" in dictionary["dt_startTime"] and "st_time" in dictionary["dt_startTime"] and "st_timezone" in dictionary["dt_startTime"] else False
            hasAllTimeValuesEnd=True if "st_date" in dictionary["dt_endTime"] and "st_time" in dictionary["dt_endTime"] and "st_timezone" in dictionary["dt_endTime"] else False
            hasAllTimeValuesOriginalStart=True if "dt_originalStartTime" in dictionary and "st_date" in dictionary["dt_originalStartTime"] and "st_time" in dictionary["dt_originalStartTime"] and "st_timezone" in dictionary["dt_originalStartTime"] else False


            calEvent = {
            
            #dataObject
            
            'summary': dictionary["title"] if "title" in dictionary else '',
            'description': dictionary["text"] if "text" in dictionary else '',
#            'created': dictionary["created"].isoformat().split('.')[0]+"+00:00" if "created" in dictionary else None,
#            'updated': dictionary["edited"].isoformat().split('.')[0]+"+00:00" if "edited" in dictionary else None,

            #calendarDataObject

            'start': {
                'dateTime': dictionary["dt_startTime"]["st_date"] + "T" + dictionary["dt_startTime"]["st_time"] + dictionary["dt_startTime"]["st_timezone"] if "st_date" in dictionary["dt_startTime"] and "st_time" in dictionary["dt_startTime"] and "st_timezone" in dictionary["dt_startTime"] else None,
                'date': dictionary["dt_startTime"]["st_date"] if "st_date" in dictionary["dt_startTime"] and not hasAllTimeValuesStart else None,
             },
             'end': {
                'dateTime': dictionary["dt_endTime"]["st_date"] + "T" + dictionary["dt_endTime"]["st_time"] + dictionary["dt_endTime"]["st_timezone"] if "st_date" in dictionary["dt_endTime"] and "st_time" in dictionary["dt_endTime"] and "st_timezone" in dictionary["dt_endTime"] else None,
                'date': dictionary["dt_endTime"]["st_date"] if "st_date" in dictionary["dt_endTime"] and not hasAllTimeValuesEnd else None,
             },

            'originalStartTime': {
                'dateTime': str(datetime.fromisoformat(dictionary["dt_originalStartTime"]["st_date"] + "T" + dictionary["dt_originalStartTime"]["st_time"] + dictionary["dt_originalStartTime"]["st_timezone"])) if "st_date" in dictionary["dt_originalStartTime"] and "st_time" in dictionary["dt_originalStartTime"] and "st_timezone" in dictionary["dt_originalStartTime"] else None,
                'date': dictionary["dt_originalStartTime"]["st_date"] if "st_date" in dictionary["dt_originalStartTime"] and not hasAllTimeValuesOriginalStart else None,
             } if "dt_originalStartTime" in dictionary else None,
 
             'endTimeUnspecified': dictionary["f_endTimeUnspecified"] if "f_endTimeUnspecified" in dictionary else False,
             'guestsCanModify': dictionary["f_guestsCanModify"] if "f_guestsCanModify" in dictionary else False,
             'htmlLink': dictionary["f_htmlLink"] if "f_htmlLink" in dictionary else None,
             'iCalUid': dictionary["f_iCalUid"] if "f_iCalUid" in dictionary else None,
             'kind': dictionary["st_kind"] if "st_kind" in dictionary else None,
             'location': dictionary["st_location"] if "st_location" in dictionary else None,
             'transparency': dictionary["st_transparency"] if "st_transparency" in dictionary else None,
             'visibility': dictionary["st_visibility"] if "st_visibility" in dictionary else None,
             'status': dictionary["f_status"] if "f_status" in dictionary else False,


             'recurrence': [
                 dictionary["rg_recurrence"]["st_recurringEventId"] if "rg_recurrence" in dictionary and "st_recurringEventId" in dictionary["rg_recurrence"] else None
             ],


             #googleCalendarDataObject
             'sequence': dictionary["ul_sequence"] if "ul_sequence" in dictionary else 0,
             'privateCopy': dictionary["f_privateCopy"] if "f_privateCopy" in dictionary else False,
             'organizer': dictionary["rg_organizer"] if "rg_organizer" in dictionary else None,
             'locked': dictionary["f_locked"] if "f_locked" in dictionary else False,
             'hangoutLink': dictionary["st_hangoutLink"] if "st_hangoutLink" in dictionary else None,
             'guestsCanSeeOtherGuests': dictionary["f_guestsCanSeeOtherGuests"] if "f_guestsCanSeeOtherGuests" in dictionary else False,
             'guestsCanInviteOthers': dictionary["f_guestsCanInviteOthers"] if "f_guestsCanInviteOthers" in dictionary else False,
             'etag': dictionary["st_etag"] if "st_etag" in dictionary else None,
             'colorId': dictionary["st_colorId"] if "st_colorId" in dictionary else None,
             'anyoneCanAddSelf': dictionary["f_anyoneCanAddSelf"] if "f_anyoneCanAddSelf" in dictionary else False,
             'attendeesOmitted': dictionary["f_attendeesOmitted"] if "f_attendeesOmitted" in dictionary else False,
        }



            if "rg_attendees" in dictionary:
                attendees=[]
                for attendee in dictionary["rg_attendees"]:
                    att=dict()
                    if "st_displayName" in attendee:
                        att["displayName"] = attendee["st_displayName"]
                    if "st_email" in attendee:
                        att["email"] = attendee["st_email"]
                    if "f_optional" in attendee:
                        att["optional"] = attendee["f_optional"]
                    if "f_organizer" in attendee:
                        att["organizer"] = attendee["f_organizer"]
                    if "f_resource" in attendee:
                        att["resource"] = attendee["f_resource"]
                    if "f_self" in attendee:
                        att["self"] = attendee["f_self"]
                    if "st_responseStatus" in attendee:
                        att["responseStatus"] = attendee["st_responseStatus"] 
                    if "ul_additionalGuests" in attendee:
                        att["additionalGuests"] = attendee["ul_additionalGuests"] 
                    if "st_comment" in attendee:
                        att["comment"] = attendee["st_comment"] 
                    if "st_id" in attendee:
                        att["id"] = attendee["st_id"] 
                    attendees.append(att)
                calEvent["attendees"]=attendees

            if "rg_attachments" in dictionary:
                attachments=[]
                for attachment in dictionary["rg_attachments"]:
                    att=dict()
                    if "st_title" in attachment:
                        att["title"] = attendee["st_title"]
                    if "st_fileId" in attachment:
                        att["fileId"] = attendee["st_fileId"]
                    if "st_fileUrl" in attachment:
                        att["fileUrl"] = attendee["st_fileUrl"]
                    if "st_iconLink" in attachment:
                        att["iconLink"] = attendee["st_iconLink"]
                    if "st_mimeType" in attachment:
                        att["mimeType"] = attendee["st_mimeType"]
                    attachments.append(att)
                calEvent["attachments"]=attachments

            if "rg_conferenceData" in dictionary:
                conferenceData=dict()
                if "st_signature" in dictionary["rg_conferenceData"]:
                    conferenceData["signature"]=dictionary["rg_conferenceData"]["st_signature"]
                if "st_notes" in dictionary["rg_conferenceData"]:
                    conferenceData["notes"]=dictionary["rg_conferenceData"]["st_notes"]
                if "rg_entryPoints" in dictionary["rg_conferenceData"]:
                    entryPoints=[]
                    for entryPoint in dictionary["rg_conferenceData"]["rg_entryPoints"]:
                        eP = dict()
                        if "st_uri" in entryPoint:
                            eP["uri"] = entryPoint["st_uri"]
                        if "st_accessCode" in entryPoint:
                            eP["accessCode"] = entryPoint["st_accessCode"]
                        if "st_entryPointType" in entryPoint:
                            eP["entryPointType"] = entryPoint["st_entryPointType"]
                        if "st_label" in entryPoint:
                            eP["label"] = entryPoint["st_label"]
                        if "st_meetingCode" in entryPoint:
                            eP["meetingCode"] = entryPoint["st_meetingCode"]
                        if "st_passcode" in entryPoint:
                            eP["passcode"] = entryPoint["st_passcode"]
                        if "st_password" in entryPoint:
                            eP["password"] = entryPoint["st_password"]
                        if "st_pin" in entryPoint:
                            eP["pin"] = entryPoint["st_pin"]
                        entryPoints.append(eP)
                    conferenceData["entryPoints"]=entryPoints

                if "rg_conferenceSolution" in dictionary["rg_conferenceData"]:
                    confSol=dict()
                    if "st_iconUri" in dictionary["rg_conferenceData"]["rg_conferenceSolution"]:
                        confSol["iconUri"] = dictionary["rg_conferenceData"]["rg_conferenceSolution"]["st_iconUri"]
                    if "st_name" in dictionary["rg_conferenceData"]["rg_conferenceSolution"]:
                        confSol["name"] = dictionary["rg_conferenceData"]["rg_conferenceSolution"]["st_name"]
                    if "rg_key" in dictionary["rg_conferenceData"]["rg_conferenceSolution"]:
                        key=dict()
                        if "st_keyType" in dictionary["rg_conferenceData"]["rg_conferenceSolution"]["rg_key"]:
                            key["type"] = dictionary["rg_conferenceData"]["rg_conferenceSolution"]["rg_key"]["st_keyType"]
                if "rg_createRequest" in dictionary["rg_conferenceData"]:
                    createReq=dict()
                    if "st_requestId" in dictionary["rg_conferenceData"]["rg_createRequest"]:
                        createReq["requestId"] = dictionary["rg_conferenceData"]["rg_createRequest"]["st_requestId"]
                    if "rg_conferenceSolutionKey" in dictionary["rg_conferenceData"]["rg_createRequest"]:
                        key=dict()
                        if "st_type" in dictionary["rg_conferenceData"]["rg_createRequest"]["rg_conferenceSolutionKey"]:
                            key["type"] = dictionary["rg_conferenceData"]["rg_createRequest"]["rg_conferenceSolutionKey"]["st_type"]
                        createReq["conferenceSolutionKey"]=key
                    if "rg_status" in dictionary["rg_conferenceData"]["rg_createRequest"]:
                        status=dict()
                        if "st_statusCode" in dictionary["rg_conferenceData"]["rg_createRequest"]["rg_status"]:
                            status["statusCode"] = dictionary["rg_conferenceData"]["rg_createRequest"]["rg_status"]["st_statusCode"]
                        createReq["status"]=status

                    conferenceData["createRequest"]=createReq

                calEvent["conferenceData"]=conferenceData

            if "rg_reminder" in dictionary:
                reminders=dict()
                if "f_useDefault" in dictionary["rg_reminder"]:
                    reminders["useDefault"]=dictionary["rg_reminder"]["f_useDefault"]
                if "rg_overrides" in dictionary["rg_reminder"]:
                    overrides=[]
                    for override in dictionary["rg_conferenceData"]["rg_overrides"]:
                        ovr = dict()
                        if "ul_minutes" in override:
                            ovr["minutes"] = override["ul_minutes"]
                        if "st_method" in override:
                            ovr["method"] = override["st_method"]
                        overrides.append(ovr)
                    reminders["overrides"]=overrides
                calEvent["reminders"]=reminders

            if "rg_creator" in dictionary:
                creator=dict()
                if "st_displayName" in dictionary["rg_creator"]:
                    creator["displayName"]=dictionary["rg_creator"]["st_displayName"]
                if "st_email" in dictionary["rg_creator"]:
                    creator["email"]=dictionary["rg_creator"]["st_email"]
                if "st_id" in dictionary["rg_creator"]:
                    creator["id"]=dictionary["rg_creator"]["st_id"]
                if "f_self" in dictionary["rg_creator"]:
                    creator["self"]=dictionary["rg_creator"]["f_self"]
                calEvent["creator"]=creator
            if "rg_source" in dictionary:
                src=dict()
                if "st_title" in dictionary["rg_source"]:
                    src["title"]=dictionary["rg_source"]["st_title"]
                if "st_url" in dictionary["rg_source"]:
                    src["url"]=dictionary["rg_source"]["st_url"]
                calEvent["source"]=src

            if "rg_gadget" in dictionary:
                gadget=dict()
                if "ul_height" in dictionary["rg_gadget"]:
                    gadget["height"]=dictionary["rg_gadget"]["ul_height"]
                if "ul_width" in dictionary["rg_gadget"]:
                    gadget["width"]=dictionary["rg_gadget"]["ul_width"]
                if "st_display" in dictionary["rg_gadget"]:
                    gadget["display"]=dictionary["rg_gadget"]["st_display"]
                if "st_iconLink" in dictionary["rg_gadget"]:
                    gadget["iconLink"]=dictionary["rg_gadget"]["st_iconLink"]
                if "st_title" in dictionary["rg_gadget"]:
                    gadget["title"]=dictionary["rg_gadget"]["st_title"]
                if "st_type" in dictionary["rg_gadget"]:
                    gadget["type"]=dictionary["rg_gadget"]["st_type"]
                if "st_link" in dictionary["rg_gadget"]:
                    gadget["link"]=dictionary["rg_gadget"]["st_link"]
                if "rg_preferences" in dictionary["rg_gadget"]:
                    pref=dict()
                    if "st_key" in dictionary["rg_gadget"]["rg_preferences"]:
                        pref["(key)"]=dictionary["rg_gadget"]["rg_preferences"]["st_key"]
                    gadget["preferences"]=pref
                calEvent["gadget"]=gadget

            if "rg_extendedProperties" in dictionary:
                extProp=dict()
                if "rg_private" in dictionary["rg_extendedProperties"]:
                    private=dict()
                    if "st_key" in dictionary["rg_extendedProperties"]["rg_private"]:
                        private["(key)"]=dictionary["rg_extendedProperties"]["rg_private"]["st_key"]
                    extProp["private"]=private
                if "rg_shared" in dictionary["rg_extendedProperties"]:
                    shared=dict()
                    if "st_key" in dictionary["rg_extendedProperties"]["rg_shared"]:
                        shared["(key)"]=dictionary["rg_extendedProperties"]["rg_shared"]["st_key"]
                    extProp["shared"]=shared
                calEvent["extendedProperties"]=extProp


            calEvent["_id"]=dictionary["_id"]

            calfinal=dict()
            for key in calEvent:
                if calEvent[key] != None:
                    calfinal[key] = calEvent[key]
            
            return calfinal
        return None
  


gcal = googleCalendarApiInterface()
gcal.extractFromAPI(True)
gcal.requestInjectionInAPI(substrIdTag = gcal.id_tag)
