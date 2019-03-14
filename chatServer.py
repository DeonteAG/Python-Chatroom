# Python Chat Server
import socket

host = '127.0.0.1'
port = 9000

s = socket.socket()
s.bind((host, port))

s.listen(100)
c,addr = s.accept()





while True:
    user = c.recv(1024)
    data = c.recv(1024)
    if not data and not user:
        break
    print("From "+str(user.decode())+": "+str(data.decode()))


c.close



