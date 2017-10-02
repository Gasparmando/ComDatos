import socket

UDP_IP_ADDRESS = "192.168.1.6"
UDP_PORT_NO = 1994
Message = "Hola Servidor UDP"

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

clientSock.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT_NO))
