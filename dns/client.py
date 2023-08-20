import socket

def main():
    server_address = ('localhost', 9999)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        service_name = input("Digite o nome do serviço: ")
        if service_name.lower() == "exit":
            break

        client_socket.sendto(service_name.encode(), server_address)
        response, _ = client_socket.recvfrom(1024)
        print(response.decode())

    client_socket.close()

if __name__ == "__main__":
    main()
