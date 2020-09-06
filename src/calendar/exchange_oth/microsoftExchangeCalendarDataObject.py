import sys
sys.path.append("../general/")
sys.path.append("../../calendar/general/")
import calendarDataObject as calendarDataObject

class exchangeOTHCalendarDataObject(calendarDataObject.calendarDataObject):
    '''defines the interface between teamup and the database'''
    # the variables prefixes are defined as in the Hungarian Apps Style

    class body(dict):
        f_isTruncated=''
        st_bodyType=''

    class conversationId(dict):
        st_id=''
        st_changeKey=''

    class effectiveRights(dict):
        f_createAssociate=''
        f_createContents=''
        f_createHierarchy=''
        f_delete=''
        f_read=''
        f_viewPrivateItems=''

    class meetingTimeZone(dict):
        w_baseOffset=''
        f_daylight=''
        f_standard=''

    class timeZone(dict):
        st_name=''
        rg_periods=[]
        rg_transitionGroups=[]
        rg_transitions=[]
        w_id=''
        

        
    st_appointmentSequenceNumber=''
    st_conference_type=''
    st_culture=''
    st_displayCC=''
    st_displayTo=''
    st_lastModifiedName=''
    st_mimeContent=''
    st_parentFolderId=''
    st_inReplyTo=''
    st_internetMessageHeaders=''
    st_uid=''
    st_webClientEditFormQueryString=''
    
    f_allowNewTimeProposal=''
    f_hasAttachments=''   
    f_isAssociated=''
    f_isDraft=''
    f_isFromMe=''
    f_isMeeting=''
    f_isOnlineMeeting=''
    f_isRecurring=''
    f_isResend=''
    f_isResponseRequested=''
    f_isSubmitted=''
    f_isUnmodified=''
    f_meetingRequestWasSent=''
    f_reminderIsSet=''

    
    dt_appointmentReplyTime=''
    dt_dateTimeReceived=''
    dt_dateTimeSent=''
    dt_reminderDueBy=''
    dt_when=''
    
    
    rg_body=body()
    rg_adjacentMeetings=[]
    rg_categories=[]  # list of categories as strings
    rg_conflictingMeetings=[]
    rg_effectiveRights=effectiveRights()
    rg_endTimeZone=timeZone()
    rg_meetingTimeZone=timeZone()
    rg_startTimeZone=timeZone()

    w_adjacentMeetingCount=''
    w_conflictingMeetingCount=''
    w_size=''

    def __init__(self):
        rg_body=self.body()
        rg_adjacentMeetings=[]
        rg_categories=[]  # list of categories as strings
        rg_conflictingMeetings=[]
        rg_effectiveRights=self.effectiveRights()
        rg_endTimeZone=self.timeZone()
        rg_meetingTimeZone=self.timeZone()
        rg_startTimeZone=self.timeZone()


