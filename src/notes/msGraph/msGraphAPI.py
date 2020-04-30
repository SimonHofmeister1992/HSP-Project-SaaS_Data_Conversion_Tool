import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
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
url = 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=07ce1641-3699-492a-ac5d-901b8309bfc0&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A5000&response_mode=query&scope=offline_access%20user.read%20mail.read&state=12345'

getAnwser()
extractCode()
token = client.exchange_code('http://localhost:5000', answer)
accessToken = str(token).split("'")
accessToken = accessToken[13]
print(token)
token = client.set_token(accessToken)
print(token)
me = client.get_me()
#me = client.get_message(message_id="")
print("logged in")

print("listing notebooks")
#notebooks = client.list_notebooks()
#print (notebooks)
print("listed notebooks")