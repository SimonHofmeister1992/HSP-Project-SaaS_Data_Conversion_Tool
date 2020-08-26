#import sys
#from http.server import HTTPServer, BaseHTTPRequestHandler
#import socketserver
#import webbrowser
#import requests
#from microsoftgraph.client import Client
#
#answer = "Empty"
#
#class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
#
#    def do_GET(self):
#        self.send_response(200)
#        self.end_headers()
#        #self.wfile.write(b'Hello, world!')
#        print(self.requestline)
#        global answer
#        test = self.requestline
#        answer = test
#        print(answer)
#        
#httpd = socketserver.TCPServer(("", 5000), SimpleHTTPRequestHandler)
#def getAnwser():
#    print("serving at port", 5000)
#    httpd.handle_request()
#    
#def extractCode():
#    global answer
#    answer = answer[11:48]
#    print(answer)
#
###################################################################################################
##logging in  
#print("logging in")
#client = Client('07ce1641-3699-492a-ac5d-901b8309bfc0', 'sNCs_0@11N]/ocLdc2S/2sv_bi6xS/hg', #account_type='by defect common', office365=True)
#scope = {'offline_access', 'user.read', 'notes.read', 'notes.readwrite'}
#url = client.authorization_url('http://localhost:5000', scope, state=None)
#print(url)
#
##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##acquire authentication code from azure ad
#webbrowser.open_new(url)
#getAnwser()
#extractCode()
#
##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##exchange code for authentication token and give it to the client class
#token = client.exchange_code('http://localhost:5000', answer)
##accessToken = token["access_token"]
##print(token)
##print(accessToken)
#client.office365_token = token
#client.token = token
##print(client.token)
##print(client.office365_token)
#
#print("logged in")
#
###################################################################################################
##get notebook information
#
##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##get list of notebooks
#print("listing notebooks")
#notebooks = client.list_notebooks()
#print("-----------------------------------------------------------")
#print("notebooks:")
##print(notebooks)
#for key in notebooks:
#    print(key)
#    if isinstance(notebooks[key], list):
#        for item in notebooks[key]:
#            for keyIntern in item:
#                print(keyIntern, ": ", item[keyIntern])
#            print()
#    else:
#        print(notebooks[key])
#    print()
#print("-----------------------------------------------------------")
#
##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##get list of sections
#section_notebook = client.get_notebook_sections('0-84C461DF521C020F!111')
#print("-----------------------------------------------------------")
#print("sections:")
#for key in section_notebook:
#    print(key)
#    if isinstance(section_notebook[key], list):
#        for item in section_notebook[key]:
#            for keyIntern in item:
#                print(keyIntern, ": ", item[keyIntern])
#            print()
#    else:
#        print(section_notebook[key])
#    print()
#print("-----------------------------------------------------------")
#
##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##get list of pages with content
#pages = client.list_pages()
#print("-----------------------------------------------------------")
#print("Pages:")
#for key in pages:
#    print(key)
#    if isinstance(pages[key], list):
#        for item in pages[key]:
#            for keyIntern in item:
#                if(keyIntern == 'contentUrl'):
#                    print(keyIntern, ": ", client._get(item[keyIntern]))
#                else:
#                    print(keyIntern, ": ", item[keyIntern])
#            print()
#    else:
#        print(pages[key])
#    print()
#print("-----------------------------------------------------------")
#
#print("listed notebooks")
