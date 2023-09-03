import socket
import threading

serverIp = "localhost"
serverPort = 12345

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverIp, serverPort))
print(f"TCP server listening on {serverIp}:{serverPort}")
serverSocket.listen(1)

dns_udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dns_udp_client.bind((serverIp, serverPort))
mensagem = "register servidorTCP localhost 12345"
dns_udp_client.sendto(mensagem.encode(), ("localhost", 53))

data, _ = dns_udp_client.recvfrom(1024)
print(f"Conexão DNS estabelecida {_}")

print(data.decode())
print("----------------------------------")
print("Esperando uma solicitação...")
print("----------------------------------")

def calculadora(operacao):

    lista_operacao = operacao.split()

    if lista_operacao == []:
        resposta = 2
        return resposta

    print(lista_operacao)

    num1 = int(lista_operacao[0])
    num2 = int(lista_operacao[2])
    sinal = lista_operacao[1]

    if sinal == "+":
        return num1 + num2
    elif sinal == "-":
        return num1 - num2
    elif sinal == "/":
        if num2 == 0:
            return "Divisão por zero não é permitida."
        return num1 / num2
    elif sinal == "*":
        return num1 * num2
    elif sinal == "**":
        return num1 ** num2
    else:
        return "Operação não suportada."


def server_thread():

    clientSocket, clientAddress = serverSocket.accept()
    print(f"Conexão de {clientAddress}")

    while True:

        data = clientSocket.recv(1024)
        operacao = data.decode()

        print("Equação recebida")

        resposta = str(calculadora(operacao))

        clientSocket.send(resposta.encode())
        print('Resposta enviada')

        if not data:
            break

    clientSocket.close()

server = threading.Thread(target=server_thread)
server.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    pass

serverSocket.close()
