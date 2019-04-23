import socket
import struct

# Create UDP socket.
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to LFS.
sock.bind(('', 5005))

while True:
    # Receive data.
    data = sock.recv(256)
    print(data)

    if not data:
        break # Lost connection
  
    # Unpack the data.
    outsim_pack = struct.unpack('I12f3i', data)
    time = outsim_pack[0]
    angvel = [outsim_pack[1], outsim_pack[2], outsim_pack[3]]
    header = outsim_pack[4]
    pitch = outsim_pack[5]
    roll = outsim_pack[6]
    accel = [outsim_pack[7], outsim_pack[8], outsim_pack[9]]
    vel = [outsim_pack[10], outsim_pack[11], outsim_pack[12]]
    pos = [outsim_pack[13], outsim_pack[14], outsim_pack[15]]
    print(outsim_pack)

# Release the socket
sock.close()
