import socket
import threading

HOST = '192.168.100.122'
PORT = 12345

# Suponhamos que o hotel tenha 10 quartos
rooms = [False] * 10  # False indica que o quarto está livre

waiting_clients = {}

def handle_client(conn, addr):
    while True:
        msg = conn.recv(1024).decode('utf-8')
        if not msg:
            break
        
        cmd, *args = msg.split()

        if cmd == "RESERVE":
            requested_rooms = list(map(int, args))
            available_rooms = [i for i, r in enumerate(rooms) if not r and i in requested_rooms]

            if set(requested_rooms) == set(available_rooms):
                for i in requested_rooms:
                    rooms[i] = True
                conn.sendall(b'ROOMS_RESERVED')
            else:
                waiting_clients[addr] = requested_rooms
                conn.sendall(b'WAITING_FOR_ROOMS')

        elif cmd == "CANCEL":
            valid_rooms = True
            for i in list(map(int, args)):
                if 0 <= i < len(rooms):
                    rooms[i] = False
                else:
                    valid_rooms = False

            clients_to_remove = []
            for client, r_rooms in waiting_clients.items():
                if set(r_rooms).issubset(set([i for i, r in enumerate(rooms) if not r])):
                    clients_to_remove.append(client)

            for client in clients_to_remove:
                waiting_clients.pop(client)

            if valid_rooms:
                conn.sendall(b'RESERVATION_CANCELLED')
            else:
                conn.sendall(b'INVALID_ROOM_NUMBER')
                        
    conn.close()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Servidor de reservas iniciado. Esperando conexões...")

        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    start_server()
