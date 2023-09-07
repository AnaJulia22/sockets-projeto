import socket
import threading

serverIp = "127.0.0.1"
serverPort = 54321

server_dns = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_dns.bind((serverIp, serverPort))
mensagem = "register servidorUDP 127.0.0.1 54321"
server_dns.sendto(mensagem.encode(), ("127.0.0.1", 5000))
data, _ = server_dns.recvfrom(1024)

print(f"Conexão DNS estabelecida {_}")
print(data.decode())


server_dns.close()

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((serverIp, serverPort))

print(f"UDP server listening on {serverIp}:{serverPort}")

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

    while True:

        data, clientAddress = serverSocket.recvfrom(1024)

        print(f"Conexão de {clientAddress}")

        operacao = data.decode()

        if operacao == "fim":
            break

        print("Equação recebida")

        resultado = calculadora(operacao)
        resposta = str(resultado)

        serverSocket.sendto(resposta.encode(),clientAddress)

        print('Resposta enviada')
    print('Digite "Ctrl+c" para finalizar a conexão')
    serverSocket.close()

server = threading.Thread(target=server_thread)
server.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    pass