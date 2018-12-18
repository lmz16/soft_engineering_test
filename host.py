import socket
import threading
import socketserver
import json
import pygame

def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))

    try:
        print ("Send: {}".format(message))
        sock.sendall(message.encode("utf-8"))
        response = sock.recv(1024)
        jresp = json.loads(response.decode('utf-8'))
        print ("Recv: %s\n"%(jresp[0]['answer']))

    finally:
        sock.close()

if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 20000
    # msg1 = [{'src':"zj", 'dst':"zjdst"}]
    # msg2 = [{'src':"ln", 'dst':"lndst"}]
    # msg3 = [{'src':"xj", 'dst':"xjdst"}]
    while True:
        request = input("print your name:\n")

        msg =[{
            "request": request
        }]

    # jmsg1 = json.dumps(msg1)
    # jmsg2 = json.dumps(msg2)
    # jmsg3 = json.dumps(msg3)

        jmsg = json.dumps(msg)

    # client(HOST, PORT, jmsg1)
    # client(HOST, PORT, jmsg2)
    # client(HOST, PORT, jmsg3)

        client(HOST, PORT, jmsg)
