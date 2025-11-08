#include <stdio.h> //for standard input output like printf(),scanf() ....
#include <stdlib.h> //for standard library function like malloc(),free() ....
#include <string.h>  //for string handling library 
#include <sys/socket.h> //socket programming interface
#include <sys/types.h>  // basic derived types 
#include <netinet/in.h> //this have defination of internet protocol family ,contain port and ip address  definition 
#include <arpa/inet.h> //definitions for internet operations like inet_addr

#define PORT 5555  //hard coded means not changeable port number

void main(){
    int sockfd;
    struct sockaddr_in serverAddr; //structure to hold server address details
    int newsocket;
    struct sockaddr_in newAddr;
    socklen_t addr_size;
    char buffer[1024]; //data buffer to hold data
    sockfd= socket(PF_INET,SOCK_STREAM,0); //create socket
    /* pf_init = protocol family , sock_stream is for tcp ,sock_datagram for udp , 0 for any best protocol*/
    printf("server socket created successfully\n");
    memset(&serverAddr ,'\0' ,sizeof(serverAddr)); //initialize server address structure with null value
    serverAddr.sin_family=AF_INET;
    serverAddr.sin_port=htons(PORT); //host to network short conversion for port number
    serverAddr.sin_addr.s_addr=inet_addr("127.0.0.1"); //convert ip address to binary format and store in server address structure
    //connect to server
    bind(sockfd,(struct sockaddr*)&serverAddr,sizeof(serverAddr));
    printf("bind to port %d \n",PORT);
    listen(sockfd,6); //server is listening for client connection
    printf("listening....\n"); 
    
    newsocket=accept(sockfd,(struct sockaddr*)&newAddr,&addr_size);
    strcpy(buffer,"Hello from server");
    send(newsocket,buffer,strlen(buffer),0);

    printf("closing connection....\n");
    }  