import socket

HOST = "192.168.243.86"  # Ip Addresse für das AGV (ESP)
PORT = 65432  # Port für das AGV (ESP)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))    # Erstellt den Server
    s.listen()
    conn, addr = s.accept()     # Wartet bis das AGV (ESP) antwortet
    with conn:
        print(f"Connected by {addr}")   # Printet die Verbindung
        while True:
           conn.sendall(bytes(input("Command:")+"\r", 'utf-8'))     # Code fürs senden von Befehlen (Debug Tool)
