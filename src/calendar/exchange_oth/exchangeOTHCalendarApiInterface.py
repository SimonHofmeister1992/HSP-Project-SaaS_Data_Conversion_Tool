import exchangelib
from exchangelib import DELEGATE, Account, Configuration, Credentials, CalendarItem, EWSDateTime, Attendee, Mailbox
from exchangelib.autodiscover import AutodiscoverProtocol
import sys
import pytz
import time
from pytz import timezone as tz
from datetime import datetime, timezone
sys.path.append('../exchange_oth/')
import exchangeOTHCalendarDataObject as exchangeOTHCalendarDataObject
sys.path.append('../general/')
import calendarDataObject as calendarDataObject
sys.path.append("../../general/tools/")
import jsonTokenExchanger as jsonTokenExchanger
from idTable import idTable as idTable
import bidict as bidict
sys.path.append("../../general/")
import baseApiInterface as baseApiInterface

class exchangeOTHCalendarInterface(baseApiInterface.baseApiInterface, jsonTokenExchanger.jsonTokenExchanger):

    idTable=idTable()
    authInfo={"server": "exchange.othr.de", "username_with_domain":"", "password":"", "email":""}

    id_tag= "calendar#exchangeOTHCalendarApiInterface#"
    name="OTH Exchange"
    correspondingDataObjectClass=exchangeOTHCalendarDataObject.exchangeOTHCalendarDataObject()

    def __init__(self):
        super().__init__()
        self.idTable=idTable()
        self.id_tag="calendar#" + self.__class__.__name__ + "#"
        self.correspondingDataObjectClass=exchangeOTHCalendarDataObject.exchangeOTHCalendarDataObject()
    
    def extractFromAPI(self, shallPersist=True):
        if self.authInfo["server"] != "" and self.authInfo["server"] != None and self.authInfo["username_with_domain"] != "" and \
           self.authInfo["username_with_domain"] != None and self.authInfo["password"] != "" and self.authInfo["password"] != None and \
           self.authInfo["email"] != "" and self.authInfo["email"] != None:
           credentials = Credentials(username=self.authInfo['username_with_domain'], password=self.authInfo['password'])
           config = Configuration(server=self.authInfo['server'], credentials=credentials)
           account = Account(primary_smtp_address=self.authInfo['email'], config=config,
                   autodiscover=False, access_type=DELEGATE)

           for calendar_item in account.calendar.all(): #all().order_by('datetime_received')
               self.handleGetCalendarItem(calendar_item, shallPersist)
           for cal in account.calendar.tree().split('\n'):
               while cal[0] < '0' or cal[0] > 'z':
                   cal = cal[1:]
               if cal != 'Kalender' and cal != 'Calendar':
                   for calendar_item in (account.calendar / cal).all():
                       self.handleGetCalendarItem(calendar_item, shallPersist)


    def injectInAPI (self, dictionary):
        
        if self.authInfo["server"] != "" and self.authInfo["server"] != None and self.authInfo["username_with_domain"] != "" and \
           self.authInfo["username_with_domain"] != None and self.authInfo["password"] != "" and self.authInfo["password"] != None and \
           self.authInfo["email"] != "" and self.authInfo["email"] != None:

            credentials = Credentials(username=self.authInfo['username_with_domain'], password=self.authInfo['password'])
            config = Configuration(server=self.authInfo['server'], credentials=credentials)
            account = Account(primary_smtp_address=self.authInfo['email'], config=config,autodiscover=False, access_type=DELEGATE)

            
            self.extractFromAPI(shallPersist=False)
            calendarItem=self.adaptDictionaryForAPI(dictionary,account)
                       

            if calendarItem == None:
                print(dictionary["_id"])
            if calendarItem != None:
                idTag=dictionary["_id"]
                containsId= self.idTable.containsId(idTag)
                if not containsId:
                    calendarItem.save()
                    self.nrInsertedSuccessfully=self.nrInsertedSuccessfully+1
                else:
                    self.logger.info(self.__class__.__name__ + ": calendar already contains event: " + dictionary["_id"])
                    self.nrNotNeededToInsert=self.nrNotNeededToInsert+1
            return
    
    def adaptDictionaryForAPI(self, dictionary, account):
        utctz=tz('UTC')
        if "dt_startTime" in dictionary:
             calItem = CalendarItem(

                 folder=account.calendar,

                 #dataObject
                  
                 subject=dictionary["title"] if dictionary["title"] != '' else '', 
                 text_body=dictionary["text"] if dictionary["text"] != '' else '',
                 datetime_created=utctz.localize(EWSDateTime.from_datetime(dictionary["created"])) if dictionary["created"] != '' else None,
                 last_modified_time=utctz.localize(EWSDateTime.from_datetime(dictionary["edited"])) if dictionary["edited"] != '' else None,

                 #calendarDataObject
                 sensitivity=dictionary["st_visibility"] if "st_visibility" in dictionary else '',
                 legacy_free_busy_status=dictionary["st_transparency"] if "st_transparency" in dictionary else '',
                 duration=dictionary["ul_duration"] if "ul_duration" in dictionary else '',
                 location=dictionary["st_location"] if "st_location" in dictionary else '',
                 item_class=dictionary["st_kind"] if "st_kind" in dictionary else '',
                 web_client_read_form_query_string=dictionary["st_htmlLink"] if "st_htmlLink" in dictionary else '',
                 #itemid=dictionary["st_id"] if "st_id" in dictionary else '',
                 is_all_day=dictionary["f_endTimeUnspecified"] if "f_endTimeUnspecified" in dictionary else False,
                 is_cancelled=True if dictionary["st_status"] == "cancelled" else False,

                 meeting_workspace_url=dictionary["rg_conferenceData"]["rg_entryPoints"][0]["st_uri"] if "rg_conferenceData" in dictionary and "rg_entryPoints" in dictionary["rg_conferenceData"] and len(dictionary["rg_conferenceData"]["rg_entryPoints"])>=1 else '',

                 net_show_url=dictionary["rg_conferenceData"]["rg_entryPoints"][0]["st_netShowUrl"] if "rg_conferenceData" in dictionary and "rg_entryPoints" in dictionary["rg_conferenceData"] and len(dictionary["rg_conferenceData"]["rg_entryPoints"])>=1 else '',

                 reminder_minutes_before_start=dictionary["rg_reminder"]["rg_overrides"]["st_netShowUrl"] if "rg_reminder" in dictionary and "rg_overrides" in dictionary["rg_reminder"] else 0,
                 
                  start=EWSDateTime.from_datetime(datetime(int(dictionary["dt_startTime"]["st_date"].split('-')[0]), int(dictionary["dt_startTime"]["st_date"].split('-')[1]), int(dictionary["dt_startTime"]["st_date"].split('-')[2]), int(dictionary["dt_startTime"]["st_time"].split(':')[0]), int(dictionary["dt_startTime"]["st_time"].split(':')[1]), int(dictionary["dt_startTime"]["st_time"].split(':')[2]), 0, pytz.UTC)) if "dt_startTime" in dictionary else None,
                  end=EWSDateTime.from_datetime(datetime(int(dictionary["dt_endTime"]["st_date"].split('-')[0]), int(dictionary["dt_endTime"]["st_date"].split('-')[1]), int(dictionary["dt_endTime"]["st_date"].split('-')[2]), int(dictionary["dt_endTime"]["st_time"].split(':')[0]), int(dictionary["dt_endTime"]["st_time"].split(':')[1]), int(dictionary["dt_endTime"]["st_time"].split(':')[2]), 0, pytz.UTC)) if "dt_endTime" in dictionary else None,
                  

                  original_start=EWSDateTime.from_datetime(datetime(int(dictionary["dt_originalStartTime"]["st_date"].split('-')[0]), int(dictionary["dt_originalStartTime"]["st_date"].split('-')[1]), int(dictionary["dt_originalStartTime"]["st_date"].split('-')[2]), int(dictionary["dt_originalStartTime"]["st_time"].split(':')[0]), int(dictionary["dt_originalStartTime"]["st_time"].split(':')[1]), int(dictionary["dt_originalStartTime"]["st_time"].split(':')[2]), 0, pytz.UTC)) if "dt_originalStartTime" in dictionary else None,

                 recurrence=Recurrence(
                     pattern=dictionary["rg_recurrence"]["pattern"] if "pattern" in dictionary["rg_recurrence"] else None,
                     start=utctz.localize(EWSDateTime.from_datetime(datetime(int(dictionary["dt_startTime"]["st_date"].split('-')[0]), int(dictionary["dt_startTime"]["st_date"].split('-')[1]), int(dictionary["dt_startTime"]["st_date"].split('-')[2]), int(dictionary["dt_startTime"]["st_time"].split(':')[0]), int(dictionary["dt_startTime"]["st_time"].split(':')[1]), int(dictionary["dt_startTime"]["st_time"].split(':')[2]), 0, pytz.UTC))) if "dt_startTime" in dictionary else None,
                 ) if "rg_recurrence" in dictionary else None,

                 #first_occurence=utctz.localize(EWSDateTime.from_datetime(datetime(int(dictionary["dt_firstOccurence"]["st_date"].split('-')[0]), int(dictionary["dt_firstOccurence"]["st_date"].split('-')[1]), int(dictionary["dt_firstOccurence"]["st_date"].split('-')[2]), int(dictionary["dt_firstOccurence"]["st_time"].split(':')[0]), int(dictionary["dt_firstOccurence"]["st_time"].split(':')[1]), int(dictionary["dt_firstOccurence"]["st_time"].split(':')[2]), 0, pytz.UTC))) if "rg_recurrence" in dictionary and "dt_firstOccurence" in dictionary["rg_recurrence"] else None,

                 last_occurrence=utctz.localize(EWSDateTime.from_datetime(datetime(int(dictionary["dt_lastOccurence"]["st_date"].split('-')[0]), int(dictionary["dt_lastOccurence"]["st_date"].split('-')[1]), int(dictionary["dt_lastOccurence"]["st_date"].split('-')[2]), int(dictionary["dt_lastOccurence"]["st_time"].split(':')[0]), int(dictionary["dt_lastOccurence"]["st_time"].split(':')[1]), int(dictionary["dt_lastOccurence"]["st_time"].split(':')[2]), 0, pytz.UTC))) if "rg_recurrence" in dictionary and "dt_lastOccurence" in dictionary["rg_recurrence"] else None,

                 #deleted_occurences=dictionary["rg_recurrence"]["rg_delOccuriencies"] if "rg_recurrence" in dictionary and "rg_delOccuriencies" in dictionary["rg_recurrence"] else None,

                 #effective_rights=EffectiveRights(modify=dictionary["f_guestsCanModify"] if "f_guestsCanModify" in dictionary else False), # read-only!

                 organizer = Organizer(email_address=dictionary["organizer"]) if "organizer" in dictionary else None,

                 #exchangeOTHCalendarObject
                 appointment_sequence_number=dictionary["st_appointmentSequenceNumber"] if "st_appointmentSequenceNumber" in dictionary else '',
                 conference_type=dictionary["st_conference_type"] if "st_conference_type" in dictionary else '',
                 culture=dictionary["st_culture"] if "st_culture" in dictionary else '',
                 display_cc=dictionary["display_cc"] if "display_cc" in dictionary else '',
                 display_to=dictionary["display_to"] if "display_to" in dictionary else '',

                 last_modified_name=dictionary["st_lastModifiedName"] if "st_lastModifiedName" in dictionary else '',
                 mime_content=dictionary["st_mimeContent"] if "st_mimeContent" in dictionary else '',
                 #parent_folder_id=dictionary["st_parentFolderId"] if "st_parentFolderId" in dictionary else '',
                 in_reply_to=dictionary["st_inReplyTo"] if "st_inReplyTo" in dictionary else '',
                 headers=dictionary["st_internetMessageHeaders"] if "st_internetMessageHeaders" in dictionary else '',
  
                 uid=dictionary["st_uid"] if "st_uid" in dictionary else '',
                 web_client_edit_form_query_string=dictionary["st_webClientEditFormQueryString"] if "st_webClientEditFormQueryString" in dictionary else '',
                 allow_new_time_proposal=dictionary["f_allowNewTimeProposal"] if "f_allowNewTimeProposal" in dictionary else False,
                 has_attachments=dictionary["has_attachments"] if "has_attachments" in dictionary else False,
                 is_associated=dictionary["f_isAssociated"] if "f_isAssociated" in dictionary else False,

                 is_draft=dictionary["f_isDraft"] if "f_isDraft" in dictionary else False,
                 is_from_me=dictionary["f_isFromMe"] if "f_isFromMe" in dictionary else False,
                 is_meeting=dictionary["f_isMeeting"] if "f_isMeeting" in dictionary else False,
                 is_online_meeting=dictionary["f_isOnlineMeeting"] if "f_isOnlineMeeting" in dictionary else False,
                 is_recurring=dictionary["f_isRecurring"] if "f_isRecurring" in dictionary else False,

                 is_resend=dictionary["f_isResend"] if "f_isResend" in dictionary else '',
                 is_response_requested=dictionary["f_isResponseRequested"] if "f_isResponseRequested" in dictionary else '',
                 is_submitted=dictionary["f_isSubmitted"] if "f_isSubmitted" in dictionary else '',
                 is_unmodified=dictionary["f_isUnmodified"] if "f_isUnmodified" in dictionary else '',
                 meeting_request_was_sent=dictionary["f_meetingRequestWasSent"] if "f_meetingRequestWasSent" in dictionary else '',

                 reminder_is_set=dictionary["f_reminderIsSet"] if "st_visibility" in dictionary else False,
                 appointment_reply_time=utctz.localize(EWSDateTime.from_datetime(dictionary["dt_appointmentReplyTime"])) if "dt_appointmentReplyTime" in dictionary else None,
                 datetime_received=utctz.localize(EWSDateTime.from_datetime(dictionary["datetime_received"])) if "datetime_received" in dictionary else None,
                 datetime_sent=utctz.localize(EWSDateTime.from_datetime(dictionary["datetime_sent"])) if "datetime_sent" in dictionary else None,

                 reminder_due_by=utctz.localize(EWSDateTime.from_datetime(dictionary["dt_reminderDueBy"])) if "dt_reminderDueBy" in dictionary else None,
                 when=utctz.localize(EWSDateTime.from_datetime(dictionary["dt_when"])) if "dt_when" in dictionary else None,
                 #adjacent_meeting_count=dictionary["adjacent_meeting_count"] if "adjacent_meeting_count" in dictionary else 0,
                 #conflicting_meeting_count=dictionary["conflicting_meeting_count"] if "conflicting_meeting_count" in dictionary else 0,
                 size=dictionary["size"] if "size" in dictionary else 0,

                 #adjacent_meetings=dictionary["rg_adjacentMeetings"] if "rg_adjacentMeetings" in dictionary else '',
                 categories=dictionary["rg_categories"] if "rg_categories" in dictionary else '',
                 #conflicting_meetings=dictionary["rg_conflictingMeetings"] if "rg_conflictingMeetings" in dictionary else '',

        )


        if "rg_attachments" in dictionary:
            for f in dictionary["rg_attachments"]:
                attFile=ItemAttachment(name=att["st_title"] if "st_title" in dictionary["rg_attachments"] else '', item=my_calendar_item)
                calItem.attach(attFile)

        optAtt=[]
        reqAtt=[]
        ressAtt=[]

        if "rg_attendees" in dictionary:
            for att in dictionary["rg_attendees"]:
                a = Attendee()
                a.mailbox=Mailbox(email_address=att["st_email"] if "st_email" in att else '', name=att["st_displayName"] if "st_displayName" in att else '')
                
                a.response_type=att["st_responseStatus"] if "st_responseStatus" in att else None
                if att["f_optional"]:
                    optAtt.append(a)
                elif att["f_resource"]:
                    ressAtt.append(a)
                else:
                    reqAtt.append(a)

        calItem.required_attendees = reqAtt
        calItem.optional_attendees = optAtt
        calItem.resources = ressAtt


        return calItem


    def handleGetCalendarItem(self, calendarItem, shallPersist):
        utctz=tz('Etc/UTC')
        dataObject=exchangeOTHCalendarDataObject.exchangeOTHCalendarDataObject()
        #dataObject
        if hasattr(calendarItem, "subject"):
            dataObject.title=calendarItem.subject
        if hasattr(calendarItem, "text_body"):
            dataObject.text=calendarItem.text_body
        if hasattr(calendarItem, "datetime_created"):
            dataObject.created=datetime.fromisoformat(str(calendarItem.datetime_created.isoformat())).replace(tzinfo=timezone.utc)
        if hasattr(calendarItem, "last_modified_time"):
           time=datetime.fromisoformat(str(calendarItem.last_modified_time.isoformat())).replace(tzinfo=timezone.utc)
           if time.tzinfo != None:
               dataObject.edited=time
           else:
               dataObject.edited=utctz.localize(time)
         
        #calendarDataObject
        if hasattr(calendarItem, "sensitivity"):
            dataObject.st_visibility=calendarItem.sensitivity
        if hasattr(calendarItem, "legacy_free_busy_status"):
            dataObject.st_transparency=calendarItem.legacy_free_busy_status
        if hasattr(calendarItem, "duration"):
            dataObject.ul_duration=calendarItem.duration
        if hasattr(calendarItem, "location"):
            dataObject.st_location=calendarItem.location
        if hasattr(calendarItem, "item_class"):
            dataObject.st_kind=calendarItem.item_class
        if hasattr(calendarItem, "web_client_read_form_query_string"):
            dataObject.st_htmlLink=calendarItem.web_client_read_form_query_string
        if hasattr(calendarItem, "itemid"):
            dataObject.st_id=calendarItem.itemid
            dataObject._id = self.id_tag + dataObject.st_id
        else:
            dataObject._id = self.id_tag + "altKey_" + '_' + str(dataObject.created) + '_' + str(dataObject.title)
        if hasattr(calendarItem, "effective_rights"):
            if hasattr(calendarItem.effective_rights, "modify"):
                dataObject.f_guestsCanModify=calendarItem.effective_rights.modify
        if hasattr(calendarItem, "is_all_day"):
            dataObject.f_endTimeUnspecified=calendarItem.is_all_day
        dataObject.st_status="confirmed"
        if hasattr(calendarItem, "is_cancelled"):
            if calendarItem.is_cancelled:
                dataObject.st_status="cancelled"
        if hasattr(calendarItem, "start"): # and not calendarItem.start==None:
            sd=datetime.fromisoformat(str(calendarItem.start.isoformat())).replace(tzinfo=timezone.utc)
            st=calendarDataObject.calendarDataObject.datetime()
            st["st_date"]=str(sd.date())
            st["st_time"]=str(sd.time())
            st["st_timezone"]='+00:00'
            dataObject.dt_startTime=st
        if hasattr(calendarItem, "end"): # and not calendarItem.end==None:
            ed=datetime.fromisoformat(str(calendarItem.end.isoformat())).replace(tzinfo=timezone.utc)
            et=calendarDataObject.calendarDataObject.datetime()
            et["st_date"]=str(ed.date())
            et["st_time"]=str(ed.time())
            et["st_timezone"]='+00:00'
            dataObject.dt_endTime=et
        if hasattr(calendarItem, "original_start") and not calendarItem.original_start==None:
            od=datetime.fromisoformat(str(calendarItem.original_start.isoformat())).replace(tzinfo=timezone.utc)
            ot=calendarDataObject.calendarDataObject.datetime()
            ot["st_date"]=str(od.date())
            ot["st_time"]=str(od.time())
            ot["st_timezone"]='+00:00'
            dataObject.dt_originalStartTime=ot
        if hasattr(calendarItem, "attachments") and not calendarItem.attachments==None:
            attList=[]
            for attachment in calendarItem.attachments:
                att=calendarDataObject.calendarDataObject.attachment()
                if hasattr(calendarItem.attachments, "name"):
                    att["st_title"]=attachment.name
                    attList.append(att)
            dataObject.rg_attachments=attList
        attList=[]
        if hasattr(calendarItem, "required_attendees") and calendarItem.required_attendees != None:    
            for att in calendarItem.required_attendees:
                attendee=calendarDataObject.calendarDataObject.attendee()
                if hasattr(att, "email"):
                    attendee["st_email"]=att.email
                    if attendee["st_email"] == authInfo['email']:
                        attendee["f_self"]=True
                    else:
                        attendee["f_self"]=False
                if hasattr(att, "name"):
                    attendee["st_displayName"]=att.name
                if hasattr(calendarItem, "organizer") and hasattr(calendarItem.organizer, "email_address"):
                    attendee["organizer"]=calendarItem.organizer.email_address
                attendee["f_optional"]=False
                attendee["f_resource"]=False   
                if hasattr(att, "response_type"):                
                    attendee["st_responseStatus"]=att.response_type
                attList.append(attendee)
                
        if hasattr(calendarItem, "optional_attendees") and calendarItem.optional_attendees != None:
            for att in calendarItem.optional_attendees:
                attendee=calendarDataObject.calendarDataObject.attendee()
                if hasattr(att, "email"):
                    attendee["st_email"]=att.email
                    if attendee["st_email"] == authInfo['email']:
                        attendee["f_self"]=True
                    else:
                        attendee["f_self"]=False
                if hasattr(att, "name"):
                    attendee["st_displayName"]=att.name
                if hasattr(calendarItem, "organizer") and hasattr(calendarItem.organizer, "email_address"):
                    attendee["organizer"]=calendarItem.organizer.email_address
                attendee["f_optional"]=True
                attendee["f_resource"]=False   
                if hasattr(att, "response_type"):                
                    attendee["st_responseStatus"]=att.response_type
                attList.append(attendee)

        if hasattr(calendarItem, "resources") and calendarItem.resources != None:
            for att in calendarItem.required_attendees:
                attendee=calendarDataObject.calendarDataObject.attendee()
                if hasattr(att, "name"):
                    attendee["st_displayName"]=att.name
                attendee["f_optional"]=False
                attendee["f_resource"]=True   
                if hasattr(att, "response_type"):                
                    attendee["st_responseStatus"]=att.response_type
                attList.append(attendee)
        dataObject.rg_attendees=attList
        
        entryPoints=[]  
        cd = dataObject.rg_conferenceData()
        eP = calendarDataObject.calendarDataObject.conferenceData.entryPoint()
        if hasattr(calendarItem, "meeting_workspace_url"):
            eP["st_uri"]=calendarItem.meeting_workspace_url
        if hasattr(calendarItem, "net_show_url"):
            eP["st_netShowUrl"]=calendarItem.net_show_url
        entryPoints.append(eP)
        cd.rg_entryPoints=entryPoints

        if hasattr(calendarItem, "reminder_minutes_before_start"):
            rem=dataObject.rg_reminder()
            ovr=calendarDataObject.calendarDataObject.reminder.override()
            ovr["ul_minutes"]=str(calendarItem.reminder_minutes_before_start)
            rem.rg_overrides.append(ovr)

        recurrence=dataObject.rg_recurrence()
        delOccurences=list()
        if hasattr(calendarItem, "recurrence") and hasattr(calendarItem.recurrence, "id"):
            recurrence["st_recurringEventId"]=calendarItem.recurrence.id       
        if hasattr(calendarItem, "recurrence") and hasattr(calendarItem.recurrence, "pattern"):
            recurrence["st_recurringEventId"]=calendarItem.recurrence.pattern
        if hasattr(calendarItem, "first_occurrence") and hasattr(calendarItem.first_occurrence, "start"):
            fo=calendarDataObject.calendarDataObject.datetime()
            date=datetime.fromisoformat(str(calendarItem.first_occurrence.start.isoformat())).replace(tzinfo=timezone.utc)
            fo["st_date"]=str(date.date())
            fo["st_time"]=str(date.time())
            fo["st_timezone"]='+00:00'
            recurrence.dt_firstOccurence=fo
        if hasattr(calendarItem, "last_occurrence") and hasattr(calendarItem.last_occurrence, "start"):
            lo=calendarDataObject.calendarDataObject.datetime()
            date=datetime.fromisoformat(str(calendarItem.last_occurrence.start.isoformat())).replace(tzinfo=timezone.utc)
            lo["st_date"]=str(date.date())
            lo["st_time"]=str(date.time())
            lo["st_timezone"]='+00:00'
            recurrence.dt_lastOccurence=lo
        if hasattr(calendarItem, "deleted_occurrences") and calendarItem.deleted_occurrences != None:
            recurrence.rg_delOccuriencies=calendarItem.deleted_occurrences 

        # ExchangeOTHCalendarDataObject
        if hasattr(calendarItem, "appointment_sequence_number"):
            dataObject.st_appointmentSequenceNumber=calendarItem.appointment_sequence_number
        if hasattr(calendarItem, "conference_type"):
            dataObject.st_conference_type=calendarItem.conference_type
        if hasattr(calendarItem, "culture"):
            dataObject.st_culture=calendarItem.culture
        if hasattr(calendarItem, "display_cc"):
            dataObject.st_displayCC=calendarItem.display_cc
        if hasattr(calendarItem, "display_to"):
            dataObject.st_displayTo=calendarItem.display_to
        if hasattr(calendarItem, "last_modified_name"):
            dataObject.st_lastModifiedName=calendarItem.last_modified_name
        if hasattr(calendarItem, "mime_content"):
            dataObject.st_mimeContent=calendarItem.mime_content
        if hasattr(calendarItem, "parent_folder_id"):
            dataObject.st_parentFolderId=calendarItem.parent_folder_id.id
        if hasattr(calendarItem, "in_reply_to"):
            dataObject.st_inReplyTo=calendarItem.in_reply_to
        if hasattr(calendarItem, "headers"):
            dataObject.st_internetMessageHeaders=calendarItem.headers            
        if hasattr(calendarItem, "uid"):
            dataObject.st_uid=calendarItem.uid      
        if hasattr(calendarItem, "web_client_edit_form_query_string"):
            dataObject.st_webClientEditFormQueryString=calendarItem.web_client_edit_form_query_string  
        if hasattr(calendarItem, "allow_new_time_proposal"):
            dataObject.f_allowNewTimeProposal=calendarItem.allow_new_time_proposal  
        if hasattr(calendarItem, "has_attachments"):
            dataObject.f_hasAttachments=calendarItem.has_attachments 
        if hasattr(calendarItem, "is_associated"):
            dataObject.f_isAssociated=calendarItem.is_associated 
        if hasattr(calendarItem, "is_draft"):
            dataObject.f_isDraft=calendarItem.is_draft
        if hasattr(calendarItem, "is_from_me"):
            dataObject.f_isFromMe=calendarItem.is_from_me
        if hasattr(calendarItem, "is_meeting"):
            dataObject.f_isMeeting=calendarItem.is_meeting
        if hasattr(calendarItem, "is_online_meeting"):
            dataObject.f_isOnlineMeeting=calendarItem.is_online_meeting
        if hasattr(calendarItem, "is_recurring"):
            dataObject.f_isRecurring=calendarItem.is_recurring
        if hasattr(calendarItem, "is_resend"):
            dataObject.f_isResend=calendarItem.is_resend
        if hasattr(calendarItem, "is_response_requested"):
            dataObject.f_isResponseRequested=calendarItem.is_response_requested
        if hasattr(calendarItem, "is_submitted"):
            dataObject.f_isSubmitted=calendarItem.is_submitted
        if hasattr(calendarItem, "is_unmodified"):
            dataObject.f_isUnmodified=calendarItem.is_unmodified
        if hasattr(calendarItem, "meeting_request_was_sent"):
            dataObject.f_meetingRequestWasSent=calendarItem.meeting_request_was_sent
        if hasattr(calendarItem, "reminder_is_set"):
            dataObject.f_reminderIsSet=calendarItem.reminder_is_set
        if hasattr(calendarItem, "appointment_reply_time") and calendarItem.appointment_reply_time != None:
             dataObject.dt_appointmentReplyTime=datetime.fromisoformat(str(calendarItem.appointment_reply_time.isoformat())).replace(tzinfo=timezone.utc) 
        if hasattr(calendarItem, "datetime_received") and calendarItem.datetime_received != None:
            dataObject.dt_dateTimeReceived=datetime.fromisoformat(str(calendarItem.datetime_received.isoformat())).replace(tzinfo=timezone.utc) 
        if hasattr(calendarItem, "datetime_sent") and calendarItem.datetime_sent != None:
            dataObject.dt_dateTimeSent=datetime.fromisoformat(str(calendarItem.datetime_sent.isoformat())).replace(tzinfo=timezone.utc) 
        if hasattr(calendarItem, "reminder_due_by") and calendarItem.reminder_due_by != None:
            dataObject.dt_reminderDueBy=datetime.fromisoformat(str(calendarItem.reminder_due_by.isoformat())).replace(tzinfo=timezone.utc) 
        if hasattr(calendarItem, "when") and calendarItem.when != None:
            dataObject.dt_when=datetime.fromisoformat(str(calendarItem.when.isoformat())).replace(tzinfo=timezone.utc) 
        if hasattr(calendarItem, "adjacent_meeting_count"):
            dataObject.w_adjacentMeetingCount=calendarItem.adjacent_meeting_count
        if hasattr(calendarItem, "conflicting_meeting_count"):
            dataObject.w_conflictingMeetingCount=calendarItem.conflicting_meeting_count
        if hasattr(calendarItem, "size"):
            dataObject.w_size=calendarItem.size
        if hasattr(calendarItem, "adjacent_meetings"):
            dataObject.rg_adjacentMeetings=calendarItem.adjacent_meetings
        if hasattr(calendarItem, "categories"):
            dataObject.rg_categories=calendarItem.categories
        if hasattr(calendarItem, "conflicting_meetings"):
            dataObject.rg_conflictingMeetings=calendarItem.conflicting_meetings
        if hasattr(calendarItem, "body"):
            if hasattr(calendarItem.body, "is_truncated"):
                dataObject.rg_body["f_isTruncated"]=calendarItem.body.is_truncated            
                if hasattr(calendarItem.body, "body_type"):
                    dataObject.rg_body["st_bodyType"]=calendarItem.body.body_type  
        if hasattr(calendarItem, "effective_rights"):
            if hasattr(calendarItem.effective_rights, "create_associate"):
                dataObject.rg_effectiveRights["f_createAssociate"]=calendarItem.effective_rights.create_associate
            if hasattr(calendarItem.effective_rights, "create_contents"):
                dataObject.rg_effectiveRights["f_createContents"]=calendarItem.effective_rights.create_contents
            if hasattr(calendarItem.effective_rights, "create_hierarchy"):
                dataObject.rg_effectiveRights["f_createHierarchy"]=calendarItem.effective_rights.create_hierarchy
            if hasattr(calendarItem.effective_rights, "delete"):
                dataObject.rg_effectiveRights["f_delete"]=calendarItem.effective_rights.delete
            if hasattr(calendarItem.effective_rights, "read"):
                dataObject.rg_effectiveRights["f_read"]=calendarItem.effective_rights.read
            if hasattr(calendarItem.effective_rights, "view_private_items"):
                dataObject.rg_effectiveRights["f_viewPrivateItems"]=calendarItem.effective_rights.view_private_items

        if hasattr(calendarItem, "_end_timezone"):
            if hasattr(calendarItem._end_timezone, "name"):
                dataObject.rg_endTimeZone["st_name"]=calendarItem._end_timezone.name
            if hasattr(calendarItem._end_timezone, "periods"):
                dataObject.rg_endTimeZone["rg_periods"]=calendarItem._end_timezone.periods
            if hasattr(calendarItem._end_timezone, "transitionGroups"):
                dataObject.rg_endTimeZone["rg_transitionGroups"]=calendarItem._end_timezone.transitionGroups
            if hasattr(calendarItem._end_timezone, "transitions"):
                dataObject.rg_endTimeZone["rg_transitions"]=calendarItem._end_timezone.transitions
            if hasattr(calendarItem._end_timezone, "id"):
                dataObject.rg_endTimeZone["w_id"]=calendarItem._end_timezone.id
        if hasattr(calendarItem, "_start_timezone"):
            if hasattr(calendarItem._start_timezone, "name"):
                dataObject.rg_startTimeZone["st_name"]=calendarItem._start_timezone.name
            if hasattr(calendarItem._start_timezone, "periods"):
                dataObject.rg_startTimeZone["rg_periods"]=calendarItem._start_timezone.periods
            if hasattr(calendarItem._start_timezone, "transitionGroups"):
                dataObject.rg_startTimeZone["rg_transitionGroups"]=calendarItem._start_timezone.transitionGroups
            if hasattr(calendarItem._start_timezone, "transitions"):
                dataObject.rg_startTimeZone["rg_transitions"]=calendarItem._start_timezone.transitions
            if hasattr(calendarItem._start_timezone, "id"):
                dataObject.rg_startTimeZone["w_id"]=calendarItem._start_timezone.id
        if hasattr(calendarItem, "_meeting_timezone"):
            if hasattr(calendarItem._meeting_timezone, "name"):
                dataObject.rg_meetingTimeZone["st_name"]=calendarItem._meeting_timezone.name
            if hasattr(calendarItem._meeting_timezone, "periods"):
                dataObject.rg_meetingTimeZone["rg_periods"]=calendarItem._meeting_timezone.periods
            if hasattr(calendarItem._meeting_timezone, "transitionGroups"):
                dataObject.rg_meetingTimeZone["rg_transitionGroups"]=calendarItem._meeting_timezone.transitionGroups
            if hasattr(calendarItem._meeting_timezone, "transitions"):
                dataObject.rg_meetingTimeZone["rg_transitions"]=calendarItem._meeting_timezone.transitions
            if hasattr(calendarItem._meeting_timezone, "id"):
                dataObject.rg_meetingTimeZone["w_id"]=calendarItem._meeting_timezone.id

        if shallPersist:
            self.persist(dataObject)
        self.idTable.appendPrefetchedIdSet(dataObject._id)
                

#exchApi=exchangeOTHCalendarInterface()
#exchApi.authInfo["server"]="exchange.othr.de"
#exchApi.authInfo["username_with_domain"]="hsr\hos47096"
#exchApi.authInfo["password"]="16Emimon04*"
#exchApi.authInfo["email"]="simon1.hofmeister@st.othr.de"
#exchApi.extractFromAPI(True)
#exchApi.requestInjectionInAPI (substrIdTag = exchApi.id_tag)



