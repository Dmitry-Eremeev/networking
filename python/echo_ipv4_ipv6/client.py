from socket import AF_UNSPEC, AI_PASSIVE, SOCK_STREAM, getaddrinfo, socket

from .settings import HOST_NAME, PORT


def send_client_data():
    for result in getaddrinfo(host=HOST_NAME, port=PORT, family=AF_UNSPEC, type=SOCK_STREAM, flags=AI_PASSIVE):
        address_family, socket_type, protocol, canonical_name, socket_address = result
        try:
            client_socket = socket(family=address_family, type=socket_type, proto=protocol)
        except OSError as error:
            client_socket = None
            print(f"Couldn't to create a socket: {error}")
            continue
        try:
            print(f"server address: {socket_address}")
            client_socket.connect(socket_address)
        except OSError as error:
            client_socket.close()
            client_socket = None
            print(f"socket couldn't connect: {error}")
            continue
        if client_socket is None:
            exit(1)
        with client_socket:
            client_socket.sendall(b"Hello")
            data = client_socket.recv(1024)
        print(f"Server responded: {data}")
