#include <sys/types.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string.h>
#include <netdb.h>
#include <stdio.h>
#include <sys/stat.h>
#include <unistd.h>
#include <fcntl.h>
#ifdef __USE_MISC
#ifndef __u_char_defined
#define __u_char_defined
#endif
#endif
#define SERVERPORT 8887
#define MAXBUF 1024

int main(int argc,char* argv[])
{
int sockd,counter,fd;
struct sockaddr_in xferServer;
char buf[MAXBUF];
int returnStatus;
if(argc<3)
{
exit(1);
}
sockd=socket(AF_INET,SOCK_STREAM,0);

xferServer.sin_family=AF_INET;
xferServer.sin_addr.s_addr=inet_addr(argv[1]);
xferServer.sin_port=htons(SERVERPORT);
int restat=connect(sockd,(struct sockaddr*)&xferServer,sizeof(xferServer));
if(restat==-1)
fprintf(stderr,"Could not connect to server");
write(sockd,argv[2],strlen(argv[2])+1);
shutdown(sockd,SHUT_WR);
fd=open(argv[3],O_WRONLY|O_CREAT|O_APPEND);
while((counter=read(sockd,buf,MAXBUF))>0)
write(fd,buf,counter);
close(sockd);
return 0;
}
