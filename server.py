import socket
import threading
import sys

# Handle arguments
IP = "localhost"
PORT = 5555
if len(sys.argv) >= 2:
    IP = sys.argv[1]
if len(sys.argv) >= 3:
    PORT = sys.argv[2]

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
