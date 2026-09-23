# python server using GET and POST http request method

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs 


class myhandler(BaseHTTPRequestHandler):
    def validate_username(self, username):
        if username=="":
            return False
        else:
            return True
    def welcome_user(self,username):
        message=f"Welcome {username}"
        return message
    def do_GET(self):
        parsed_url=urlparse(self.path)
        if self.path=="/":
            self.send_response(200)
            print("ok; successful")
            self.send_header("content-Type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h1><marquee> welcome to first python server...</marquee></h1>")
        elif parsed_url.path=="/welcome":
            unpack= parse_qs(parsed_url.query)
            extract=unpack.get("name",["Guest"])
            user_name=extract[0]
            msg=self.welcome_user(user_name)
            self.send_response(200)
            print("ok; successful")
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(msg.encode("utf-8"))
        elif self.path=="/homepage":
            html="""
            <form action="/submit_signup" method="post">
                <label for="user_name"> Enter Name</label>
                <input type="text" id="user_name" name= "user_name">
                <button type="submit" > submit</button>
            </form>
            """
            self.send_response(200)
            print("ok;successful")
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode("utf-8"))
        else:
            self.send_response(404)
            print("Faild;404-Error: Not Found")
            self.end_headers()
            self.wfile.write(b"404 Error:Page Not Found")
    def do_POST(self):
        if self.path=="/submit_signup":
            content_Length=int(self.headers["Content-Length"])
            read_data= self.rfile.read(content_Length)
            decode_data= read_data.decode("utf-8")
            extract_data= parse_qs(decode_data, keep_blank_values=True)
            grab_data=extract_data.get("user_name", ["Guest"])
            user_name= grab_data[0]
            is_valid=self.validate_username(user_name)
            if is_valid==False:
                self.send_response(400)
                print("400 Error: Bad Request")
                self.send_header("Content-Type", "text/html")
                self.end_headers()
                self.wfile.write(b"inavlid: empty field")
            else:
                message= f"Hello {user_name}!"
                self.send_response(200)
                print("ok; successful")
                self.send_header("Content-Type", "text/html")
                self.end_headers()
                self.wfile.write(message.encode("utf-8"))

server=HTTPServer(("localhost", 8000), myhandler)
print("server running on http://localhost:8000")
server.serve_forever()

