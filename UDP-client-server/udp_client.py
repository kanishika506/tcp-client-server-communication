import socket

client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #.af_inet for ipv4 ,sock_dgram for connectionless udp

msg="HELLO ! UDP SERVER"

client_socket.sendto(msg.encode('utf-8'),('127.0.0.1',12345))
data,addr=client_socket.recvfrom(1024)
print("SERVER SAYS:")
print(str(data))
client_socket.close()