import socket, sys
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Chatroom address: ")
server_ip = input()
print("\nPort: ")
server_port = int(input())
print("\nYour Username: ")
username = input()

server.connect((server_ip, server_port))
server.send(username.encode())

#function for recieving messages
def recv():
    while True:
        message = server.recv(2048).decode()
        print(str(message))

#function for sending messages
def send():
    while True:
        message = '<' + username + '>' + ':' + str(input())
        if message:
            server.send(message.encode())
            if message == 'leave()':
                server.close()
                sys.exit(0)

#starting threads to recieve and send messages simultaniously      
Thread(target=recv).start()
Thread(target=send).start()