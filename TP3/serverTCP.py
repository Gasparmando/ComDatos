import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('192.168.1.6', 1998)
sock.bind(server_address)

sock.listen(1)

while True:
	print >>sys.stderr, 'Esperando una conexion ...'
	connection, client_address = sock.accept()
	
	try:
		print >>sys.stderr, 'Conexion de', client_address
		while True:
			data = connection.recv(16)
			print >>sys.stderr, 'Recibido "%s"' % data
			if data:
				print >>sys.stderr, 'Reenviando data al cliente'
				connection.sendall(data)
			else:
				print >>sys.stderr, 'no mas data de', client_address
				break
	finally:
		connection.close()
	
	
