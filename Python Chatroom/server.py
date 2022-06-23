#creating the socket
import socket

#assigning one thread for each connection
from _thread import *

#creating the socket 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = socket.gethostname()
server_ip = socket.gethostbyname(hostname)
print("IP: \n" + server_ip)
print ("\nPort: ")
server_port = int(input())

#bind address to the socket
server.bind((server_ip, server_port))

server.listen(20)

#list with all clients
clients = []

#recieving and broadcasting messages
def serveClient(c, addr, username):
    c.send("Welcome to the chatroom".encode())
    
    while True:
        try:
            incoming = c.recv(2048).decode()
            print(incoming)

            if incoming =="<" + username + ">:" + 'leave()':
                c.close()
                message = username + " left the room"
                remove(c)
                broadcast(message, server)
            else:
                broadcast(incoming, c)

        except:
            continue

def broadcast(message, c):
    for client in clients:
        if client != c:
            try:
                client.send(message.encode())
            except:
                #closing connection with unresponsive client
                client.close()

                #remove unresponsive client
                remove(client)

#removing client from clients list
def remove(connection):
        if connection in clients:
            clients.remove(connection)
            message = "someone just left the room..."
            print(message)
            broadcast(message, server)
        
#accepting the new connection 
#getting username
while True:
    c, addr = server.accept()
    username = c.recv(2048).decode()
    clients.append(c)
    
    print(addr[0] + ": " + username + " entered the Chat room")
    start_new_thread(serveClient, (c, addr, username))