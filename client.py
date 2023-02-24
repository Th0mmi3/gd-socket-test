"""
import socket
import keyboard
import sys

import gd

# Handle arguments
clientName = sys.argv[1]


messages = ["Get good.", "RIP", "F", "bruh", "hm..."]
memory = gd.memory.get_memory()
do_print = True

HOST = "192.168.0.203"  # The server's hostname or IP address
PORT = 5555  # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
msg = f"{clientName} joined the server"
s.sendall(bytes(msg, "utf-8"))
data = s.recv(1024)
print(f"Received: {data!r}")

# The loop
while True:

    # Quit
    if keyboard.is_pressed('b'):
        break

    # Test the sending feature
    if keyboard.is_pressed('c'):
        s.sendall(b"a has been pressed")

    # Handle player deaths
    if memory.is_dead():  # if player is dead
        if do_print:
            msg = f"death"
            s.sendall(bytes(msg, "utf-8"))
            data = s.recv(1024)
            print(f"Received: {data!r}")
        do_print = False
    else:
        do_print = True
"""

import socket
import threading
import gd

IP = "0.tcp.eu.ngrok.io"
PORT = 17010
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

memory = gd.memory.get_memory()
do_print = True
revertDeath = False

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))
print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")

connected = True
while connected:
    msg = "!state"


    #print("are we looping?")

    # Handle player deaths

    if memory.is_dead():  # if player is dead
        if do_print:
            msg = "!died"
            client.send(msg.encode(FORMAT))
            print("print: player died ---------------------")
            do_print = False
    else:
        do_print = True
        msg = "!undie"
        print("print: im not dead")

    if msg == DISCONNECT_MSG:
        connected = False
    else:
        client.send(msg.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER {msg}]")

        if msg == "True":
            print("Someone died! ------------------------------")