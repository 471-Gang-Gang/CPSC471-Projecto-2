import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ("127.0.0.1", 45678)
sock.settimeout(1)
# Keeping track of any packet lost
packets_lost = 0
# List of RTT
rtt_list = []
try:
    for i in range(1,16):
        start = time.time()
        message = 'Ping #' + str(i) + " " + time.ctime(start)
        byte = str.encode(message)
        try:
            sock.sendto(byte, server_addr)
            print("Sent " , message)
            data, server = sock.recvfrom(4096)
            print("Received ", data)
            end = time.time()
            # Find RTT and convert to milliseconds
            elapsed =  round((end - start)*1000,3)
            rtt_list.append(elapsed)
            print("RTT: " , str(elapsed) , " ms\n")
        except socket.timeout:
            print("#" + str(i) + " Requested Time out\n")
            packets_lost += 1

finally:
    print("closing socket")
    sock.close()
    print("Min RTT = ", min(rtt_list), " ms")
    print("Max RTT = ", max(rtt_list), " ms")
    print("Avg RTT = ", round((sum((rtt_list))/15),3), " ms")
    print("Packets lost = ", (packets_lost/15)*100, "%")
