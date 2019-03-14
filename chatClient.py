#Python Client Chat

import socket

host = '127.0.0.1'
port = 9000

s = socket.socket()
s.connect((host, port))

user = input("enter Username: ") 
str = input("Enter data: ")

while str != 'exit':
    s.send(user.encode())
    s.send(str.encode())
    str = input("Enter data: ")

s.close
