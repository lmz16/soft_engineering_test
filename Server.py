import socket
import threading
import socketserver
import json, types,string
import os, time

p1_info = {
    "site":[200,300]
}

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        ctr = json.loads(data.decode('utf-8'))[0]
        update(ctr)
        response = [p1_info]
        jresp = json.dumps(response)
        self.request.sendall(jresp.encode('utf-8'))

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


def update(ctr):
    if ctr["up"]:
        p1_info["site"][1] -= 10
    if ctr["down"]:
        p1_info["site"][1] += 10
    if ctr["right"]:
        p1_info["site"][0] += 10
    if ctr["left"]:
        p1_info["site"][0] -= 10


if __name__ == "__main__":
    HOST, PORT = "localhost", 20000

    socketserver.TCPServer.allow_reuse_address = True
    server = ThreadedTCPServer((HOST, PORT), MyServer)
    ip, port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:", server_thread.name)
    print(" .... waiting for connection")

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()