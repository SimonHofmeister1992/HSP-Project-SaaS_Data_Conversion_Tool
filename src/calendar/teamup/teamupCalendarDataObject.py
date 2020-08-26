import sys
sys.path.append("../general/")
sys.path.append("../../calendar/general/")
import calendarDataObject as calendarDataObject

class teamupCalendarDataObject(calendarDataObject.calendarDataObject):
    '''defines the interface between teamup and the database'''
    # the variables prefixes are defined as in the Hungarian Apps Style
    st_remoteId='' # id of corresponding event in third party system
    st_subcalendarIds='' # ids in which calendars this event shall appear
    st_subcalendarId='' # id in which calendars this event shall appear (old)
    st_timezone='' # version-nr of the event
    st_version='' # version-nr of the event

    
