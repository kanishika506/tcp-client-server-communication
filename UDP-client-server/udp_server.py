import socket

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind server to IP & Port
server_socket.bind(("127.0.0.1", 9999))
print("UDP Server is running and waiting for messages...")

while True:
    data, addr = server_socket.recvfrom(1024)   # Receive data from client
    print("Client:", data.decode())

    reply = input("Enter reply to client: ")
    server_socket.sendto(reply.encode(), addr)   # Send reply to client
