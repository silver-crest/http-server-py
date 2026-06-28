import socket
import threading

from http_data import Request, Response


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
    request = Request(conn.recv(1024).decode())
    response = Response()
    response.create_html([
        ("h1", request.path),
        ("h2", request["User-Agent"]),
    ])
    conn.send(str(response).encode())
