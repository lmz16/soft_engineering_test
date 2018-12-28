import socket
import threading
import socketserver
import json
import pygame
import time
import SendTest as St

def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))

    try:
        print ("Send: {}".format(message))
        sock.sendall(message.encode("utf-8"))
        response = sock.recv(1024)
        jresp = json.loads(response.decode('utf-8'))
        print ("Recv: %s\n"%(jresp[0]))

    finally:
        sock.close()

if __name__ == "__main__":
    #Port 0 means to select an arbitrary unused port
    fresh_time = time.time()
    count = 0
    test_case = St.HostTest()
    while True:
        temptime = time.time()
        if (temptime - fresh_time) > 1:
            fresh_time = temptime
            msg = [test_case.test()]

            jmsg = json.dumps(msg)

            client(HOST, PORT, jmsg)
