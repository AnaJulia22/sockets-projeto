import socket
import time

def clientTCP(message):
    serverIp = "127.0.0.1"
    serverPort = 12346

    dns_tcp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    servico = "servidorTCP"
    dns_tcp_client.sendto(servico.encode(), ("127.0.0.1", 5000))

    ip = dns_tcp_client.recvfrom(1024)

    print("Requisição DNS feita")

    host = ip[0].decode()
    lista = host.split(":")
    enderecoIP, porta = str(lista[1]), int(lista[2])
    print(f"Endereço e porta do servidor: {enderecoIP}:{porta}")

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((enderecoIP, porta))

    print('Conectado')
    print("----------------------------------")
    print('Exemplo: 10 + 5')
    print("Digite a operação no formato do exemplo acima:")
    print("----------------------------------")

    for equacao in equacoes:

            startTime = time.perf_counter()
            valor = equacao

            clientSocket.send(equacao.encode())
            response = clientSocket.recv(1024)

            endTime = time.perf_counter()

            print("----------------------------------")
            print(f"Equação = {valor}")
            print(f"A resposta é: {response.decode()}")
            print(f"Tempo total: {endTime - startTime:.6f} seconds")
            print("----------------------------------")

    servico = '1'
    dns_tcp_client.sendto(servico.encode(), ("127.0.0.1", 5000))
    mensagem = input('Digite "fim" para finalizar a conexão: ').lower()
    clientSocket.sendto(mensagem.encode(), (enderecoIP, porta))

    dns_tcp_client.close()
    clientSocket.close()

if __name__ == "__main__":

    equacoes = ["20 + 10", "10 * 10", "100 - 50", "40 / 2", "5 ** 3"]
    clientTCP(equacoes)