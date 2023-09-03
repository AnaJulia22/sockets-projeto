import socket

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

        resultado = 0

        lista_operacao = operacao.split(' ')
        print(lista_operacao)

        num1 = int(lista_operacao[0])
        num2 = int(lista_operacao[2])
        sinal = lista_operacao[1]

        if sinal == "+":
            resultado = num1 + num2
        elif sinal == "-":
            resultado = num1 - num2
        elif sinal == "/":
            resultado = num1 / num2
        elif sinal == "*":
            resultado = num1 * num2
        resposta = str(resultado)

        clientSocket.send(resposta.encode())
        print('Resposta enviada')

    clientSocket.close()

serverTCP()