import socket
import threading

server_ip = "127.0.0.1"
server_port = 5000

server_dns = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_dns.bind((server_ip, server_port))
print(f"Service Name Server listening on {server_ip}:{server_port}")
print("----------------------------------")

def server_thread():

    services = {}

    while True:
        data, client_address = server_dns.recvfrom(1024)
        print(f"Conexão estabelecida com {client_address}")
        print("----------------------------------")
        if data.decode() == "servidorTCP":
            name = "servidorTCP"
            if name in services:
                host, port = services[name]
                response = f"{name}:{host}:{port}"
                server_dns.sendto(response.encode(), client_address)
        elif data.decode() == "servidorUDP":
            name = "servidorUDP"
            if name in services:
                host, port = services[name]
                response = f"{name}:{host}:{port}"
                server_dns.sendto(response.encode(), client_address)
        else:

            service_name = data.decode().split()

            action = service_name[0]
            name = service_name[1]
            print(service_name)

            if action == 'register':
                protocol, port = service_name[2], service_name[3]
                services[name] = (protocol, port)
                response = f"Aplicacao registrada: {name} ({protocol}:{port})"
            elif action == "Consulta":
                if name in services:
                    host, port = services[name]
                    response = f"{name}:{host}:{port}"
            elif action == 'deletar':
                if "servidorTCP" and "servidorUDP" in services:
                    del services[name]
                    print("----------------------------------")
                    print(f'Serviço {name} removido')
                    print(f"Serviços: {services}")
                    print("----------------------------------")
                    if len(services) == 0:
                        break

        print(response)
        server_dns.sendto(response.encode(), client_address)
    server_dns.close()

server = threading.Thread(target=server_thread)
server.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    pass