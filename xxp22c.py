# Python Heartbeat Client
import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ("127.0.0.1", 12000)
sock.settimeout(1)

for i in range(1,6):
        # start = time.time()
        message = 'heartbeat pulse ' + str(i) 
        print(message)
        byte = str.encode(message)
        sock.sendto(byte, server_addr)
        # end = time.time()
        time.sleep(5)

print("Client shutting down")