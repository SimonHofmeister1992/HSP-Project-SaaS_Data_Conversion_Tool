#OneNoteServiceAPI
import sys
import os

from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import webbrowser
import requests
from datetime import datetime
from xml.etree import cElementTree as ET
from microsoftgraph.client import Client
sys.path.append("../../general/")
from baseApiInterface import baseApiInterface
from oneNoteDataObject import oneNoteDataObject

answer = ""

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        global answer
        answer = self.requestline

class oneNoteApiInterface (baseApiInterface):

    azureID = ""
    azureSecret = ""
    id_tag = ""
    
    def __init__(self, azureID, azureSecret):
        """provide the login information with object generation"""
        self.azureID = azureID
        self.azureSecret = azureSecret
        self.id_tag = "notes#" + oneNoteApiInterface.__name__ + "#"
    
    def getAnwser(self, httpd):
        """get the answer from the webserver"""
        
        httpd.handle_request()
        global answer 
        self.answer = answer
        
    def extractCode(self):
        """extract the authentication code from the webservers answer"""
        
        self.answer = self.answer[11:48]
    
    def extractContentFromPage(self, pageContent):
        """extract the content from the OneNote content url"""
        
        xml = pageContent.decode('UTF-8')
        root = ET.fromstring(xml)
        page = root[1][0]
        content = ""
        for paragraph in list(page):
            if(paragraph.text is not None):
                content = content + paragraph.text
            else:
                content = content
        return content
        
    def injectInAPI (self, dataObjects, section_id = '0-84C461DF521C020F!116'):
        """function for the injection of given data from JSON into the service"""
        
        client = self.login()
        for dataObject in dataObjects:
            root = ET.Element("html", {"lang" : "de-DE"})
            head = ET.SubElement(root, "head")
            body = ET.SubElement(root, "body", {"style" : "font-family:Calibri;font-size:11pt", "data-absolute-enabled" : "true"})
            ET.SubElement(head, "title").text = dataObject.title
            ET.SubElement(head, "meta", {"content" : "text/html; charset=utf-8", "http-equiv" : "Content-Type"})
            ET.SubElement(head, "meta", {"content" : dataObject.created, "name" : "created"})
            div = ET.SubElement(body, "div", {"style" : "position:absolute;left:48px;top:115px;width:624px"})
            ET.SubElement(div, "p", {"style" : "margin-top:0pt;margin-bottom:0pt"}).text = DataObject.text
            content_xml = ET.tostring(root, encoding='utf8', method='xml')
            content_xml = content_xml[38:]
            content_xml = b'<!DOCTYPE html>\n'+content_xml
            
            _headers = {
                'Accept': 'application/json',
                'Authorization' : 'Bearer ' + client.office365_token['access_token'],
                'Content-Type' : 'application/xhtml+xml'
            }
            add_page = client._parse(requests.request('POST', client.base_url + '/me/onenote/sections/{}/pages'.format(section_id), headers=_headers, data=content_xml))          
    
    def extractFromAPI (self):
        """function for the injection of given data from the service into JSON"""
        
        client = self.login()
        pages = client.list_pages()
        
        objectStore = []
        for page in pages['value']:
            content = self.extractContentFromPage(client._get(page['contentUrl']))
            oneNoteNote = {
            "title" : page['title'],
            "text" : content,
            "edited" : page['lastModifiedDateTime'], 
            "created" : page['createdDateTime'],
            "parentSection" : page['parentSection'], 
            "links" : page['links'],
            "id" : page['id'], 
            "self" : page['self'],
            "createdByAppId" : page['createdByAppId']
            }
            print(oneNoteNote)
            print()
            
            dataObject = oneNoteDataObject()
            dataObject.title = page['title']
            dataObject.text = content
            dataObject.edited = page['lastModifiedDateTime']
            dataObject.created = page['createdDateTime']
            dataObject.parentSection = page['parentSection']
            dataObject.links = page['links']
            dataObject._id = self.id_tag +str(page['id'])
            dataObject.self = page['self']
            dataObject.createdByAppId = page['createdByAppId']
            
            objectStore.append(dataObject)
            self.persist(dataObject)
            
        return objectStore
        
    def login (self):
        """establish a connection to the service an return an access object"""
        
        global httpd
        httpd = socketserver.TCPServer(("", 5000), SimpleHTTPRequestHandler)
        print("Starting login")
        #start login
        client = Client(self.azureID, self.azureSecret, account_type='by defect common', office365=True)
        scope = {'offline_access', 'user.read', 'notes.read', 'notes.readwrite'}
        url = client.authorization_url('http://localhost:5000', scope, state=None)
        
        #acquire authentication code from azure ad
        webbrowser.open_new(url)
        self.getAnwser(httpd)
        self.extractCode()
        
        #exchange code for authentication token and give it to the client class
        token = client.exchange_code('http://localhost:5000', self.answer)
        client.office365_token = token
        client.token = token
        
        print("login successfull")
        return client


test = oneNoteApiInterface('07ce1641-3699-492a-ac5d-901b8309bfc0', 'sNCs_0@11N]/ocLdc2S/2sv_bi6xS/hg')
#dictionary = {"title" : "test", "text" : "testtext"}
#liste = [dictionary]
#print(test.inject_in_API(liste))
result = test.extractFromAPI()
for res in result:
    print(res)