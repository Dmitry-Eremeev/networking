from socket import getaddrinfo, socket
from sys import exit

from .settings import PORT


def server():
    listening_socket = None
    for (address_family, socket_type, protocol, canonical_name, socket_address) in getaddrinfo(host=None, port=PORT):
        try:
            listening_socket = socket(family=address_family, type=socket_type, proto=protocol)
        except OSError as error:
            listening_socket = None
            print(f"Couldn't to create a socket: {error}")
            continue
        try:
            print(f"server address: {socket_address}")
            listening_socket.bind(socket_address)
            listening_socket.listen(1)
        except OSError as error:
            listening_socket.close()
            listening_socket = None
            print(f"socket could't bind or listen or accept: {error}")
            continue
        break
    if listening_socket is None:
        exit(1)
    connection, client_address = listening_socket.accept()
    with connection:
        print(f"Client address: {client_address}")
        while True:
            data = connection.recv(1024)
            if not data:
                break
            connection.sendall(data)
