from socket import socket

from .settings import HOST, PORT


def server():
    with socket() as listen_socket:
        listen_socket.bind((HOST, PORT))
        listen_socket.listen(1)
        client_socket, client_address = listen_socket.accept()
        with client_socket:
            while True:
                print(f"client address: {client_address}")
                data = client_socket.recv(512)
                if not data:
                    break
                client_socket.sendall(data)
