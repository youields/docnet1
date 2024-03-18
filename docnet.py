from socket import *

server_socket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
serverPort = 6789
server_socket.bind(('localhost', serverPort))
server_socket.listen()

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = server_socket.accept()

    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1][1:]
        f = open(filename[1:])
        outputdata = f.read()

        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())

        # Close client socket
        connectionSocket.close()

server_socket.close()
sys.exit()  # Terminate the program after sending the corresponding data