import socket

server_ip = "localhost"
server_port = 53

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_ip, server_port))
print(f"Service Name Server listening on {server_ip}:{server_port}")

def main():

    services = {}

    while True:
        data, client_address = server_socket.recvfrom(1024)
        print(f"Conexão estabelecida com {client_address}")
        if data.decode() == "servidorTCP":
            name = "servidorTCP"
            if name in services:
                host, port = services[name]
                response = f"{name}:{host}:{port}"
                server_socket.sendto(response.encode(), client_address)
        elif data.decode() == "servidorUDP":
            name = "servidorUDP"
            if name in services:
                host, port = services[name]
                response = f"{name}:{host}:{port}"
                server_socket.sendto(response.encode(), client_address)
        else:


            service_name = data.decode().split()

            action = service_name[0]
            name = service_name[1]
            print(service_name)

            if action == 'register':
                protocol, port = service_name[2], service_name[3]
                services[name] = (protocol, port)
                response = f"Aplicacao registrada: {name} ({protocol}:{port})"
            elif action == 'Deletar':
                if name in services:
                    del services[name]
                    response = f'{name} removido'
            elif action == "Consulta":
                if name in services:
                    host, port = services[name]
                    response = f"{name}:{host}:{port}"
            print(response)
            server_socket.sendto(response.encode(), client_address)
    server_socket.close()

if __name__ == "__main__":
    main()
