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
    counter = 0

    while True:
        data, client_address = server_dns.recvfrom(1024)

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
        elif data.decode() == '1':
            counter += 1

        else:

            service_name = data.decode().split()

            action = service_name[0]
            name = service_name[1]

            if action == 'register':
                protocol, port = service_name[2], service_name[3]
                services[name] = (protocol, port)
                response = f"Aplicacao registrada: {name} ({protocol}:{port})"
            elif action == "Consulta":
                if name in services:
                    host, port = services[name]
                    response = f"{name}:{host}:{port}"
        if counter == 2:
            break

        print(response)
        server_dns.sendto(response.encode(), client_address)

    services.clear()
    print("----------------------------------")
    print(f'Serviço removidos')
    print(f"Serviços: {services}")
    print("----------------------------------")

    server_dns.close()

server = threading.Thread(target=server_thread)
server.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    pass