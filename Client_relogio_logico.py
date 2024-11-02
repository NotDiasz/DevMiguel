import socket

HOST = '192.168.100.122'
PORT = 12345

# Inicializando o relógio lógico do cliente em 0
client_clock = 0

def reserve_rooms(*room_numbers):
    global client_clock

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        s.sendall((f"{client_clock} RESERVE " + " ".join(map(str, room_numbers))).encode('utf-8'))
        response = s.recv(1024).decode('utf-8')
        
        server_clock, msg = response.split(" ", 1)
        client_clock = max(client_clock, int(server_clock)) + 1
        print(f"Relógio lógico do cliente atualizado para: {client_clock}")

        if msg == 'ROOMS_RESERVED':
            print(f"Quartos {', '.join(map(str, room_numbers))} reservados com sucesso!")
        elif msg == 'WAITING_FOR_ROOMS':
            print(f"Em espera pelos quartos {', '.join(map(str, room_numbers))}.")

def cancel_reservation(*room_numbers):
    global client_clock

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        s.sendall((f"{client_clock} CANCEL " + " ".join(map(str, room_numbers))).encode('utf-8'))
        response = s.recv(1024).decode('utf-8')

        server_clock, msg = response.split(" ", 1)
        client_clock = max(client_clock, int(server_clock)) + 1
        print(f"Relógio lógico do cliente atualizado para: {client_clock}")

        if msg == 'RESERVATION_CANCELLED':
            print(f"Reserva para os quartos {', '.join(map(str, room_numbers))} foi cancelada.")
        elif msg == 'INVALID_ROOM_NUMBER':
            print(f"Um ou mais quartos informados não são válidos. Por favor, tente novamente.")

if __name__ == "__main__":
    action = input("Você deseja 'reservar' ou 'cancelar' quartos? ").strip().lower()
    room_numbers = list(map(int, input("Digite os números dos quartos (separados por espaço): ").split()))

    if action == 'reservar':
        reserve_rooms(*room_numbers)
    elif action == 'cancelar':
        cancel_reservation(*room_numbers)
