import socket

serverIp = "127.0.0.1"
serverPort = 12345

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverIp, serverPort))
serverSocket.listen(1)

print(f"TCP server listening on {serverIp}:{serverPort}")
print("Esperando uma solicitação...")


def serverTCP():

    clientSocket, clientAddress = serverSocket.accept()
    print(f"Conexão de {clientAddress}")

    while True:

        data = clientSocket.recv(1024)
        operacao = data.decode()

        print("Equação recebida")

        resultado = eval(operacao)
        resposta = str(resultado)

        clientSocket.send(resposta.encode())
        print('Resposta enviada')

    clientSocket.close()

serverTCP()