import socket

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

        serverSocket.sendto(resposta.encode(),clientAddress)

        print('Resposta enviada')

    serverSocket.close()


serverUDP()