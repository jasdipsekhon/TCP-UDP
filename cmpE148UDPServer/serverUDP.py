#UDP server
from socket import *
import sys

port = 10000
ipAddress = gethostbyname("")

server = socket(AF_INET, SOCK_DGRAM)
server.bind((ipAddress, port))

print("Server started!")

def leapYear(decodedMessage):
    year = list(map(int, clientMessage.split(",")))
    print ('-----------------Calculating Leap Years--------------------')
    for i in year:
        if (i % 4 == 0 and i % 100 != 0 or i % 400 == 0):   
            
            print ('Year {} is a leap year!'.format(i))
        else:
            print ('Year {} is not a leap year!'.format(i))
        
    return "Done!"

while True:
    clientMessage, clientAddress = server.recvfrom(1024)
    decodedMessage = clientMessage.decode('utf-8')
 
            
    response = leapYear(decodedMessage)
    server.sendto(response.encode('utf-8'),clientAddress)   
    print ('\n')
    print('Sending calculations back to client!')
serverSocket.close()
