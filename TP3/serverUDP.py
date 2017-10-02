import socket

UDP_IP_ADDRESS = "192.168.1.6"
UDP_PORT_NO = 1994

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

while True:
	data, addr = serverSock.recvfrom(1024)
	print "Message: ", data
