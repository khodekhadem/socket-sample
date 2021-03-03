import socket
import random
import time

def socket_server () :
	
	sonnection = 0
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((socket.gethostbyname('192.168.1.40'), int(input("enter port : "))))
	s.listen()
	clientsocket, address = s.accept()
	
	while True:
		print(f"Connection from {address}")
		msg = input('write message')
		clientsocket.send(bytes(msg,"utf-8"))
		if msg == 'ex':
			clientsocket.close()

socket_server()

