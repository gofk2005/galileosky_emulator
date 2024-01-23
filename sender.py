import socket

class Sender():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket()
        self.client_socket.connect((host, port))

    def __del__(self):
        self.client_socket.close()

    def send(self, request):
        print(">>>", request)
        self.client_socket.send(request)
        data = self.client_socket.recv(1024)
        print("<<<", data)
        print()
