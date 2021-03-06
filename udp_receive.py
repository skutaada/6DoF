import socket

UDP_IP = ''
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    try:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print("receive message", data.decode(encoding="utf-8"))
    except Exception:
        print ('\nExit . . .\n')
        break