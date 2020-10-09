from socket import socket

from .settings import HOST, PORT


# start server beforehand
def send_client_data():
    with socket() as client_socket:
        client_socket.connect((HOST, PORT))
        client_socket.sendall(b"Hello")
        data = client_socket.recv(512)
        print(f"server responded: {data}")

