### socket_client.py
import socket  # Import socket library

# Define server information to connect to
HOST = '127.0.0.1'  # Server IP address (localhost)
PORT = 65432        # Port used by the server
MESSAGE = "Hello, server!"  # Message to send

def main():
    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect((HOST, PORT))  # Connect to the server
            print(f"[+] Connected to server at {HOST}:{PORT}")
            client_socket.sendall(MESSAGE.encode('utf-8'))  # Send encoded message
            print(f"[>] Sent: {MESSAGE}")
            response = client_socket.recv(1024)  # Receive server's response
            print(f"[<] Received: {response.decode('utf-8')}")
        except ConnectionRefusedError:
            print(f"[!] Could not connect to server at {HOST}:{PORT}. Is the server running?")
        except socket.error as err:
            print(f"[!] Socket error: {err}")
        except Exception as exc:
            print(f"[!] Unexpected error: {exc}")

if __name__ == "__main__":
    main()
