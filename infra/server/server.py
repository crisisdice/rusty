# pylint: disable=import-error
import sys

from controller import internal_get, internal_post
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT=8000

"""
    _____________________________
    subclasses:
        0: BaseHTTPRequestHandler
"""
class Server(BaseHTTPRequestHandler):
    def __init__(self, request, client_addr, server):
        super().__init__(request, client_addr, server)

    def send_code(self, code):
        self.send_response(code)
        self.end_headers()

    def do_GET(self):
        self.send_code(200)
        self.wfile.write(internal_get())

    def do_POST(self):
        try:
            self.send_code(201)
            content_length = int(self.headers_as_dict().get('Content-Length'))
            request = self.rfile.read(content_length)
            #self.wfile.write(internal_post(request))
            self.wfile.write(request)

        except Exception as err:
            print(err)
            self.send_code(500)

    def headers_as_dict(self):
        kvp = lambda p : (p[0].strip(), p[1].strip())
        parse_header = lambda header : kvp(header.split(':'))
        return dict([parse_header(header) for header in self.headers.as_string().split('\n') if header != ''])

"""
    start server
    ------------
"""
def main(server_class=HTTPServer, handler_class=Server, port=PORT):
    # TODO logging
    # TODO configuration
    print(sys.argv)
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f'Listening on {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    main()
