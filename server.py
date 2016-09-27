import socket
import os

HOST = 'localhost'
PORT = 8000

_socket = socket.socket()
_socket.bind((HOST, PORT))
_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT

while True:
    client_connection = _socket.accept()
    data = client_connection.recv(1024)
    request = data.decode('utf-8').split(" ")
    address = request[1][1:]

    if address == "/about/aboutme.html":
        file = open("/home/maxim/Desktop/web/"+address, mode = 'r')
        response = """HTTP/1.1 200 OK \n Content type:text HTML\n\n\n """ + file.read()
        client_connection.send(response)  

    if address == "/index.html" or "/":
        file = open("/home/maxim/Desktop/web/index.html", mode = 'r')
        response = """http/1.1 200 OK \n Content type:text HTML\n\n\n """ + file.read()
        client_connection.send(response)  

    client_connection.close()
_socket.close()