import socket
import threading

HOST = '192.168.100.122'
PORT = 12345

# Inicializando o relógio lógico do servidor em 0
server_clock = 0

# Suponhamos que o hotel tenha 10 quartos
rooms = [False] * 10
waiting_clients = {}

def handle_client(conn, addr):
    global server_clock
    while True:
        msg = conn.recv(1024).decode('utf-8')
        if not msg:
            break

        # Tentando desempacotar a mensagem com segurança
        parts = msg.split()
        if len(parts) < 2:
            conn.sendall(b'INVALID_REQUEST')
            continue
        
        client_clock, cmd, *args = parts

        # Ajustando o relógio lógico
        server_clock = max(server_clock, int(client_clock)) + 1
        print(f"Relógio lógico do servidor atualizado para: {server_clock}")

        if cmd == "RESERVE":
            requested_rooms = list(map(int, args))
            available_rooms = [i for i, r in enumerate(rooms) if not r and i in requested_rooms]

            if set(requested_rooms) == set(available_rooms):
                for i in requested_rooms:
                    rooms[i] = True
                conn.sendall(f"{server_clock} ROOMS_RESERVED".encode('utf-8'))
            else:
                waiting_clients[addr] = requested_rooms
                conn.sendall(f"{server_clock} WAITING_FOR_ROOMS".encode('utf-8'))

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
                conn.sendall(f"{server_clock} RESERVATION_CANCELLED".encode('utf-8'))
            else:
                conn.sendall(f"{server_clock} INVALID_ROOM_NUMBER".encode('utf-8'))

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
