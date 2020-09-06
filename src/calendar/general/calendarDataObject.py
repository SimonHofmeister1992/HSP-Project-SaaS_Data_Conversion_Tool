import sys
sys.path.append("../../general")
import dataObject as dataObject

class calendarDataObject(dataObject.dataObject):
    '''interface which contains attributes defined in all calendars'''
    # the variables prefixes are defined as in the Hungarian Apps Style, Extension: dt=Date

    class attachment(dict):
        st_fileUrl=''
        st_title=''
        st_fileId=''
        st_iconLink=''
        st_mimeType=''

    class attendee(dict):
        '''person, room or thing attending the event'''
        f_optional=''
        f_resource=''     
        st_responseStatus=''
        st_displayName=''
        st_email=''
        st_organizer=''
        f_self=''
        ul_additionalGuests=0
        st_comment=''
        st_id=''
             
    
    class conferenceData(dict):
        class conferenceSolution(dict):
            class key(dict):
                st_keyType=''

            st_name=''
            st_iconUri=''
            rg_key=key()
            
            def __init__(self):
                rg_key=self.key()

        class createRequest(dict):
            class conferenceSolutionKey(dict):
                st_type=''
            class status(dict):
                st_statusCode=''

            st_requestId=''
            rg_conferenceSolutionKey=conferenceSolutionKey()
            rg_status=status()
            
            def __init__(self):
                rg_conferenceSolutionKey=self.conferenceSolutionKey()
                rg_status=self.status()
            
        class entryPoint(dict):
            st_uri=''
            st_netShowUrl=''
            st_accessCode=''
            st_entryPointType=''
            st_label=''
            st_meetingCode=''
            st_passcode=''
            st_password=''
            st_pin=''


        st_notes=''
        st_signature=''
        rg_conferenceSolution=''
        rg_entryPoints=[]
        rg_createRequest=''

        def __init__(self):
            rg_conferenceSolution=self.conferenceSolution()
            rg_entryPoints=[]
            rg_createRequest=self.createRequest()

    class datetime(dict):
        st_date=''
        st_time=''
        st_timezone=''

    class recurrence(dict):
        '''recurrence information of the event'''
        dt_firstOccurence=''
        dt_lastOccurence=''
        rg_delOccuriencies=[]
        st_pattern=''
        st_recurringEventId=''
        
        def __init__(self):
            rg_delOccurencies=[]
            
    class reminder(dict):
        class override(dict):
            ul_minutes=0
            st_method=''
        rg_overrides=list()
        f_useDefault=''
        def __init__(self):
            self.rg_overrides=list()    

    class uniqueBody(dict):
        st_bodyType=''
    
    dt_endTime=datetime()
    dt_originalStartTime=datetime()
    dt_startTime=datetime()
    
    f_endTimeUnspecified=False # true if the event is all day
    f_guestsCanModify=False # true if guests are able to modify the event
    f_status=False # true if meeting is declined or deleted
    
    rg_attachments=[]
    rg_attendees=[] # structure defining attendees of the event
    rg_conferenceData=conferenceData()
    rg_reminder=reminder()
    rg_recurrence=recurrence() # structure defining recurrence patterns
    rg_uniqueBody=uniqueBody()
   
    st_iCalUid='' #calendar_internal id to be identified outside the calendar    
    st_id='' # calendar_internal id
    st_htmlLink='' # link to the calendar event
    st_kind='' # calendar_internal kind of the event
    st_location=''   
    st_transparency=''
    st_visibility='' # text value indicating the privacy level, if the event shall be shown to others

    ul_duration=0 # duration of the event in minutes    

    def execCorrectSubclassCastsByNamedTuple(self, dataObject):
        '''correcting not working subclass casts from namedtuple to calendarDataObject'''
        super().execCorrectSubclassCastsByNamedTuple(dataObject)
        #datetimes
         #start time
        if hasattr(dataObject, 'dt_startTime'):
            start=calendarDataObject.datetime()
            if hasattr(dataObject.dt_startTime, 'st_date'):
                start["st_date"]=dataObject.dt_startTime.st_date
            if hasattr(dataObject.dt_startTime, 'st_time'):
                start["st_time"]=dataObject.dt_startTime.st_time
            if hasattr(dataObject.dt_startTime, 'st_timezone'):
                start["st_timezone"]=dataObject.dt_startTime.st_timezone
            dataObject.dt_startTime=start
         # original start time
        if hasattr(dataObject, 'dt_originalStartTime'):
            start=calendarDataObject.datetime()
            if hasattr(dataObject.dt_originalStartTime, 'st_date'):
                start["st_date"]=dataObject.dt_originalStartTime.st_date
            if hasattr(dataObject.dt_originalStartTime, 'st_time'):
                start["st_time"]=dataObject.dt_originalStartTime.st_time
            if hasattr(dataObject.dt_originalStartTime, 'st_timezone'):
                start["st_timezone"]=dataObject.dt_originalStartTime.st_timezone
            dataObject.dt_originalStartTime=start
         #end time
        if hasattr(dataObject, 'dt_endTime'):
            start=calendarDataObject.datetime()
            if hasattr(dataObject.dt_endTime, 'st_date'):
                start["st_date"]=dataObject.dt_endTime.st_date
            if hasattr(dataObject.dt_endTime, 'st_time'):
                start["st_time"]=dataObject.dt_endTime.st_time
            if hasattr(dataObject.dt_endTime, 'st_timezone'):
                start["st_timezone"]=dataObject.dt_endTime.st_timezone
            dataObject.dt_endTime=start
        #attachments
        if hasattr(dataObject, 'rg_attachments'):
            attList=list()
            for attachment in dataObject.rg_attachments:
                att=calendarDataObject.attachment()
                if hasattr(attachment, 'st_title'):
                    att["title"]=attachment.st_title
                if hasattr(attachment, 'st_fileUrl'):
                    att["st_fileUrl"]=attachment.st_fileUrl
                attList.append(att)
            dataObject.rg_attachments=attList
        #attendees
        if hasattr(dataObject, 'rg_attendees'):
            attList=list()
            for attendee in dataObject.rg_attendees:
                att=calendarDataObject.attendee()
                if hasattr(attendee, 'st_displayName'):
                    att["st_displayName"]=attendee.st_displayName
                if hasattr(attendee, 'st_email'):
                    att["st_email"]=attendee.st_email
                if hasattr(attendee, 'st_organizer'):
                    att["st_organizer"]=attendee.organizer
                if hasattr(attendee, 'st_self'):
                    att["st_self"]=attendee.st_self
                if hasattr(attendee, 'f_optional'):
                    att["f_optional"]=attendee.f_optional
                if hasattr(attendee, 'f_resource'):
                    att["f_resource"]=attendee.f_resource
                if hasattr(attendee, 'st_responseStatus'):
                    att["st_responseStatus"]=attendee.st_responseStatus
                if hasattr(attendee, 'st_responseStatus'):
                    att["st_responseStatus"]=attendee.st_responseStatus
                if hasattr(attendee, 'st_organizer'):
                    att["st_organizer"]=attendee.st_organizer
                if hasattr(attendee, 'f_self'):
                    att["f_self"]=attendee.f_self
                attList.append(att)
            dataObject.rg_attendees=attList
        #conferenceData
        if hasattr(dataObject, 'rg_conferenceData'):
            confData=calendarDataObject.conferenceData()
            #conferenceSolution
            if hasattr(dataObject.rg_conferenceData, 'rg_conferenceSolution'):
                confSol=calendarDataObject.conferenceData.conferenceSolution()
                if hasattr(dataObject.rg_conferenceData.rg_conferenceSolution, 'st_name'):
                    confSol["st_name"]=dataObject.rg_conferenceData.rg_conferenceSolution.st_name
                confData["rg_conferenceSolution"]=confSol
            #entryPoint
            if hasattr(dataObject.rg_conferenceData, 'rg_entryPoint'):
                entryPoint=calendarDataObject.conferenceData.entryPoint()
                if hasattr(dataObject.rg_conferenceData.rg_entryPoint, 'st_uri'):
                    entryPoint["st_uri"]=dataObject.rg_conferenceData.rg_entryPoint.st_uri
                confData["rg_entryPoint"]=entryPoint
            dataObject.rg_conferenceData=confData
        #reminder
        if hasattr(dataObject, 'rg_reminder'):
            reminder=calendarDataObject.reminder()
            if hasattr(dataObject.rg_reminder, "rg_overrides"):
                overrides=list()
                for override in dataObject.rg_reminder.rg_overrides:
                    overr=calendarDataObject.reminder.override()
                    if hasattr(override, "ul_minutes"):
                        overr["ul_minutes"]=override.ul_minutes
                    overrides.append(overr)
                reminder["rg_overrides"]=overrides
            dataObject.reminder=reminder
        #recurrence
        if hasattr(dataObject, 'rg_recurrence'):
            recurrence=calendarDataObject.recurrence()
            if hasattr(dataObject.rg_recurrence, 'st_pattern'):
                recurrence["st_pattern"]=dataObject.recurrence.st_pattern
            if hasattr(dataObject.rg_recurrence, 'st_recurringEventId'):
                recurrence["st_recurringEventId"]=dataObject.recurrence.st_recurringEventId
            if hasattr(dataObject.rg_recurrence, 'st_firstOccurence'):
                recurrence["st_firstOccurence"]=dataObject.recurrence.st_firstOccurence
            if hasattr(dataObject.rg_recurrence, 'st_lastOccurence'):
                recurrence["st_lastOccurence"]=dataObject.recurrence.st_lastOccurence
            if hasattr(dataObject.rg_recurrence, "rg_delOccurencies"):
                delOcc=list()
                for occ in dataObject.rg_attendee.rg_delOccurencies:
                    delOcc.append(occ)
                recurrence["rg_delOccurencies"]=delOcc
            dataObject.rg_recurrence=recurrence
        #uniqueBody
        if hasattr(dataObject, 'rg_uniqueBody'):
            uniqueBody=calendarDataObject.uniqueBody()
            dataObject.rg_uniqueBody=uniqueBody
        return dataObject

    def __init__(self):
        self.rg_attendees=[]
        self.rg_attachments=[]
        self.dt_startTime=self.datetime()
        self.dt_endTime=self.datetime()
        self.dt_originalStartTime=self.datetime()
        self.id_tag = "calendar#" + self.__class__.__name__ + "#" 


