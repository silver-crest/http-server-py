from server import Server

if __name__ == '__main__':
    server = Server(8000)
    server.loop()
    while True:
        line = input("Enter q to stop : ")
        if line.strip() == "q":
            break
    server.stop()

