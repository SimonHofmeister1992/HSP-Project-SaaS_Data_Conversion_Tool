import sys
sys.path.append("../../general/")
from notesDataObject import notesDataObject

class keepDataObject(notesDataObject):
    parent = ""
    parent_id = ""
    version = ""
    color = ""
    trashed = ""
    updated = ""
    
    