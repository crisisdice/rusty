from subprocess import Popen, PIPE
from http.server import BaseHTTPRequestHandler, HTTPServer

class Server(BaseHTTPRequestHandler):
    def __init__(self, request, client_addr, server):
        super().__init__(request, client_addr, server)

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(internal())

    def do_POST(self):
        self.send_response(405)
        self.end_headers()   

### internal ###
"""
"""
def internal():
    #bts = b'\x61\x6c\x65\x78'
    #process = subprocess.Popen(['./example'],#, 'More output'],
    #process = Popen(['rustc', 'example.rs'],
    # TODO return stderr if not empty from rustc
    # TODO return stdout and stderr of executable

    process = Popen(['echo', 'hello world'],
                stdout=PIPE, 
                stderr=PIPE)

    stdout, stderr = process.communicate()

    print(f'{stdout}, {stderr}')

    return stdout

### run server ###
"""
"""
def run(server_class=HTTPServer, handler_class=Server, port=8080):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    #print("Starting httpd on port {}...".format(port))
    httpd.serve_forever()

if __name__ == "__main__":
    run()
