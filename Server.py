import socket
import threading
import socketserver
import json, types,string
import os, time
import Mainfunc as Mf
import Extern as Et
from Define import *

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        Et.data = json.loads(data.decode('utf-8'))[0]
        #Et.data["ip"] = self.client_address[0]
        if (Et.game_state == GAMEJOIN)&(Et.init_time ==0):
            Et.init_time = time.time()
        response = Mf.sendBack()
        jresp = json.dumps(response)
        self.request.sendall(jresp.encode('utf-8'))
        Mf.gameFSM()

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = "localhost", 20000  #此处填写的是Server的IP
    Mf.gameFSM()
    socketserver.TCPServer.allow_reuse_address = True
    server = ThreadedTCPServer((HOST, PORT), MyServer)
    #ip, port = server.server_address
    #print(ip)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:", server_thread.name)
    print(" .... waiting for connection")

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
