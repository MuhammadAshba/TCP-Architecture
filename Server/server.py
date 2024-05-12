import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_address = ('localhost', 8888)
print(f"Starting up on {server_address[0]} port {server_address[1]}")
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

while True:
    # Wait for a connection
    print("Waiting for a connection...")
    connection, client_address = server_socket.accept()

    try:
        print(f"Connection from {client_address}")

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            print(f"Received: {data.decode()}")

            if data:
                print("Sending back the data")
                connection.sendall(data)
            else:
                print(f"No more data from {client_address}")
                break

    finally:
        # Clean up the connection
        connection.close()
