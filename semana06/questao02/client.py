import socket


## define as portas e o servidor 
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.26"
ADDR = (SERVER, PORT)

## cria o socket com tipo de conexao com internet e streaming de dados
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

## define uma funçao de envio de msg
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

## chama a funçao
send("Hello World!")
input()
send("Hello Everyone!")
input()
send("Hello Tim!")

## disconecta do servidor
send(DISCONNECT_MESSAGE)


