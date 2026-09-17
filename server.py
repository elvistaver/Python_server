# python server using GET http request method

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs 


class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url=urlparse(self.path)
        if self.path=="/":
            self.send_response(200)
            print("ok; successful")
            self.send_header("content-Type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1><marquee> welcome to first python server...</marquee></h1>")
        elif parsed_url.path=="/homepage":
            unpack=parse_qs(parsed_url.query)
            extract=unpack.get("name",["Guest"])
            user_name=extract[0]
            message=f"*Welcome {user_name}!*"
            self.send_response(200)
            print("ok; successful")
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(message.encode("utf-8"))
        else:
            self.send_response(404)
            print("Faild;404-Error: Not Found")
            self.end_headers()
            self.wfile.write(b"404 Error:Page Not Found")

server=HTTPServer(("localhost", 8000), myhandler)
print("server running on http://localhost:8000")
server.serve_forever()