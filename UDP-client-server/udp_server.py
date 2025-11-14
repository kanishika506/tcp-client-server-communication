import socket

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind server to IP & Port
sock.bind(("127.0.0.1", 12345))
print("UDP Server is running and waiting for messages...")

while True:
    data, addr = sock.recvfrom(1024)   # Receive data from client
    print(str(data))
    msg=bytes("HELLO UDP CLIENT").encode('utf-8')
    sock.sendto(msg,addr)
    
