from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hello World')

def run(server_class=HTTPServer, handler_class=SimpleHandler):
    server_address = ('', 3000)
    httpd = server_class(server_address, handler_class)
    print('Starting server on port 3000...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
