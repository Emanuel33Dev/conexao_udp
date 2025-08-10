import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(5)

try:
    client.connect(('192.168.200.229', 4466))

    client.send(b'Ola, Tem alguem ai?\n')
    pacotes_recebidos = client.recv(1024).decode()
    print(pacotes_recebidos)
except:
    print("Um erro aconteceu!")