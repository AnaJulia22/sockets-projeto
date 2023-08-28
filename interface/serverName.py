import socket

def main():
    server_ip = "127.0.0.1"
    server_port = 8888

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((server_ip, server_port))
    print(f"Service Name Server listening on {server_ip}:{server_port}")

    services = {
        "udp_service": ("udp", 54321),
        "tcp_service": ("tcp", 12345)
    }

    while True:
        data, client_address = server_socket.recvfrom(1024)
        service_name = data.decode()

        if service_name in services:
            protocol, port = services[service_name]
            response = f"{protocol}://{server_ip}:{port}"
        else:
            response = "Service not found"

        server_socket.sendto(response.encode(), client_address)

if __name__ == "__main__":
    main()
