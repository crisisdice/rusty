from ios import internal
from http.server import BaseHTTPRequestHandler, HTTPServer

class Server(BaseHTTPRequestHandler):
    def __init__(self, request, client_addr, server):
        super().__init__(request, client_addr, server)

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(internal())

    def do_POST(self):
        self.send_response(201)
        self.end_headers()
        #print(self.headers)
        content_length = self.headers.as_string()
        print(content_length)

        self.wfile.write(self.rfile.read(10))
        #self.wfile.write(internal())

"""
"""
def run(server_class=HTTPServer, handler_class=Server, port=8080):
    # TODO logging, configuration
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
    run()
