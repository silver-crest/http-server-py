class Request:
    def __init__(self, content: str):
        self.lines: list[str] = content.splitlines()
        self.path = self.lines[0].split()[1]

    def __getitem__(self, item: str):
        search = filter(lambda line: line.startswith(item), self.lines)
        try:
            match: str = next(search)
        except StopIteration:
            raise IndexError
        return match[match.index(":") + 2: ]

class Reponse:
    def __init__(self):
        self.headers: str = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\nConnection: close\r\n"
        self.content_header = ""
        self.html = ""

    def create_html(self, elements: list[tuple[str, str]]):
        elements = map(lambda tag, content: f"<{tag}>{content}</{tag}>", elements)
        elements = "\n".join(elements)
        self.html = f"""<html>
            <body>
            {elements}
            <body>
        </html>
        """
        self.content_header = f"Content-Length: {len(self.html.encode())}\r\n\r\n"

    def __str__(self):
        if len(self.html) <= 0:
            raise ValueError("Html hasn't been created")

        return self.headers + self.content_header + self.html
