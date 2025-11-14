import socket

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg="HELLO ! UDP SERVER"
client_socket.sendto(msg.encode('utf-8'),('127.0.0.1',12345))
data,addr=client_socket.recvfrom(1024)
print("SERVER SAYS:")
print(str(data))
client_socket.close()
