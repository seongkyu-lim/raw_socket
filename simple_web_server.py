# import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a server socket
# portnumber = 1235, my computer IP address = 192.168.0.5
serverPort = 1235
serverSocket.bind(('192.168.0.5', serverPort))
serverSocket.listen(1)

while True:
    # Establish the connection
    # Wait state until client is connected
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        # 2048 is buffer size$
        message = connectionSocket.recv(2048).decode()
        # Extract only index '1' divided by space. which is name of file.
        filename = message.split()[1]
        # open file
        f = open(filename[1:])
        # f.read() returns the entire contents of the file to a string.
        outputdata = f.read()
        f.close()
        # Send one HTTP header line into socket
        # Because in outputdata, there are only data(body)
        # so send status line first, with encoding.
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
        print("OK!")

    except IOError:
        # Send response message for file not found with encoding.
        connectionSocket.send('404 Not Found\r\n\r\n'.encode())
        # Close client socket
        connectionSocket.close()
serverSocket.close()
