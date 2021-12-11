#Server code
import socket
s=socket.socket()
s.bind(('localhost',9999))
s.listen(2)
print('listening...')
while True:
    c1,addr=s.accept()                               #client1 connection
    print("connected", addr)
    c2,addr = s.accept()                             #client2 connection
    print("connected",addr)
    for i in range(5):                               #msgs transfer between client1 and client2
        msg1=c1.recv(1024)
        c2.send(msg1)
        msg2=c2.recv(1024)
        c1.send(msg2)
    print('5 msgs has been sent and received by each client')
    c1.close()
    c2.close()
    break                                             #this is no required if you want to reconnect in loop
