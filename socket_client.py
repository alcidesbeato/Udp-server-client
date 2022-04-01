import socket
import sys
import json


jsonResult = {
        "first":"You're",
        "second":"Awsome"}
jsonResult = json.dumps(jsonResult)
print (jsonResult)
try:
    sock = socket.socket()
except socket.error as err:
    print ('Socket error because of %s') %(err)

port = 1500
address = "192.168.0.4"

try:
    sock.connect((address, port))
    sock.send(bytearray(jsonResult,'utf-8'))
except socket.gaierror:

    print ('There an error resolving the host')

    sys.exit() 
        
print (jsonResult, 'was sent!')
sock.close()
