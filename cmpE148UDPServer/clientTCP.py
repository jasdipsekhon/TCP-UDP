#TCP client
from socket import *
import sys
port = 8000

#if IP address gives error. Uncomment the following line or type in the correct IP address
#this only was tested on macOS so it might not work on Windows

#ipAddress = gethostbyname(gethostname())
ipAddress = '127.0.0.1'
print ('IP address: ', ipAddress)
print ('Disclaimer: Change IP address if program does not run')
print ('Port: ', port)
#create socket
clientSocket = socket(AF_INET, SOCK_STREAM)

clientAddress = (ipAddress, port)
#connect to server
clientSocket.connect(clientAddress)
print('hi')
i = 0
#while True:
while i < 1:
    years = open('year.txt','r').read()
    print('Years in textfile:', years)
    print('\n')
    #encode string as unicode
    unicodeString = years.encode('utf-8')
    #send to server
    clientSocket.send(unicodeString)
    
    #read up to 1024 bytes of server message
    clientMessage = clientSocket.recv(1024)
    #Decode server message
    unicodeDecoded = clientMessage.decode('utf-8')
    
    print('Received from server: ', unicodeDecoded)
    print ('Finished')
    print('--------------------------------------------------------------')
    print('\n')
    print('\n')
    i = i + 1
clientSocket.close()
