import socket
from .chat import User_chat
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.10.3'
port = 5500

client_socket.connect((host, port))

client_socket.sendall(User_chat.user_input)

data = client_socket.recv(1024)

print("Recieved from usman computer : ", data.decode())

client_socket.close()
