import socket
import threading

### LISTEN TCP CONN. ###
def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    try:
        while True:
            # Receive data from the client (up to 1024 bytes)
            data = client_socket.recv(1024)
            if not data:
                break  # No data, connection closed by the client
            print(f"Received: {data.decode()} from {client_address}")
            # Send a response to the client
            client_socket.send(b"ACK: Message received\n")
    except Exception as e:
        print(f"Error handling client {client_address}: {e}")
    finally:
        # Close the client connection
        print(f"Closing connection from {client_address}")
        client_socket.close()

# Set up the server to listen on a specific port
def start_server(host='0.0.0.0', port=8080):
    # Create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))  # Bind to the host and port
    server.listen(4096)  # Set the backlog for pending connections to 4096

    print(f"[*] Listening on {host}:{port}...")

    while True:
        # Accept a new connection from a client
        client_socket, client_address = server.accept()
        # Create a new thread to handle the client connection
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()  # Start the thread

start_server()