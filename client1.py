#Client1 code
import socket
c1=socket.socket()
c1.connect(('localhost',9999))
print("connected to server")
for i in range(5):                                               #receive and send msgs 5 times
    msg=input("message to send:-")
    c1.send(bytes(msg,'utf-8'))
    print('message received:-',c1.recv(1024).decode())