#Client2 code
import socket
c2=socket.socket()
c2.connect(('localhost',9999))
print("connected to server")
print('waiting for client1 msg...')
for i in range(5):                                                      #receive and send msgs 5 times
    print("message received:-",c2.recv(1024).decode())
    msg2=input('message to send:-')
    c2.send(bytes(msg2,'utf-8'))
