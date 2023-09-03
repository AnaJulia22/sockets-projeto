import socket
import time

def clientUDP(message):
    serverIp = "127.0.0.1"
    serverPort = 64321

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    servico = "servidorUDP"
    clientSocket.sendto(servico.encode(), (serverIp, 53))

    ip = clientSocket.recvfrom(1024)
    print(ip)
    host = ip[0].decode()
    lista = host.split(":")
    enderecoIP, porta = str(lista[1]), int(lista[2])
    print(f"Endereço e porta do servidor: {enderecoIP}:{porta}")

    print('Conectado')
    print("----------------------------------")
    print('Exemplo: 10 + 5')
    print("Digite a operação no formato do exemplo acima:")
    print("----------------------------------")

    for equacao in message:

        print(f"Equação = {equacao}")

        startTime = time.perf_counter()

        clientSocket.sendto(equacao.encode(), (enderecoIP, porta))
        response, _ = clientSocket.recvfrom(1024)

        endTime = time.perf_counter()

        print("----------------------------------")
        print(f"A resposta é: {response.decode()}")
        print("----------------------------------")

        print(f"Tempo total: {endTime - startTime:.6f} seconds")

    clientSocket.close()
if __name__ == "__main__":

    equacoes = ["20 + 10", "10 * 10", "100 - 50", "40 / 2", "5 ** 3"]
    clientUDP(equacoes)