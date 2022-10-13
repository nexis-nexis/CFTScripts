#import socket
import socket
 
# specify the IP
ip = '192.168.11.94'
 
ports =[]
for i in range (1, 1000):
# python will try this code and if there's any error, it will go to the exception
    try:
# build the socket with the socket function
# the first parameter is address family INTERNET it represent IPv4 address and SOCK.STREAM which is TCP
# these parameters define the socket.
        s = socket.socket(socket.AF_INET )
 
# use the connection function
#if there is a conncetion to this, it means that the port is open
        s.connect((ip,i))
        # if there is connection to this port and ip print the below statement
        print("{} port is open".format(i))
        ports.append(i)
        s.close()
    except:
             s.close()
             #pass
 
print(ports)
 
