import socket
import time

def clientTCP():
    serverIp = "127.0.0.1"
    serverPort = 12345

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverIp, serverPort))

    print('Conectado')
    while True:
        print('Exemplo: 10 + 5')
        message = input("Digite a operação no formato do exemplo acima:")
        if message == "fim":
            break
        startTime = time.time()

        clientSocket.send(message.encode())

        response = clientSocket.recv(1024)
        print("----------------------------------")
        print(response.decode())
        print(f"A resposta é: {response.decode()}")
        endTime = time.time()
        print('Digite fim para finalizar a conexão')

        print(f"Total time taken: {endTime - startTime:.6f} seconds")

    clientSocket.close()


clientTCP()