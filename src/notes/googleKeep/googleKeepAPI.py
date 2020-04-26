import sys
import gkeepapi
###################################################
#Login
print("Starting login")
k = gkeepapi.Keep()
k.login('thsp006@gmail.com', 'TestHSPT3st534')
print("login successfull")

###################################################
#Create note
print("Creating note")
gnote = k.createNote('Title', 'Text')
k.sync()
print("Created note")

###################################################
#Get notes
gnotes = k.find(pinned=False, trashed=False)
for n in gnotes:
    print(n.title + " " + n.Text)