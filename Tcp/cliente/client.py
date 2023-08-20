import socket
import time

def clientTCP(message):
    serverIp = "127.0.0.1"
    serverPort = 12345

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverIp, serverPort))

    print('Conectado')

    startTime = time.time()
    clientSocket.send(message.encode())

    with open(message, 'wb') as file:
        while 1:
            response = clientSocket.recv(1024)
            if not response:
                break
            file.write(response)
    endTime = time.time()

    print(f"TCP server response: {response.decode()}")
    print(f"Total time taken: {endTime - startTime:.6f} seconds")

    clientSocket.close()

message = input('escreva um nome de arquivo:')
clientTCP(message)