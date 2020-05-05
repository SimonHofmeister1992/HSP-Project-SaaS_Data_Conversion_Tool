import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
import webbrowser
import requests
from microsoftgraph.client import Client

answer = "Empty"

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        #self.wfile.write(b'Hello, world!')
        print(self.requestline)
        global answer
        test = self.requestline
        answer = test
        print(answer)
        
httpd = socketserver.TCPServer(("", 5000), SimpleHTTPRequestHandler)
def getAnwser():
    print("serving at port", 5000)
    httpd.handle_request()
    
def extractCode():
    global answer
    answer = answer[11:48]
    print(answer)
    
print("logging in")
client = Client('07ce1641-3699-492a-ac5d-901b8309bfc0', 'sNCs_0@11N]/ocLdc2S/2sv_bi6xS/hg', account_type='by defect common', office365=True)
scope = {'offline_access', 'user.read', 'notes.read'}
url = client.authorization_url('http://localhost:5000', scope, state=None)
print(url)
#url = 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=07ce1641-3699-492a-ac5d-901b8309bfc0&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A5000&response_mode=query&scope=offline_access%20user.read%20mail.read&state=12345'

webbrowser.open_new(url)
getAnwser()

extractCode()

token = client.exchange_code('http://localhost:5000', answer)
#accessToken = token["access_token"]
#print(token)
#print(accessToken)
client.office365_token = token
client.token = token
#print(client.token)
#print(client.office365_token)

#params = {'Authorization':'Bearer '+accessToken,
          #'Host':'https://graph.microsoft.com/v1.0/me'}
#me =  requests.get("https://graph.microsoft.com/v1.0/me", params)
#print(me.url)
#print(me)
#print(token)
#me = client.get_me()
#me = client.get_message(message_id="")
print("logged in")

print("listing notebooks")
notebooks = client.list_notebooks()
print (notebooks)
section_notebook = client.get_notebook_sections('0-84C461DF521C020F!111')
print(section_notebook)
pages = client.list_pages()
print(pages)

print("listed notebooks")