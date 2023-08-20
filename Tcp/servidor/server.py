import socket

def serverTCP():
    serverIp = "127.0.0.1"
    serverPort = 12345

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((serverIp, serverPort))
    serverSocket.listen(1)
    print(f"TCP server listening on {serverIp}:{serverPort}")

    while True:

        clientSocket, clientAddress = serverSocket.accept()
        print(f"Connection from {clientAddress}")
        data = clientSocket.recv(1024)

        with open(data.decode(), 'rb') as file:
            for dado in file.readlines():
                clientSocket.send(data)
            print('Arquivo enviado')
        clientSocket.close()

serverTCP()