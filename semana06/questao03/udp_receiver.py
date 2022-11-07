import socket
import select

## define IP e portas
UDP_IP = "127.0.0.1"
IN_PORT = 5005
timeout = 3

## inicia o socket nos devidos endereços
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, IN_PORT))

while True:
    ## recebe endereço e dados do do udp_sender e mostra na tela
    data, addr = sock.recvfrom(1024)
    if data:
        print "File name:", data
        file_name = data.strip()

    ## abre o documento
    f = open(file_name, 'wb')

    while True:
        ## salva os dados recebidos em uma lista
        ready = select.select([sock], [], [], timeout)
        if ready[0]:
            data, addr = sock.recvfrom(1024)
            f.write(data)
        else:
            ## se nao receber mais dados finaliza o programa
            print "%s Finish!" % file_name
            f.close()
            break
