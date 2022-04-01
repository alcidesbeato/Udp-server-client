from datetime import datetime
import socket
import sys
import json

sock = socket.socket()
sock.bind(('', 0))
porta_origem = sock.getsockname()

ip_destino = input("Digite o IP destino: ")
porta_destino = int(input("Digite a porta de destino: "))
msg = input("Digite a mensagem a ser enviada: ")

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
