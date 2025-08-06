import socket
# creating a socket
# s - server socket
# socket contains two arguments, by default - type of address (IPV4, IPV6), type of protocol(TCP/UDP)
s = socket.socket()
print('Socket is created')
# port number range 0 to 65535
s.bind(('localhost',19))
# decide at one point, how many clients you want to connect
s.listen(1)  # maintain buffer for 3 connections
print('Waiting for connections')
# to process multiple requests from client continuously
while True:
    # i want to accept a connection from the client
    c, addr = s.accept()  # it returns client socket and address
    name = c.recv(1024).decode()
    print('Connected with', addr, name)
    c.send(bytes('Welcome to socket connection','utf-8'))
    #c.send('Welcome to socket connection')
    c.close()