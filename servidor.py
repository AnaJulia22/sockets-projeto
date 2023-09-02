import socket
def calculadora(num1, num2, sinal):
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
    else:
        return "Operação não suportada."

def serverUDP():
    serverIp = "127.0.0.1"
    serverPort = 54321

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind((serverIp, serverPort))

    print(f"UDP server listening on {serverIp}:{serverPort}")

    while True:

        data, clientAddress = serverSocket.recvfrom(1024)

        operacao = data.decode()

        if operacao == "fim":
            print("Conexão finalizada")
            break

        print("Equação recebida")

        lista_operacao = operacao.split(' ')
        print(lista_operacao)

        num1 = int(lista_operacao[0])
        num2 = int(lista_operacao[2])
        sinal = lista_operacao[1]

        resultado = calculadora(num1, num2, sinal)
        resposta = str(resultado)

        serverSocket.sendto(resposta.encode(),clientAddress)

        print('Resposta enviada')

    serverSocket.close()

def serverTCP():
    serverIp = "127.0.0.1"
    serverPort = 12345

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((serverIp, serverPort))
    serverSocket.listen(1)

    print(f"TCP server listening on {serverIp}:{serverPort}")
    print("Esperando uma solicitação...")

    clientSocket, clientAddress = serverSocket.accept()
    print(f"Conexão de {clientAddress}")

    while True:

        data = clientSocket.recv(1024)
        operacao = data.decode()

        if operacao == "fim":
            print("Conexão finalizada")
            break

        print("Equação recebida")

        lista_operacao = operacao.split(' ')
        print(lista_operacao)

        num1 = int(lista_operacao[0])
        num2 = int(lista_operacao[2])
        sinal = lista_operacao[1]

        resultado = calculadora(num1, num2, sinal)
        resposta = str(resultado)

        clientSocket.send(resposta.encode())
        print('Resposta enviada')

    clientSocket.close()

if __name__ == "__main__":
    serverTCP()
    serverUDP()