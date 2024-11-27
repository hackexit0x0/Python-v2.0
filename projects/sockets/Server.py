#!/python3 

# Server.

# import library *
import socket
# connetion creation (use ipv4 and Tcp)
Connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# remove kernal sleep mode
Connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Servre ip and port (bind)
Connection.bind(("127.0.0.1", 8080))
# listening
print("[+] Listening.....")
Connection.listen(1)
# accept connection
Client, address = Connection.accept()
# print message
print("[+] Accepted connection..")
# send message

# while loop
while True:
    # input shell Command
    KernalInput = input(">> ")
    if KernalInput.lower() == "exit":
        break
    Client.send(KernalInput.encode())
    ClientOutput = Client.recv(1024).decode()
    print(ClientOutput)
