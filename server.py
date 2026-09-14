# python server using GET http request method

from http.server import HTTPServer, BaseHTTPRequestHandler


class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path=="/":
            self.send_response(200)
            self.send_header("content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1><marquee> welcome to first python server...<h1/><marquee/>")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Error:Page Not Found")

server=HTTPServer(("localhost", 8000), myhandler)
print("server running on http://localhost:8000")
server.serve_forever()