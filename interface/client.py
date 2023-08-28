import socket

def main():
    server_ip = "127.0.0.1"
    server_port = 8888

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    service_to_request = "tcp_service"  # Altere para o serviço que deseja verificar

    client_socket.sendto(service_to_request.encode(), (server_ip, server_port))
    response, _ = client_socket.recvfrom(1024)

    print(f"Response from Service Name Server: {response.decode()}")

    client_socket.close()

if __name__ == "__main__":
    main()
