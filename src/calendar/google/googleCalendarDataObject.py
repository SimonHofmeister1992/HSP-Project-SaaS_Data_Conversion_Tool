import sys
sys.path.append("../general/")
sys.path.append("../../calendar/general/")
import calendarDataObject as calendarDataObject

class googleCalendarDataObject(calendarDataObject.calendarDataObject):
    '''defines the interface between teamup and the database'''
    # the variables prefixes are defined as in the Hungarian Apps Style

    class creator(dict):
        st_displayName=''
        st_email=''
        st_id=''
        f_self=''

    class source(dict):
        st_title=''
        st_url=''

    class extendedProperties(dict):
        class key(dict):
            st_key=''

        rg_private=''
        rg_shared=''
        def __init__(self):
            rg_private=self.key()
            rg_shared=self.key()


    class gadget(dict):
        class key(dict):
            st_key=''

        rg_preferences=''
        st_display=''
        ul_height=0
        st_iconLink=''
        st_link=''
        st_title=''
        st_type=''
        ul_width=0

        def __init__(self):
            rg_preferences=self.key()


    f_anyOneCanAddSelf=''
    f_attendeesOmitted=''
    f_guestsCanInviteOthers=''
    f_guestsCanSeeOtherGuests=''
    f_locked=''
    f_privateCopy=''

    rg_creator=creator()
    rg_source=source()
    rg_extendedProperties=extendedProperties()
    rg_gadget=gadget()
    rg_organizer=''

    st_colorId=''
    st_etag=''
    st_hangoutLink=''
   
    ul_sequence=0

    def __init__(self):
        rg_creator=self.creator()
        rg_source=self.source()
        rg_gadget=self.gadget()
        rg_extendedProperties=self.extendedProperties()
        

