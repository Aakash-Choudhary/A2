#!/usr/bin/python2

import socket
recv_ip="127.0.0.1"
recv_port=4444 #0-1024 -- all the numbers are free for port number outside this range

#creating udp socket
#              IPtype V4         udp
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#fitting        ip and port with udp socket
s.bind((recv_ip,recv_port))    #bind support tuple datatype

#recieve data from sender
while 4 > 2:
	data=s.recvfrom(100)
	print("message from sender " ,data[0])
	print("sender IP + port --socket  ",data[1])
	#reply to sender
	reply = raw_input("type your reply  : ")
	s.sendto(reply,data[1])

si.close()
