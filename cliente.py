import socket
import time

def clientUDP(message):
    serverIp = "127.0.0.1"
    serverPort = 54321

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:

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

def clientTCP(message):
    serverIp = "127.0.0.1"
    serverPort = 12345

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverIp, serverPort))

    print('Conectado')
    while True:

        if message == "fim":
            break
        startTime = time.time()

        clientSocket.send(message.encode())

        response = clientSocket.recv(1024)

        print("----------------------------------")
        print(f"A resposta é: {response.decode()}")

        endTime = time.time()

        print(f"Total time taken: {endTime - startTime:.6f} seconds")

        print('Digite fim para finalizar a conexão')

    clientSocket.close()
if __name__ == "__main__":

    print('Exemplo: 10 + 5')
    message = input("Digite a operação no formato do exemplo acima:")
    clientTCP(message)
    clientUDP(message)