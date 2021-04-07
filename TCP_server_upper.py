from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))

serverSocket.listen(1)
print("The server is ready to receive.")

try:
    while True:
        connectionSocket, clientAddress = serverSocket.accept()
        message = connectionSocket.recv(2048)
        modifiedMessage = message.decode().upper()
        connectionSocket.send(modifiedMessage.encode())
        connectionSocket.close()
except KeyboardInterrupt:
    print("Press Ctrl-c to terminate while statement")
    pass
