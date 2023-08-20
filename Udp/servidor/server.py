import socket

def serverUDP():
    serverIp = "127.0.0.1"
    serverPort = 54321

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind((serverIp, serverPort))
    print(f"UDP server listening on {serverIp}:{serverPort}")

    while True:

        data, clientAddress = serverSocket.recvfrom(1024)
        with open(data.decode(), 'rb') as file:
            for dado in file.readlines():
                serverSocket.sendto(dado,clientAddress)
                data = file.read(1024)
            print('Arquivo enviado')
        print(f"Received from {clientAddress}: {data.decode()}")


serverUDP()