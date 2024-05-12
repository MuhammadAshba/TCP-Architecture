import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server
server_address = ('localhost', 8888)
print(f"Connecting to {server_address[0]} port {server_address[1]}")
client_socket.connect(server_address)

try:
    # Send data
    message = "Hello, server! This is wahab"
    print(f"Sending: {message}")
    client_socket.sendall(message.encode())

    # Receive data
    data = client_socket.recv(1024)
    print(f"Received: {data.decode()}")

finally:
    # Clean up the connection
    print("Closing the connection")
    client_socket.close()
