#TCP server
from socket import *
import sys
#set port #
port = 8000
#get IP address
ipAddress = gethostbyname("")
#create socket
server = socket(AF_INET, SOCK_STREAM)

serverAddress = (ipAddress,port)
#set address equal to the IP address and port number
server.bind(serverAddress)
#wait for socket communication from client
server.listen(1)

print('Server started!')

#calculate leap years
def leapYear(decodedMessage):
    year = list(map(int, decodedMessage.split(",")))
    print ('-----------------Calculating Leap Years--------------------')
    for i in year:
        if (i % 4 == 0 and i % 100 != 0 or i % 400 == 0):   
            
            print ('Year {} is a leap year!'.format(i))
        else:
            print ('Year {} is not a leap year!'.format(i))
        
    return "Done!"
#auses the process to block until the client connects to the server.
#it returns a new descriptor with which all communication is carried
serverSocket, address = server.accept() 

while True:
    #calls are used to receive messages from a socket
    clientMessage = serverSocket.recv(1024)
    #decodes the string to unicode
    decodedMessage = clientMessage.decode('utf-8')
    
    response = leapYear(decodedMessage)
    #encode as unicode and send to client
    serverSocket.send(response.encode('utf-8'))
    print ('\n')
    print('Sending calculations back to client!')

server.close()
