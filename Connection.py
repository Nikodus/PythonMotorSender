import socket
import time
from threading import Thread


class Connection:

    def __init__(self, ip: str = "127.0.0.1", port: int = 7777):
        self.__ip = ip
        self.__port = port
        self.__motorindex = 0
        self.__conn = None

    def connect(self):
        if not self.isConnected():
            connection_thread = Thread(target=self.__threaded_connect, daemon=True)
            connection_thread.start()

    def send(self, msg: str = ""):
        if self.__conn != None:
            msg = msg + "_" + str(self.__motorindex)
            self.__conn.sendall(bytes(msg + "\r", 'utf-8'))
        else:
            print("Send failed!")

    def __threaded_connect(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.__ip, self.__port))
            s.listen()
            self.__conn, addr = s.accept()
            with self.__conn:
                print(f"Connected with {addr}")
                while True:
                    try:
                        self.__conn.send(bytes("KA" + "\r", 'utf-8'))
                        time.sleep(0.1)
                    except:
                        self.__conn = None
                        return

    def isConnected(self):
        if self.__conn != None:
            return True
        return False

    def setMotorindex(self, motor: int):
        if motor >= 1:
            self.__motorindex = 1
        if motor <= 0:
            self.__motorindex = 0

    def getMotorindex(self):
        return self.__motorindex
