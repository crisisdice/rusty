from ios import internal
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT=8080

class Server(BaseHTTPRequestHandler):
    def __init__(self, request, client_addr, server):
        super().__init__(request, client_addr, server)

    def send_code(seld, code):
        self.send_response(code)
        self.end_headers()

    def do_GET(self):
        self.send_code(200)
        self.wfile.write(internal())

    def do_POST(self):
        try:
            response_headers = dict([parse_header(header) for header in self.headers.as_string().split('\n')])

            self.send_code(201)
            self.wfile.write(self.rfile.read(headers.get('Content-Length')))
           #self.wfile.write(internal())
        except Exception as err:
            print(err)
            self.send_code(500)

def parse_header(header):
    sp = header.split(':')
    return (sp[0].strip(), sp[1].strip())

"""
"""
def run(server_class=HTTPServer, handler_class=Server, port=PORT):
    # TODO logging, configuration
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f'Listening on {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
