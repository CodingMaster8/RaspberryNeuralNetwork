import io
import socket
import struct
from PIL import Image


#PC configuration
server_address = 'raspberry_pi_ip_address' #Replace this with the Rapsberry
server_port = 8000

#Connect to the Raspberry Pi
client_socket = socket.socket()
client_socket.connect((server_address, server_port))
connection =  client_socket.makefile('rb')

try:
    while True:
        #Read Image Length
        image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]

        #Read Image Data
        image_stream = io.BytesIO(connection.read(image_len))

        #Display image or save it to a file
        image = Image.open(image_stream)
        image.show()

finally:
    connection.close()
    client_socket.close()