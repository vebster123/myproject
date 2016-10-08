import os
from wsgiref.simple_server import make_server

HOST = 'localhost'
PORT = 8000
top_str = "<div class='top'>Middleware TOP</div>\n"
bottom_str = "<div class='bottom'>Middleware BOTTOM</div>\n"
body_open = "<body>"
body_close = "</body>"

def app(environ, start_response):
    address = environ["PATH_INFO"]
    print address
    result = ["file not found"]
    if address == "/about/aboutme.html":
        file = open("/home/maxim/Desktop/web/about/aboutme.html", mode = 'r')
        for line in file:
            result.append(line)
        file.close()
        start_response('200 OK', [('Content-type', 'text/HTML')])
        return result

    elif address == "/index.html" or "/":
        file = open("/home/maxim/Desktop/web/index.html", mode = 'r')
        for line in file:
            result.append(line)
        file.close()
        start_response('200 OK', [('Content-type', 'text/HTML')])
        return result
    else:
        start_response('404 Not Found', [("Content-Type", "text/html")])
        result = ["file not found"]
        return result

class Middleware(object):
    def __init__(self, app):
        self.app = app
        
    def __call__(self, environ, start_response):       
        for line in self.app(environ, start_response):
            if line.find(body_open) != -1:
                yield line
                yield top_str
            elif line.find(body_close) != -1:
                yield bottom_str
                yield line
            else:
                yield line

if __name__ == '__main__':
    app = Middleware(app)
    _server = make_server(HOST, PORT, app)
    print 'Serving HTTP on port %s ...' % PORT
_server.serve_forever()