### socket_server.py
import socket

# Define host and port for the server to listen on
HOST = '127.0.0.1'
PORT = 65432  # Any number between 1024–65535

# Create a TCP/IP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  # Bind the socket to the address and port
    s.listen()  # Listen for incoming connections
    print(f"[+] Server listening on {HOST}:{PORT}")
    
    conn, addr = s.accept()  # Accept a connection
    with conn:
        print(f"[+] Connected by {addr}")
        while True:
            data = conn.recv(1024)  # Receive data from the client
            if not data:
                print("[!] No data received. Closing connection.")
                break  # Break the loop if no data is received
            print(f"[Client]: {data.decode()}")  # Print the client message
            conn.sendall(b"Message received!")  # Send a response back to the client

