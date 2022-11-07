import socket 
import threading

## define as portas e o servidor
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

## cria o socket com tipo de conexao com internet e streaming de dados
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

## define a funçao cliente e conecta com os endereços informados
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    ## conectado ele envia os dados
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()
        
## define a funçao start que inicia a troca de dados com o servidor
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

## chama a funçao start
print("[STARTING] server is starting...")
start()

