#!/python3 

# Server.

# import library *
import socket
# connetion creation (use ipv4 and Tcp)
Connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Servre ip and port (bind)
Connection.bind(("127.0.0.1", 8080))
# listening
print("[+] Listening.....")
Connection.listen(1)
# accept connection