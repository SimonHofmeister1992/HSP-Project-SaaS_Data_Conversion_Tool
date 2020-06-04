import sys
sys.path.append("../../general")
from dataObject import dataObject

class keepDataObject(dataObject):
    parent = ""
    parent_id = ""
    version = ""
    color = ""
    trashed = ""
    updated = ""