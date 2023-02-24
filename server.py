""""
import socket

HOST = "192.168.0.203"  # Standard loopback interface address (localhost)
PORT = 5555  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

            print(f"{data} was send by {addr}")
"""

import socket
import threading

IP = "localhost"
PORT = 5555
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

print("[STARTING SERVER]")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen()
print(f"[LISTENING] Server is listening on {IP}:{PORT}")

serverDeath = False


def handle_client(conn, addr):
    global serverDeath
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg = conn.recv(SIZE).decode(FORMAT)

        if msg == DISCONNECT_MSG:
            connected = False

        if msg == "!died":
            serverDeath = True

        if msg == "!undie":
            serverDeath = False

        print(f"[{addr}] {msg}")
        returnMsg = f"{str(serverDeath)}"
        conn.send(returnMsg.encode(FORMAT))

    conn.close()


while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
