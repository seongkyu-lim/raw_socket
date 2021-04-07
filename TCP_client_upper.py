from socket import *

serverName = "127.0.0.1"
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

message = input("Input lowercase sentence:")

clientSocket.send(message.encode())

modifiedMessage = clientSocket.recv(2048)
print(modifiedMessage.decode())
clientSocket.close()
