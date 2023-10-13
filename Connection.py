import socket
from threading import Thread

class Connection:

    __active_connection = None


    def __init__(self, ip:str = "127.0.0.1", port:int = 7777 ):
        self.ip = ip
        self.port = port

    def connect(self):
        def threaded_connect():
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((self.ip, self.port))
                s.listen()
                conn, addr = s.accept()
                with conn:
                    print(f"Connected with {addr}")
                    Connection.active_connection = conn

        connection_thread = Thread(target=threaded_connect,daemon=True)
        connection_thread.start()


    def send(self, msg:str = ""):
        if self.__active_connection != None:
            self.__active_connection.sendall(bytes(msg+"\r", 'utf-8'))
        else:
            print("Send failed!")



    def isConnected(self):
        if self.__active_connection != None:
            return True
        return False
