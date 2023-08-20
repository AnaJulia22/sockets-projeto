import socket
import time

def clientUDP(message):
    serverIp = "127.0.0.1"
    serverPort = 54321

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    startTime = time.time()
    clientSocket.sendto(message.encode(), (serverIp, serverPort))

    with open(message, 'wb') as file:
        while True:
            response, _ = clientSocket.recvfrom(1024)
            if not response:
                break
            file.write(response)

    endTime = time.time()

    print(f"UDP server response: {response.decode()}")
    print(f"Total time taken: {endTime - startTime:.6f} seconds")

    clientSocket.close()
message = input('>>>')
clientUDP(message)