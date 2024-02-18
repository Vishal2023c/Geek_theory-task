import socket

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost",1111))

server.listen()
print("Waiting for connection ------------")    

client ,address=server.accept()
print("connection is ready -----------")
done=False

while not done:
    
        response=client.recv(1024).decode('utf-8')
        
        if response=="vishal":
            done=True
        else:
            print(response)
             
        client.send(input("massage:").encode('utf-8'))
    
client.close()
server.close()
        
