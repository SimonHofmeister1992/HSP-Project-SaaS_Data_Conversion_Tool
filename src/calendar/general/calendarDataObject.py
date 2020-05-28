import sys
sys.path.append("../../general")
import dataObject as dataObject

class calendarDataObject(dataObject.dataObject):
    '''interface which contains attributes defined in all calendars'''
    # the variables prefixes are defined as in the Hungarian Apps Style, Extension: dt=Date

    class attendee(object):
        '''person, room or thing attending the event'''
        st_displayName=''
        st_email=''
    
    class recurrence(object):
        '''recurrence information of the event'''
        st_pattern=''
        st_recurringEventId=''
        
    class attachment(object):
        st_fileUrl=''
        st_title=''
    
    class conferenceData(object):
        class conferenceSolution(object):
            st_name=''
            
        class entryPoint(object):
            st_uri=''
        rg_conferenceSolution=conferenceSolution()
        rg_entryPoint=entryPoint()
            
    class reminder(object):
        class override(object):
            ul_minutes=0
        gr_overrides=list()

        def __init__(self):
            self.gr_overrides=list()
        
    
    class datetime(object):
        st_date=''
        st_time=''
        st_timezone=''

    dt_endTime=datetime()
    dt_originalStartTime=datetime()
    dt_startTime=datetime()
    
    f_endTimeUnspecified=False # true if the event is all day
    f_guestsCanModify=False # true if guests are able to modify the event
    f_status=False # true if meeting is declined or deleted
    f_transparency=False # true if event blocks time-span of duration in calendar
    
    rg_attachments=list()
    rg_attendees=list() # structure defining attendees of the event
    rg_conferenceData=conferenceData()
    rg_reminder=reminder()
    rg_recurrence= recurrence() # structure defining recurrence patterns
   
    st_iCalUid='' #calendar_internal id to be identified outside the calendar    
    st_id='' # calendar_internal id
    st_htmlLink='' # link to the calendar event
    st_kind='' # calendar_internal kind of the event
    st_location=''   
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
                start.st_date=dataObject.dt_startTime.st_date
            if hasattr(dataObject.dt_startTime, 'st_time'):
                start.st_time=dataObject.dt_startTime.st_time
            if hasattr(dataObject.dt_startTime, 'st_timezone'):
                start.st_timezone=dataObject.dt_startTime.st_timezone
            dataObject.dt_startTime=start
         # original start time
        if hasattr(dataObject, 'dt_originalStartTime'):
            start=calendarDataObject.datetime()
            if hasattr(dataObject.dt_originalStartTime, 'st_date'):
                start.st_date=dataObject.dt_originalStartTime.st_date
            if hasattr(dataObject.dt_originalStartTime, 'st_time'):
                start.st_time=dataObject.dt_originalStartTime.st_time
            if hasattr(dataObject.dt_originalStartTime, 'st_timezone'):
                start.st_timezone=dataObject.dt_originalStartTime.st_timezone
            dataObject.dt_originalStartTime=start
         #end time
        if hasattr(dataObject, 'dt_endTime'):
            start=calendarDataObject.datetime()
            if hasattr(dataObject.dt_endTime, 'st_date'):
                start.st_date=dataObject.dt_endTime.st_date
            if hasattr(dataObject.dt_endTime, 'st_time'):
                start.st_time=dataObject.dt_endTime.st_time
            if hasattr(dataObject.dt_endTime, 'st_timezone'):
                start.st_timezone=dataObject.dt_endTime.st_timezone
            dataObject.dt_endTime=start
        #attachments
        if hasattr(dataObject, 'rg_attachments'):
            attList=list()
            for attachment in dataObject.rg_attachments:
                att=calendarDataObject.attachment()
                if hasattr(attachment, 'st_title'):
                    att.title=attachment.st_title
                if hasattr(attachment, 'st_fileUrl'):
                    att.st_fileUrl=attachment.st_fileUrl
                attList.append(att)
            dataObject.rg_attachments=attList
        #attendees
        if hasattr(dataObject, 'rg_attendees'):
            attList=list()
            for attendee in dataObject.rg_attendees:
                att=calendarDataObject.attendee()
                if hasattr(attendee, 'st_displayName'):
                    att.st_displayName=attendee.st_displayName
                if hasattr(attendee, 'st_email'):
                    att.st_email=attendee.st_email
                attList.append(att)
            dataObject.rg_attendees=attList
        #conferenceData
        if hasattr(dataObject, 'rg_conferenceData'):
            confData=calendarDataObject.conferenceData()
            #conferenceSolution
            if hasattr(dataObject.rg_conferenceData, 'rg_conferenceSolution'):
                confSol=calendarDataObject.conferenceData.conferenceSolution()
                if hasattr(dataObject.rg_conferenceData.rg_conferenceSolution, 'st_name'):
                    confSol.st_name=dataObject.rg_conferenceData.rg_conferenceSolution.st_name
                confData.rg_conferenceSolution=confSol
            #entryPoint
            if hasattr(dataObject.rg_conferenceData, 'rg_entryPoint'):
                entryPoint=calendarDataObject.conferenceData.entryPoint()
                if hasattr(dataObject.rg_conferenceData.rg_entryPoint, 'st_uri'):
                    entryPoint.st_uri=dataObject.rg_conferenceData.rg_entryPoint.st_uri
                confData.rg_entryPoint=entryPoint
            dataObject.rg_conferenceData=confData
        #reminder
        if hasattr(dataObject, 'rg_reminder'):
            reminder=calendarDataObject.reminder()
            if hasattr(dataObject.rg_reminder, "rg_overrides"):
                overrides=list()
                for override in dataObject.rg_reminder.rg_overrides:
                    overr=calendarDataObject.reminder.override()
                    if hasattr(override, "ul_minutes"):
                        overr.ul_minutes=override.ul_minutes
                    overrides.append(overr)
                reminder.rg_overrides=overrides
            dataObject.reminder=reminder
        #recurrence
        if hasattr(dataObject, 'rg_recurrence'):
            recurrence=calendarDataObject.recurrence()
            if hasattr(dataObject.rg_recurrence, 'st_pattern'):
                recurrence.st_pattern=dataObject.recurrence.st_pattern
            if hasattr(dataObject.rg_recurrence, 'st_recurringEventId'):
                recurrence.st_recurringEventId=dataObject.recurrence.st_recurringEventId
            dataObject.rg_recurrence=recurrence
        return dataObject

    def __init__(self):
        self.rg_attendees=list()
        self.rg_attachments=list()

