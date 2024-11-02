import socket
import threading

HOST = '192.168.100.122'
PORT = 12345

peer_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
peer_socket.bind((HOST, PORT))

def receive():
    while True:
        message, addr = peer_socket.recvfrom(1024)
        print(f"[{addr}] {message.decode('utf-8')}")

listener_thread = threading.Thread(target=receive)
listener_thread.daemon = True
listener_thread.start()

while True:
    target_ip = input("Digite o IP do destinatário (ou 'sair' para encerrar): ")
    if target_ip.lower() == 'sair':
        break

    target_port = int(input("Digite a porta do destinatário: "))
    message_to_send = input("Digite sua mensagem: ")

    peer_socket.sendto(message_to_send.encode('utf-8'), (target_ip, target_port))
