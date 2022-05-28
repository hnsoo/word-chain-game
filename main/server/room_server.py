import threading
import socket

class Room_thread(threading.Thread):
    def __init__(self, title):
        super().__init__()
        self.title = title

    def run(self):
        # 룸 생성 로직
        room = Room()

class Room:
    def __init__(self):
        self.room_server_socket = None
        self.create_listening_server()


    def create_listening_server(self):
        # 소켓 생성
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        HOST = '127.0.0.1'
        PORT = 55555
        # 소켓 레벨과 데이터 설정
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 소켓을 네트워크(주소, 포트)에 연결
        self.server_socket.bind((HOST, PORT))
        print("Listening for incoming messages..")
        # 최대 20명까지 listen
        self.server_socket.listen(4)
        self.receive_new_user()