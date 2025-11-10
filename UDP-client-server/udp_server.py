import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #.af_inet for ipv4 ,sock_dgram for connectionless udp
sock.bind(('127.0.0.1',12345)) #binding the socket to ip and port

while True:
    data,addr=sock.recvfrom(1024)  #1024 is no. of byte than can be received
    #in udp we use recvfrom instead of recv that was being used in tcp bcz 
    # in udp there is no connection established b/w client and server ,
    # their for we nee to provide data as well as address

    msg=bytes("HELLO UDP CLIENT").encode('utf-8') 

    sock.sendto(msg,addr)  #in udp we use sendto instead of send that was being used in tcp bcz
    # in udp there is no connection established b/w client and server ,
    # their for we nee to provide data as well as address