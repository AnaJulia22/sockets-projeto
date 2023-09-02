import socket
import time

def clientUDP():
    serverIp = "127.0.0.1"
    serverPort = 54321

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:

        print('Exemplo: 10 + 5')
        message = input("Digite a operação no formato do exemplo acima:")

        if message == "fim":
            break

        startTime = time.time()

        clientSocket.sendto(message.encode(), (serverIp, serverPort))

        response, _ = clientSocket.recvfrom(1024)

        print("----------------------------------")
        print(f"A resposta é: {response.decode()}")

        endTime = time.time()


        print(f"Total time taken: {endTime - startTime:.6f} seconds")
        print('Digite fim para finalizar a conexão')

    clientSocket.close()

clientUDP()