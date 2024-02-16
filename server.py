import socket

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost",1111))

server.listen()
print("Waiting for connection ------------")    

client ,address=server.accept()
print("connection is ready -----------")
while True:
    try:
        data=client.recv(1024).decode()
        print(data)
    except:
        client.close()
        break