'''
    Simple Client
'''


import socket
import json
from time import sleep

i = 0
while i < 30:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('192.168.4.1', 6060))
    
    data = {
        "todo": 1,
    }
    client.send(json.dumps(data).encode())
    print(client.recv(1024))
    sleep(2)

    client.close()
    negdata = {
        "todo": 0,
    }

    nclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    nclient.connect(('192.168.4.1', 6060))
    nclient.send(json.dumps(negdata).encode())
    print(nclient.recv(1024))
    sleep(2)
    client.close()

    i += 2