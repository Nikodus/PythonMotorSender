import socket

HOST = "192.168.243.86"  # Ip Addresse für das AGV (ESP)
PORT = 65432  # Port für das AGV (ESP)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
           conn.sendall(bytes(input("Command:")+"\r", 'utf-8'))
