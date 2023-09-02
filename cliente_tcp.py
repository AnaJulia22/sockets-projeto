import socket
import time

def clientTCP(message):
    serverIp = "127.0.0.1"
    serverPort = 12345

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverIp, serverPort))

    print('Conectado')
    for equacao in message:

        print(f"Equação = {equacao}")

        startTime = time.time()

        clientSocket.send(equacao.encode())
        response = clientSocket.recv(1024)

        endTime = time.time()

        print("----------------------------------")
        print(f"A resposta é: {response.decode()}")
        print("----------------------------------")

        print(f"Tempo total: {endTime - startTime:.6f} seconds")

    clientSocket.close()
if __name__ == "__main__":

    print('Exemplo: 10 + 5')
    print("Digite a operação no formato do exemplo acima:")
    equacoes = ["20 + 10", "10 * 10", "100 - 50", "40 / 2", "5 ** 3"]
    clientTCP(equacoes)