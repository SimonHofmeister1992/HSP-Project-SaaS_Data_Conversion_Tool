#!/usr/bin/env python
# coding: utf-8

# In[1]:

import sys
sys.path.append("../calendar_interfaces/")
import calendarDataObject as calendarDataObject

# In[3]:


class teamupCalendarDataObject(calendarDataObject.calendarDataObject):
    '''defines the interface between teamup and the database'''
    # the variables prefixes are defined as in the Hungarian Apps Style
    
    st_subcalendar_ids='' # ids in which calendars this event shall appear
    st_version='' # version-nr of the event
    gr_responseOfApi='' # temporary!!!

