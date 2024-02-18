import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("localhost",1111))

done=False

while not done:
    
        client.send(input("massage: ").encode('utf-8'))
        response=client.recv(2024).decode('utf-8')
        
        if response=="vishal":
            done=True
        else:
            print(response)
        
client.close()
        
        
     
