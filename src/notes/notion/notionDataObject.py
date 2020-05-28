import sys
sys.path.append("../../general/")
from dataObject import dataObject

class notionDataObject(dataObject):
    version = ""
    type = ""
    parent = ""
    parent_table = ""
    last_edited_by = ""
    alive = ""
    created_by_table = ""
    created_by_id = ""
    last_edited_by_id = ""