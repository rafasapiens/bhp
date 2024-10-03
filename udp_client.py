import socket
target_host = "127.0.0.1"
target_port = 9997
# create a socket object
#1 
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# send some data
#2 
client.sendto(b"AAABBBCCC",(target_host,target_port))
# receive some data
#3 
data, addr = client.recvfrom(4096)
print(data.decode())
client.close()

'''
As you can see, we change the socket type to SOCK_DGRAM 1 when creat-
ing the socket object. The next step is to simply call sendto() 2, passing in 
the data and the server you want to send the data to. Because UDP is a con-
nectionless protocol, there is no call to connect() beforehand. The last step 
is to call recvfrom() 3 to receive UDP data back. You will also notice that it 
returns both the data and the details of the remote host and port.
Again, we’re not looking to be superior network programmers; we want 
it to be quick, easy, and reliable enough to handle our day-to-day hacking 
tasks. Let’s move on to creating some simple servers.
'''
