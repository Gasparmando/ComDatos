import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 1998)
print>>sys.stderr, 'conectando a %s port %s' % server_address

sock.connect(server_address)

try:
	message = 'Hola Servidor TCP como estas'
	print >>sys.stderr, 'enviando "%s"' % message
	sock.sendall(message)

	amount_received = 0
	amount_expected = len(message)
	
	while amount_received < amount_expected:
		data = sock.recv(16)
		amount_received += len(data)
		print >>sys.stderr, 'recibido "%s"' % data

finally:
	print >>sys.stderr, 'closing socket'
	sock.close()
