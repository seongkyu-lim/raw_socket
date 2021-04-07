from socket import *

serverName = "127.0.0.1"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

message = input("Input lowercase sentence:")

clientSocket.send(message.encode())

# Because server send two response for one request message,
# i make two variance for two response with buffer 2048.
modifiedMessage1 = clientSocket.recv(2048)
modifiedMessage2 = clientSocket.recv(2048)

# then print response with decoding.
print('The number of characters:', end="")
print(modifiedMessage1.decode())
print('The reversed string(s):', end="")
print(modifiedMessage2.decode())

clientSocket.close()
