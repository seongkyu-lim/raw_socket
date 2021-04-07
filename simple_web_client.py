from socket import *

serverName = "192.168.0.5"
serverPort = 1235

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# format of http request message is like (Method SP | Request-URI SP | HTTP-Version CRLF).
# which i referred to https://www.tutorialspoint.com/http/http_requests.htm here.
message = 'GET /requestedFile.html HTTP/1.1\r\n\r\n'

# send Request.
clientSocket.send(message.encode())

# print data which response from server
# contents of the file 'requestedFile.html'
while True:
    outputdata = clientSocket.recv(2048)
    if(len(outputdata) < 1):
        break
    print(outputdata.decode(), end="")

# close socket
clientSocket.close()
