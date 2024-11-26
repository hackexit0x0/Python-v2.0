#!/python3 

# Cliente

# import library *
import socket
# connetion creation (use ipv4 and Tcp)
Connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Servre ip and port (bind)
Connection.connect(("127.0.0.1", 8080))
# print message
print("[+] Connected to server...")