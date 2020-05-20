#OneNoteServiceAPI
import sys, os

from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import webbrowser
import requests
from datetime import datetime
from xml.etree import cElementTree as ET
from microsoftgraph.client import Client

path = os.path.abspath(os.getcwd())
path = path.split("\\")
path = path[:len(path)-2]
path = "\\".join(path)
path = path+"\\general"
sys.path.insert(0, path)
from apiBase import apiBase

answer = ""

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        global answer
        answer = self.requestline

class OneNoteServiceAPI (apiBase):
    
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
        for paragraphs in list(page):
            if(paragraph.text is not None):
                content = content + paragraph.text
            else:
                content = content + paragraph.text
        return content
        
    def inject_in_API (self, attributes, section_id = '0-84C461DF521C020F!116'):
        """function for the injection of given data from JSON into the service"""
        
        client = self.login()
        for page in attributes:
            root = ET.Element("html", {"lang" : "de-DE"})
            head = ET.SubElement(root, "head")
            body = ET.SubElement(root, "body", {"style" : "font-family:Calibri;font-size:11pt", "data-absolute-enabled" : "true"})
            ET.SubElement(head, "title").text = page['title']
            ET.SubElement(head, "meta", {"content" : "text/html; charset=utf-8", "http-equiv" : "Content-Type"})
            ET.SubElement(head, "meta", {"content" : page['created'].strftime("%d&m&Y, %H:%M:%S"), "name" : "created"})
            div = ET.SubElement(body, "div", {"style" : "position:absolute;left:48px;top:115px;width:624px"})
            ET.SubElement(div, "p", {"style" : "margin-top:0pt;margin-bottom:0pt"}).text = page[text]
            content_xml = ET.tostring(root, encoding='utf8', method='xml')
            content_xml = content_xml[38:]
            content_xml = b'<!DOCTYPE html>\n'+content_xml
            
            _headers = {
                'Accept': 'application/json',
                'Authorization' : 'Bearer ' + client.office365_token['access_token'],
                'Content-Type' : 'application/xhtml+xml'
            }
            add_page = client._parse(requests.request('POST', client.base_url + '/me/onenote/sections/{}/pages'.format(section_id), headers=_headers, data=content_xml))          
    
    def extract_from_API (self):
        """function for the injection of given data from the service into JSON"""
        
        client = self.login()
        pages = client.list_pages()
        
        datastore = []
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
            datastore.append(oneNoteNote)
        return datastore
        
    def login (self):
        """establish a connection to the service an return an access object"""
        
        global httpd
        httpd = socketserver.TCPServer(("", 5000), SimpleHTTPRequestHandler)
        print("Starting login")
        #start login
        client = Client('07ce1641-3699-492a-ac5d-901b8309bfc0', 'sNCs_0@11N]/ocLdc2S/2sv_bi6xS/hg', account_type='by defect common', office365=True)
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


test = OneNoteServiceAPI()
#dictionary = {"title" : "test", "text" : "testtext"}
#liste = [dictionary]
#print(test.inject_in_API(liste))
print(test.extract_from_API())