import socket
#import gd
import sys

IP = sys.argv[1]
PORT = int(sys.argv[2])
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

# memory = gd.memory.get_memory()
do_print = True
invincibility = False

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))
print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")

connected = True
while connected:
    msg = "!state"
    #print("are we looping?")

    # Handle player deaths

    """
    if memory.is_dead():  # if player is dead
        if do_print:
            msg = "!died"
            #client.send(msg.encode(FORMAT))
            do_print = False
        else:
            "zmsg = "!undie"
    else:
        do_print = True
    """


    if msg == DISCONNECT_MSG:
        connected = False
    else:
        client.send(msg.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        #print(f"[SERVER {msg}]")

        if msg == "True":
            print("Someone died! ------------------------------")

            #memory.player_kill()

