import socket
import threading

class Server:
    def __init__(self, port: int):
        self.host: str = "localhost"
        self.port: int = port
        self.socket: socket.socket = socket.create_server((self.host, self.port))

    def loop(self):
        while True:
            conn, addr = self.socket.accept()
            t = threading.Thread(target=handle_client, args=(conn, ))
            t.start()

def handle_client(conn: socket.socket):
    request = conn.recv(1024).decode()
    print(request)
    lines = request.split("\n")

