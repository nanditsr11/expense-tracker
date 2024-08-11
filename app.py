from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from backend.database import Database
from backend.utils import authenticate_user

db = Database('expenses.db')

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("templates/index.html", "r") as file:
                self.wfile.write(file.read().encode())
        elif self.path == "/dashboard":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("templates/dashboard.html", "r") as file:
                self.wfile.write(file.read().encode())
        elif self.path == "/login":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("templates/login.html", "r") as file:
                self.wfile.write(file.read().encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/api/add_expense":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            db.add_expense(data)
            self.send_response(200)
            self.end_headers()
        elif self.path == "/api/get_expenses":
            expenses = db.get_expenses()
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(expenses).encode())

httpd = HTTPServer(('localhost', 8000), RequestHandler)
httpd.serve_forever()
