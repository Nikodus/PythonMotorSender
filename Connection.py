import socket
from threading import Thread

class Connection:

    conn = None


    def __init__(self, ip:str = "127.0.0.1", port:int = 7777 ):
        self.ip = ip
        self.port = port

    def connect(self):
        if not self.isConnected():
            connection_thread = Thread(target=self.__threaded_connect,daemon=True)
            connection_thread.start()


    def send(self, msg:str = ""):
        if self.conn != None:
            self.conn.sendall(bytes(msg+"\r", 'utf-8'))
        else:
            print("Send failed!")


    def __threaded_connect(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.ip, self.port))
            s.listen()
            self.conn, addr = s.accept()
            with self.conn:
                print(f"Connected with {addr}")
                while True:
                    None

    def isConnected(self):
        if self.conn != None:
            return True
        return False
