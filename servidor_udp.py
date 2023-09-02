import socket

serverIp = "127.0.0.1"
serverPort = 54321

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((serverIp, serverPort))

print(f"UDP server listening on {serverIp}:{serverPort}")

def serverUDP():

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

serverUDP()