import socket
from datetime import datetime
import sys
import json

sock = socket.socket()
print ('Socket created ...')

port = 1500
sock.bind(('', port))
sock.listen(5)

print ('socket is listening\n\n')

while True:
    c, addr = sock.accept()
    print ('got connection from ', addr)
   
    jsonReceived = c.recv(1024)
    print ("Json received -->", jsonReceived)
    if jsonReceived:
     print("msg recebida")
     break

x = json.loads(jsonReceived)
ip_origem = x["IP_destino"]
ip_destino = x["IP_origem"]
porta_origem = x["Porta_Destino"]
porta_destino = x["Porta_Origem"]
time_client = x["Time_Stamp"]
time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
jsonResult = {
    "IP_origem" : ip_origem,
    "IP_destino" : ip_destino,
    "Porta_Origem":porta_origem,
    "Porta_Destino" : porta_destino,
    "Time_Stamp": time_client,
    "Time_destino": time,
    "ACK": True}
jsonResult = json.dumps(jsonResult)
try:
    sock = socket.socket()
except socket.error as err:
    print ('Socket error because of %s') %(err)
try:
    sock.connect((ip_destino, porta_destino))
    sock.send(bytearray(jsonResult,'utf-8'))
except socket.gaierror:
    print ('There an error resolving the host')
    sys.exit() 	
print (jsonResult, 'was sent!')
sock.close()   
c.close()

msg = input ("\n\nDigite a mensagem a ser enviada: ")

sock = socket.socket()
hostname = socket.gethostname()
ip_origem = socket.gethostbyname(hostname)
time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
jsonResult = {
        "IP_origem" : ip_origem,
        "IP_destino" : ip_destino,
        "Porta_Origem":porta_origem,
        "Porta_Destino" : porta_destino,
        "Time_Stamp": time,
        "Mensagem" : msg}
jsonResult = json.dumps(jsonResult)

try:
    sock.connect((ip_destino, porta_destino))
    sock.send(bytearray(jsonResult,'utf-8'))
    sock.close()
except socket.gaierror:

    print ('There an error resolving the host')

    sys.exit() 
        
print (jsonResult, 'was sent!')

sock = socket.socket()
sock.bind(('', port))
sock.listen(5)

print ('\nServer is wating confirmation...\n\n')

while True:
    c, addr = sock.accept()
    print ('got connection from ', addr)
   
    jsonReceived = c.recv(1024)
    print ("Json received -->", jsonReceived)
    if jsonReceived:
     print("msg recebida")
     break

