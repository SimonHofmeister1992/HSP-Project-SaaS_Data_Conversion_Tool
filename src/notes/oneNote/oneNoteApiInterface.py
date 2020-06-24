#OneNoteServiceAPI
#User Name: hsp2020SaaS@outlook.de
#Password: TestHSPT3st535

import sys
import os

from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import webbrowser
import requests
import traceback
from datetime import datetime
from pytz import timezone
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
    client = None
    httpd = None
    
    def __init__(self, azureID, azureSecret):
        """provide the login information with object generation"""
        self.azureID = azureID
        self.azureSecret = azureSecret
        self.id_tag = "notes#" + oneNoteApiInterface.__name__ + "#"
        self.login()
    
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
        
    def requestInjection (self, substrIdTag = None):
        """requests the data for Injection into the service and provides the methode to do so"""
        
        self.errorCount = 0
        self.successCount = 0
        self.requestInjectionInAPI(oneNoteDataObject, substrIdTag)
        print()
        print("Results: ")
        print("Notes failed to inject: ", self.errorCount)
        print("Notes successfully injected: ", self.successCount)
        
    def addNote (self, dataObject, client):
        """creates a new note with dataObject and inserts it into OneNote"""
        
        root = ET.Element("html", {"lang" : "de-DE"})
        head = ET.SubElement(root, "head")
        body = ET.SubElement(root, "body", {"style" : "font-family:Calibri;font-size:11pt", "data-absolute-enabled" : "true"})
        ET.SubElement(head, "title").text = dataObject.title
        ET.SubElement(head, "meta", {"content" : "text/html; charset=utf-8", "http-equiv" : "Content-Type"})
        ET.SubElement(head, "meta", {"content" : dataObject.created, "name" : "created"})
        div = ET.SubElement(body, "div", {"style" : "position:absolute;left:48px;top:115px;width:624px"})
        ET.SubElement(div, "p", {"style" : "margin-top:0pt;margin-bottom:0pt"}).text = dataObject.text
        content_xml = ET.tostring(root, encoding='utf8', method='xml')
        content_xml = content_xml[38:]
        content_xml = b'<!DOCTYPE html>\n'+content_xml
        
        _headers = {
            'Accept': 'application/json',
            'Authorization' : 'Bearer ' + self.client.office365_token['access_token'],
            'Content-Type' : 'application/xhtml+xml'
        }
        
        add_page = client._parse(requests.request('POST', client.base_url + '/me/onenote/sections/{}/pages'.format(section_id), headers=_headers, data=content_xml))
        
    def patchNote(self, dataObject, client):
        """patches a note with dataObject and inserts changes it into OneNote"""
        
        content_json = "["
        title = "{'target':'title','action':'replace','content':'"+dataObject["title"]+"'}"
        text = "{'target':'#para1','action':'replace','content':'"+dataObject["text"]+"'}"
        createdDateTime = "{'target':'createdDateTime','action':'replace','content':'"+dataObject["created"]+"'}"
        lastModifiedDateTime = "{'target':'lastModifiedDateTime','action':'replace','content':'"+dataObject["edited"]+"'}"
        
        content_json = content_json + title + text + createdDateTime + lastModifiedDateTime + "]"
        
        patch_page = client._patch(client.base_url + '/me/onenote/sections/{}/pages'.format(section_id), data=content_json)
        
    def injectInAPI (self, dataObject, section_id = '0-84C461DF521C020F!116'):
        """function for the injection of given data from JSON into the service"""
        
        if dataObject != None:
            try:
                client = self.login()
                oneNoteId = dataObject["_id"].split("#")[2]
                note = client._get(client.base_url + 'me/onenote/sections/{0}/pages?filter=id eq \'{1}\''.format(section_id, oneNoteId))
                
                if note is not None:
                    print("Found preexisting Note")
                    content_json = "["
                    title = "{'target':'title','action':'replace','content':'"+dataObject["title"]+"'},"
                    #text = "{'target':'#para1','action':'replace','content':'"+dataObject["text"]+"'},"
                    #createdDateTime = "{'target':'createdDateTime','action':'replace','content':'"+dataObject["created"]+"'},"
                    #lastModifiedDateTime = "{'target':'lastModifiedDateTime','action':'replace','content':'"+dataObject["edited"]+"'}"
                    
                    content_json = content_json + title + "]"#+ text + createdDateTime + lastModifiedDateTime + "]"
                    
                    #print(client._get(client.base_url + 'me/onenote/sections/{0}/pages/content?incluedIDs=true'.format(section_id)))
                    
                    patch_page = client._patch(client.base_url + '/me/onenote/sections/{}/pages'.format(section_id), data=content_json)
                    
                else:
                    print("Not found. Creating new note")
                    root = ET.Element("html", {"lang" : "de-DE"})
                    head = ET.SubElement(root, "head")
                    body = ET.SubElement(root, "body", {"style" : "font-family:Calibri;font-size:11pt", "data-absolute-enabled" : "true"})
                    ET.SubElement(head, "title").text = dataObject.title
                    ET.SubElement(head, "meta", {"content" : "text/html; charset=utf-8", "http-equiv" : "Content-Type"})
                    ET.SubElement(head, "meta", {"content" : dataObject.created, "name" : "created"})
                    div = ET.SubElement(body, "div", {"style" : "position:absolute;left:48px;top:115px;width:624px"})
                    ET.SubElement(div, "p", {"style" : "margin-top:0pt;margin-bottom:0pt"}).text = dataObject.text
                    content_xml = ET.tostring(root, encoding='utf8', method='xml')
                    content_xml = content_xml[38:]
                    content_xml = b'<!DOCTYPE html>\n'+content_xml
                    
                    _headers = {
                        'Accept': 'application/json',
                        'Authorization' : 'Bearer ' + self.client.office365_token['access_token'],
                        'Content-Type' : 'application/xhtml+xml'
                    }
                    
                    add_page = client._parse(requests.request('POST', client.base_url + '/me/onenote/sections/{}/pages'.format(section_id), headers=_headers, data=content_xml))
                    

                self.successCount += 1                 
                return note
            except Exception as exception:
                traceback.print_exc()
                self.httpd.server_close()
                raise exception
                self.errorCount += 1
        else:
            print("No dataObject given")        
        
        
        
        
        
        
        #add_page = client._parse(requests.request('POST', client.base_url + '/me/onenote/sections/{}/pages'.format(section_id), headers=_headers, data=content_xml))
    
    def extractFromAPI (self, section_id = '0-84C461DF521C020F!116'):
        """function for the injection of given data from the service into JSON"""
        
        client = self.login()
        pages = client._get(client.base_url + 'me/onenote/sections/{}/pages'.format(section_id))
        #pages = client.list_pages()
        
        timezone = datetime.now().strftime("%fZ")
        
        objectStore = []
        for page in pages['value']:
            content = self.extractContentFromPage(client._get(page['contentUrl']))
            oneNoteNote = {
            "title" : page['title'],
            "text" : content,
            "edited" : datetime.strptime(page['lastModifiedDateTime'][:-1]+"."+timezone, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%dT%H:%M:%S.%fZ"), 
            "created" : datetime.strptime(page['createdDateTime'][:-1]+"."+timezone, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%dT%H:%M:%S.%fZ"), 
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
            dataObject.edited = datetime.strptime(page['lastModifiedDateTime'][:-1]+"."+timezone, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            dataObject.created = datetime.strptime(page['createdDateTime'][:-1]+"."+timezone, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%dT%H:%M:%S.%fZ")
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
        if self.client is None:
            self.httpd = socketserver.TCPServer(("", 5000), SimpleHTTPRequestHandler)
            print("Starting login")
            #start login
            self.client = Client(self.azureID, self.azureSecret, account_type='by defect common', office365=True)
            scope = {'offline_access', 'user.read', 'notes.read', 'notes.readwrite'}
            url = self.client.authorization_url('http://localhost:5000', scope, state=None)
            
            #acquire authentication code from azure ad
            webbrowser.open_new(url)
            self.getAnwser(self.httpd)
            self.extractCode()
            
            #exchange code for authentication token and give it to the client class
            token = self.client.exchange_code('http://localhost:5000', self.answer)
            self.client.office365_token = token
            self.client.token = token
            
            print("login successfull")
        return self.client


test = oneNoteApiInterface('07ce1641-3699-492a-ac5d-901b8309bfc0', 'sNCs_0@11N]/ocLdc2S/2sv_bi6xS/hg')
#result = test.extractFromAPI()
test.requestInjection()