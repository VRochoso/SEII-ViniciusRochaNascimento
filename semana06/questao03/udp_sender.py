import socket
import time
import sys

## define IP e portas
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
buf = 1024
file_name = sys.argv[1]

## inicia o socket e envia o arquivo para o endereço 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(file_name, (UDP_IP, UDP_PORT))
print "Sending %s ..." % file_name

## abre o arquivo em formato leitura
f = open(file_name, "r")
data = f.read(buf)
while(data):
    if(sock.sendto(data, (UDP_IP, UDP_PORT))):
        ## le o arquivo e da um tempo para ele salvar
        data = f.read(buf)
        time.sleep(0.02) 

## fecha o socket e o arquivo
sock.close()
f.close()
