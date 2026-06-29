import socket
import threading

from http_data import Request, Response


def init_thread(server: socket.socket, keep_alive: threading.Event):
    print("Thread started")
    while not keep_alive.is_set():
        conn, addr = server.accept()
        t = threading.Thread(target=handle_client, args=(conn,))
        t.start()
    print("Thread killed")

class Server:
    def __init__(self, port: int):
        self.host: str = "localhost"
        self.port: int = port
        self.socket: socket.socket = socket.create_server((self.host, self.port))
        self.loop_thread: threading.Thread = None
        self.keep_alive: threading.Event = threading.Event()

    def loop(self):
        print("Starting server")
        self.keep_alive.clear()
        self.loop_thread = threading.Thread(target=init_thread, args=(self.socket, self.keep_alive))
        self.loop_thread.start()

    def stop(self):
        self.keep_alive.set()
        print("Stopped server")

def handle_client(conn: socket.socket):
    request = Request(conn.recv(1024).decode())
    response = Response()
    response.create_html([
        ("h1", request.path),
        ("h2", request["User-Agent"]),
    ])
    conn.send(str(response).encode())
    conn.close()
