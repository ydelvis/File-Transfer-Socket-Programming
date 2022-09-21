""""
Internet Programming Design - Group Project Work

Group Members:
Elvis Yeboah-Duako (202124080120)
Worae Daniel Adu (202124080119)
Rayan Anwar Mohamed Alawad (202114010103)
"""

import socket
import tqdm   # pip install tqdm  (if module not already installed) - Used to show progress of file transfer
import os

print("Professor Tang Yong's PC is Online ...\n")
SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

# the ip address or hostname of the server, the receiver
host = socket.gethostbyname(socket.gethostname())

# the port, let's use 5001
port = 5001

#Get name of file to be sent -- the file must exist in the clientData folder

namefile = str(input("Enter filename with extension to send: "))

filename = "clientData/"+namefile

# get the file size
filesize = os.path.getsize(filename)

# create the client socket
s = socket.socket()

# Connecting to the Server
print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")

# send the filename and filesize

print('Sending File Name to Server ...\n')
s.send(f"{filename}{SEPARATOR}{filesize}".encode())

# start sending the file
progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    while True:
        # read the bytes from the file
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            # file transmitting is done
            break
        # we use sendall to assure transimission in 
        # busy networks
        s.sendall(bytes_read)
        # update the progress bar
        progress.update(len(bytes_read))
# close the socket


s.close()


