import socket

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('127.0.0.1', 9999)

while True:
    msg = input("Enter message for server: ")
    client_socket.sendto(msg.encode(), server_address)  # Send msg to server

    data, server = client_socket.recvfrom(1024)         # Receive reply
    print("Server:", data.decode())
