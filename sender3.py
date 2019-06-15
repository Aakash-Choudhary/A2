#!/usr/bin/python3

import socket
recv_ip="127.0.0.1"
recv_port=4444 #0-1024 -- all the numbers are free for port number outside this range

#creating udp socket
#              IPtype V4         udp
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while 4 > 3:
	msg=input("please enter your message : ")
	#converting string to bytes like object
	nmsg=msg.encode('ascii')
#sending  data to reciever
s.sendto(nmsg,(recv_ip,recv_port))
print(s.recvfrom(10))
