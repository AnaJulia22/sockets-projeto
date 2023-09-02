import socket
import time

def clientUDP(message):
    serverIp = "127.0.0.1"
    serverPort = 54321

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for equacao in message:

        print(f"Equação = {equacao}")

        startTime = time.perf_counter()

        clientSocket.sendto(equacao.encode(), (serverIp, serverPort))
        response, _ = clientSocket.recvfrom(1024)

        endTime = time.perf_counter()

        print("----------------------------------")
        print(f"A resposta é: {response.decode()}")
        print("----------------------------------")

        print(f"Tempo total: {endTime - startTime:.6f} seconds")

    clientSocket.close()
if __name__ == "__main__":

    print("Exemplo: 10 + 5")
    print("Digite a operação no formato do exemplo acima:")
    equacoes = ["20 + 10", "10 * 10", "100 - 50", "40 / 2", "5 ** 3"]
    clientUDP(equacoes)