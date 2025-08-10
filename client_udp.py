import socket


client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    while True:
        msg = input(str("Mensagem: ")) + "\n"
        client.sendto(msg.encode(), ("192.168.200.229", 4433))
        data, sender = client.recvfrom(1024)
        print(sender[0] + ": " + data.decode())
        if data.decode() == "sair\n" or msg == "sair\n":
            break

    client.close()
except Exception as erro:
    print("Erro de conexão")
    print(erro)
    client.close()