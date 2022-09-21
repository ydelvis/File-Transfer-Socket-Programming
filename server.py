""""
Internet Programming Design - Group Project Work

Group Members:
Elvis Yeboah-Duako (202124080120)
Worae Daniel Adu (202124080119)
Rayan Anwar Mohamed Alawad (202114010103)

Server Name = ElWadRay   --- just a nice combination of our names :)
"""

import socket
import tqdm
import os

print('[starting] server is starting... \n \nWelcome to ElWadRay Servers!\n ')

# device's IP address
SERVER_HOST = host = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 5001

# receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

# create the server socket
# TCP socket
s = socket.socket()

# bind the socket to our local address
s.bind((SERVER_HOST, SERVER_PORT))

# enabling our server to accept connections
# 5 here is the number of unaccepted connections that
# the system will allow before refusing new connections
s.listen(5)
print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}\n")

# accept connection if there is any
client_socket, address = s.accept() 
# if below code is executed, that means the sender is connected
print(f"[+] {address} is connected. \n \n Preparing to receive File ... \n \n Ready to receive File from Client\n")

# receive the file infos
# receive using client socket, not server socket
received = client_socket.recv(BUFFER_SIZE).decode()


filename, filesize = received.split(SEPARATOR)
# remove absolute path if there is
filename = os.path.basename(filename)

#appending the server location for file to be stored
filename = 'serverData/' + str(filename)

# convert to integer
filesize = int(filesize)


# start receiving the file from the socket
# and writing to the file stream
progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "wb") as f:
    while True:
        # read 1024 bytes from the socket (receive)
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:    
            # nothing is received
            # file transmitting is done
            break
        # write to the file the bytes we just received
        f.write(bytes_read)
        # update the progress bar
        progress.update(len(bytes_read))

# close the client socket

client_socket.close()
# close the server socket
s.close()
