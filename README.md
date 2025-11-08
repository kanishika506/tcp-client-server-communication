# tcp-client-server-communication
This repository contains a simple implementation of TCP Client-Server communication in C using the socket programming APIs:
->socket()
->bind()
->listen()
->accept()
->connect()
->send()
->recv()

The purpose of this project is to demonstrate how TCP communication works between a client and a server using standard Berkeley socket functions.

TCP (Transmission Control Protocol) is a connection-oriented, reliable communication protocol. In this project:

The Server waits for a client request, accepts the connection, receives a message from the client, and sends a response back.
The Client establishes a connection to the server, sends a message, and receives a response.
This project helps understand the basic flow of TCP communication.

---Flow of Execution---

1.Server->
      Creates a socket.
      Binds it to an IP & port.
      Listens for incoming connections.
      Accepts a client.
      Receives and sends messages.

2.Client->

      Creates a socket
      Connects to server
      Sends a message
      Receives server response
