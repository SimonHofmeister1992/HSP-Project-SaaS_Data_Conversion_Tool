import sys
sys.path.append("../../general")
import dataObject as dataObject

class calendarDataObject(dataObject.dataObject):
    '''interface which contains attributes defined in all calendars'''
    # the variables prefixes are defined as in the Hungarian Apps Style, Extension: dt=Date
    
    class attendee():
        '''person, room or thing attending the event'''
        st_displayName=''
        st_email=''
    
    class recurrence():
        '''recurrence information of the event'''
        st_pattern=''
        st_recurringEventId=''
        
    class attachment():
        st_fileUrl=''
        st_title=''
    
    class conferenceData():
        class conferenceSolution():
            st_name=''
            
        class entryPoint():
            st_uri=''
            
    class reminder():
        class override():
            ul_minutes=0
        gr_overrides=[]
    
    dt_endTime=''
    dt_originalStartTime=''
    dt_startTime=''
    
    f_endTimeUnspecified=False # true if the event is all day
    f_guestsCanModify=False # true if guests are able to modify the event
    f_status=False # true if meeting is declined or deleted
    f_transparency=False # true if event blocks time-span of duration in calendar
    
    rg_attendees=[] # structure defining attendees of the event
    rg_conferenceData=conferenceData()
    rg_entryPoints=[]
    rg_recurrence= recurrence() # structure defining recurrence patterns
   
    st_iCalUid='' #calendar_internal id to be identified outside the calendar    
    st_id='' # calendar_internal id
    st_htmlLink='' # link to the calendar event
    st_kind='' # calendar_internal kind of the event
    st_location=''   
    st_visibility='' # text value indicating the privacy level, if the event shall be shown to others

    ul_duration=0 # duration of the event in minutes    

