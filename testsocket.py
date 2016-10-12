import socket
import os
import sys

def retBanner(ip, port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip, port))
		banner = s.recv(1024)
		return banner
	except:
		return "nao deu"

if len(sys.argv)==3:
	ip = sys.argv[1]
	port = int(sys.argv[2])
	bananer = retBanner(ip, port)
 	print bananer
else:
	print "nenhum ip fornecido"
	exit()

