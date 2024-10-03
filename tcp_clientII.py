import socket
target_host = "0.0.0.0" #"www.google.com"
target_port = 9998 #80
# create a socket object
#1 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect the client
#2 
client.connect((target_host,target_port))
# send some data
#3 
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
# receive some data
#4 
response = client.recv(4096)
print(response.decode())
client.close()


"""
We first create a socket object with the AF_INET and SOCK_STREAM param-
eters 1. The AF_INET parameter indicates we’ll use a standard IPv4 address 
or hostname, and SOCK_STREAM indicates that this will be a TCP client. We 
then connect the client to the server 2 and send it some data as bytes 3. 
The last step is to receive some data back and print out the response 4 and 
then close the socket. This is the simplest form of a TCP client, but it’s the 
one you’ll write most often.
This code snippet makes some serious assumptions about sockets that 
you definitely want to be aware of. The first assumption is that our con-
nection will always succeed, and the second is that the server expects us to 
send data first (some servers expect to send data to you first and await your 
response). Our third assumption is that the server will always return data 
to us in a timely fashion. We make these assumptions largely for simplic-
ity’s sake. While programmers have varied opinions about how to deal 
with blocking sockets, exception-handling in sockets, and the like, it’s 
quite rare for pentesters to build these niceties into their quick-and-dirty 
tools for recon or exploitation work, so we’ll omit them in this chapter.


Primeiro, criamos um objeto de soquete com os parâmetros AF_INET e SOCK_STREAM 
1. O parâmetro AF_INET indica que usaremos um endereço IPv4 padrão 
ou nome de host, e SOCK_STREAM indica que este será um cliente TCP. 
Então, conectamos o cliente ao servidor 
2 e enviamos alguns dados como bytes 
3. 
A última etapa é receber alguns dados de volta e imprimir a resposta 
4 e então fechar o soquete. Esta é a forma mais simples de um cliente TCP, mas é a 
que você escreverá com mais frequência. 
Este trecho de código faz algumas suposições sérias sobre soquetes que 
você definitivamente quer estar ciente. A primeira suposição é que nossa conexão 
sempre terá sucesso, e a segunda é que o servidor espera que 
enviemos dados primeiro (alguns servidores esperam enviar dados para você primeiro e aguardam sua 
resposta).  Nossa terceira suposição é que o servidor sempre retornará dados para nós em tempo hábil. Fazemos essas suposições em grande parte por uma questão de simplicidade. Embora os programadores tenham opiniões variadas sobre como lidar com soquetes de bloqueio, tratamento de exceções em soquetes e coisas do tipo, é muito raro que os pentesters criem essas sutilezas em suas ferramentas rápidas e sujas para trabalho de reconhecimento ou exploração, então as omitiremos neste capítulo.

"""
