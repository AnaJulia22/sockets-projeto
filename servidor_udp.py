import socket
import threading

serverIp = "localhost"
serverPort = 54321

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((serverIp, serverPort))

print(f"UDP server listening on {serverIp}:{serverPort}")

mensagem = "register servidorUDP localhost 54321"
serverSocket.sendto(mensagem.encode(), ("localhost", 53))
data, _ = serverSocket.recvfrom(1024)

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

    while True:

        data, clientAddress = serverSocket.recvfrom(1024)

        print(f"Conexão de {clientAddress}")

        operacao = data.decode()

        print("Equação recebida")

        resultado = calculadora(operacao)
        resposta = str(resultado)

        serverSocket.sendto(resposta.encode(),clientAddress)

        print('Resposta enviada')

        if not data:
            break

    serverSocket.close()

server = threading.Thread(target=server_thread)
server.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    pass