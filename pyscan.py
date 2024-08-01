import sys
import socket
from datetime import datetime


asciiart="""
██████╗ ██╗   ██╗███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗╚██╗ ██╔╝██╔════╝██╔════╝██╔══██╗████╗  ██║
██████╔╝ ╚████╔╝ ███████╗██║     ███████║██╔██╗ ██║
██╔═══╝   ╚██╔╝  ╚════██║██║     ██╔══██║██║╚██╗██║
██║        ██║   ███████║╚██████╗██║  ██║██║ ╚████║
╚═╝        ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
"""

usage="pytho3 pyscan <IP/hostname>"
print(asciiart)

if len(sys.argv)==2:
	target= socket.gethostbyname(sys.argv[1])
else:
	print(usage)
	exit(0)
#Banner:
print("-" * 50)
print("Scanning Target "+ sys.argv[1]+" IP: " + target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
	for port in range(0,1024):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result ==0:
			print("Port {} is open".format(port))
		s.close()
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
except socket.gaierro:
	print("Hostname could not be resolved.")
	sys.exit()
except socket.error:
	print("Could not connect to server.")
	sys.exit()