from socket import *
from time import gmtime, strftime

address = ('192.168.192.6', 6000)
clients = []

socket = socket(AF_INET, SOCK_DGRAM)
socket.bind(address)
# never stop listening on the port
socket.setblocking(0)

while True:
    try:
        data, addr = socket.recvfrom(1024)
        print(data, addr)
        if "/quit" == str(data):
            if addr in clients:
                clients.remove(addr)
                print('client: %s' % (addr), "removed")

        else:
            if addr not in clients:
                clients.append(addr)

            print(str(data), ",", str(addr), strftime("%Y-%m-%d %H:%M:%S", gmtime()))
            for client in clients:
                if client != addr:
                    socket.sendto(data, client)
    except:
        pass
socket.close()