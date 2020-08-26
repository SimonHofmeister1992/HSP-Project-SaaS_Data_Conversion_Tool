##gkeepapi version 0.11.14
#import sys
#import gkeepapi
#import json
####################################################
##Login
#print("Starting login")
#k = gkeepapi.Keep()
#k.login('thsp006@gmail.com', 'TestHSPT3st534')
#print("login successfull")
#
####################################################
##Create note
##print("Creating note")
##gnote = k.createNote('Title', 'Text')
##k.sync()
##print("Created note")
#
####################################################
##Get notes
#print()
#print("List of all nodes with attributes:")
#print()
#gnotes = k.find(pinned=False, trashed=False)
#print("-------------------------------------------")
#for n in gnotes:
#    print("title: ", n.title)
#    print("parent: ", n.parent)
#    print("id: ", n.id)
#    print("server_id: ", n.server_id)
#    print("parent_id: ", n.parent_id)
#    print("version: ", n._version)
#    print("text: ", n._text)
#    print("color: ", n._color)
#    print("archived: ", n._archived)
#    print("pinned: ", n._pinned)
#    print("moved: ", n._moved)
#    
#    print("media blobs: ")
#    for b in n.blobs:
#        print("    id: ", b.blob_id, " type: ", b.type)
#    
#    print("labels: ", n.labels)
#    for l in n.labels.all():
#        print("    name: ", l._name, " id: ", l.id)
#    
#    print("collaborators: ", n.collaborators)
#    for c in n.collaborators.all():
#        print("    name: ", c)
#    
#    print("children: ", n._children)
#    
#    print("timestamps: ", n.timestamps)
#    print("    created: ", n.timestamps._created)
#    print("    deleted: ", n.timestamps._deleted)
#    print("    trashed: ", n.timestamps._trashed)
#    print("    updated: ", n.timestamps._updated)
#    print("    edited: ", n.timestamps._edited)
#    
#    print("settings: ", n.settings)
#    print("    new_listitem_placement: ", n.settings._new_listitem_placement)
#    print("    graveyard_state: ", n.settings._graveyard_state)
#    print("    checked_listitems_policy: ", n.settings._checked_listitems_policy)
#    
#    print("annotations: ", n.annotations)
#    for a in n.annotations.all():
#        print("    ", a)
#    
#    print()
#    print("json format:")
#    #gather data and convert to json   
#    keepNote = {
#    "title" : n.title, 
#    #"parent" : n.parent, 
#    "id" : n.id, 
#    #"server_id" : n.server_id, 
#    #"parent_id" : n.parent_id, 
#    "version" : n._version, 
#    "text" : n._text, 
#    "color" : n._color.name, 
#    "archived" : n._archived, 
#    "pinned" : n._pinned, 
#    "moved" : n._moved, 
#    "created" : n.timestamps.dt_to_str(n.timestamps._created), 
#    #"deleted" : n.timestamps.dt_to_str(n.timestamps._deleted), 
#    "trashed" : n.timestamps.dt_to_str(n.timestamps._trashed), 
#    "updated" : n.timestamps.dt_to_str(n.timestamps._updated), 
#    "edited" : n.timestamps.dt_to_str(n.timestamps._edited)
#    }
#    jsonNode = json.dumps(keepNote)
#    print(jsonNode)
#    print("-------------------------------------------")
