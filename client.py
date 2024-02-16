import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("localhost",1111))

while True:
    
    data=input("Enter any input : ")
    try:
        
        client.send(data.encode())
    except:
        client.close()
        break