from backend.app import app

if __name__ == "__main__":
    app.httpd.serve_forever()
