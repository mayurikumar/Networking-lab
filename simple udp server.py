# Networking-lab
import socket
UDP_IP_ADDRESS="10.1.24.120"                                                                              
UDP_PORT_NO=6789
serverSock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS,UDP_PORT_NO))
print("MESSAGE IS WAITING")
while True:
 data,addr=serverSock.recvfrom(1024)
 print ("Message: ", data)       
