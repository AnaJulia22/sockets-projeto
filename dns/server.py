import socket

class DNS_Server:
    def __init__(self):
        self.services = {}

    def register_service(self, service_name, ip, port):
        self.services[service_name] = (ip, port)

    def resolve_service(self, service_name):
        if service_name in self.services:
            ip, port = self.services[service_name]
            return f"{ip}:{port}"
        else:
            return "Not Found"

def main():
    dns_server = DNS_Server()
    dns_server.register_service("servico1", "192.168.1.1", 8000)
    dns_server.register_service("servico2", "192.168.1.2", 9000)

    server_address = ('localhost', 9999)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(server_address)

    print("Servidor DNS em execução...")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        service_name = data.decode()
        response = dns_server.resolve_service(service_name).encode()
        server_socket.sendto(response, client_address)

if __name__ == "__main__":
    main()
