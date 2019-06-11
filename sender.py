#!/usr/bin/python2

import socket
recv_ip="127.0.0.1"
recv_port=4444 #0-1024 -- all the numbers are free for port number outside this range

#creating udp socket
#              IPtype V4         udp
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#sending  data to reciever
s.sendto("hello",(recv_ip,recv_port))
