import socket
import threading

serverIp = "127.0.0.1"
serverPort = 12345

dns_tcp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dns_tcp_server.bind((serverIp, serverPort))
mensagem = "register servidorTCP 127.0.0.1 12345"
dns_tcp_server.sendto(mensagem.encode(), ("127.0.0.1", 5000))
data, _ = dns_tcp_server.recvfrom(1024)

print(f"Conexão DNS estabelecida {_}")
print(data.decode())

dns_tcp_server.close()

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverIp, serverPort))
print(f"TCP server listening on {serverIp}:{serverPort}")
serverSocket.listen(1)

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

        if operacao == "fim":
            break

        print("Equação recebida")

        resposta = str(calculadora(operacao))

        clientSocket.send(resposta.encode())
        print('Resposta enviada')

    print('Digite "Ctrl+c" para finalizar a conexão')
    clientSocket.close()

server = threading.Thread(target=server_thread)
server.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    pass

serverSocket.close()
