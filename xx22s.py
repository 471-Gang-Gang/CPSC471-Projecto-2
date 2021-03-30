# Heartbeat Server Code 
# UDPPingerServer.py
# We will need the following module to generate randomized lost packets
# import random
import time
from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM, 0)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
print("Started UDP server on port 12000")
while True:
    serverSocket.settimeout(10)
    # print("server loop executed...")
    start = time.time()
    # Receive the client packet along with the address it is coming from
    # print("starting now...")

    try: 
        message, address = serverSocket.recvfrom(1024)
        # Convert message back to string 
        msgString = message.decode("utf-8")
        end = time.time()
        delay = end-start
        # Capitalize the message from the client
        # message = message.upper()
        # If rand is less is than 4, we consider the packet lost and do not respond
        # Otherwise, the server responds
        # serverSocket.sendto(message, address)
    
        # Keep track of client pulse being absent for more than 10 seconds
    
        # Prints out "No pulse after 10 seconds. Server Quits"

        # Have the initial time, then have the end time, then keep track 
        print("Server received", msgString, "Pulse interval was", round(delay), "seconds")

    except OSError : 
        print("No pulse after 10 seconds. Server quits")
        break
        

print("Server stops.")