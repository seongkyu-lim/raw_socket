from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))

serverSocket.listen(1)
print("The server is ready to receive.")

try:
    while True:
        connectionSocket, clientAddress = serverSocket.accept()
        # receive request message with connectionsocket.
        # buffer size = 2048.
        message = connectionSocket.recv(2048)
        # decode message.
        modifiedMessage = message.decode()
        # i make two variable for two response value
        # first is number of characters in the strings.
        modifiedMessage1 = str(len(modifiedMessage))
        # second is reversed strings.
        # i used indexing, slicing of python for reverse of strings.
        modifiedMessage2 = modifiedMessage[::-1]
        # then send response message twice with encoding.
        connectionSocket.send(modifiedMessage1.encode())
        connectionSocket.send(modifiedMessage2.encode())
        connectionSocket.close()
except KeyboardInterrupt:
    print("Press Ctrl-c to terminate while statement")
    pass
