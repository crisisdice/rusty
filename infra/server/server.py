from ios import internal
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT=8080

class Server(BaseHTTPRequestHandler):
    def __init__(self, request, client_addr, server):
        super().__init__(request, client_addr, server)

    def send_code(self, code):
        self.send_response(code)
        self.end_headers()

    def do_GET(self):
        self.send_code(200)
        self.wfile.write(internal())

    def do_POST(self):
        try:
            self.send_code(201)

            response_headers = self.headers_as_dict()
            self.wfile.write(self.rfile.read(int(response_headers.get('Content-Length'))))
            #self.wfile.write(internal())

        except Exception as err:
            # TODO logging
            print(err)
            self.send_code(500)

    def headers_as_dict(self):
        kvp = lambda p : (p[0].strip(), p[1].strip())
        parse_header = lambda header : kvp(header.split(':'))
        return dict([parse_header(header) for header in self.headers.as_string().split('\n') if header != ''])

"""
"""
def run(server_class=HTTPServer, handler_class=Server, port=PORT):
    # TODO configuration
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f'Listening on {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
