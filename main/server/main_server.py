import socket
import threading
import pickle

import room_server


class Main:
    # clients_list = []
    user_name_list = []
    current_room = [0, 0, 0, 0]

    def __init__(self):
        # self.create_rooms()
        self.main_server_socket = None
        # bind and listen
        self.create_listening_server()

    # def create_rooms(self):
    #     for i in range(4):
    #         title = "Room {}".format(i)
    #         t = room_server.Room_thread(title)
    #         t.start()

    def create_listening_server(self):
        # 소켓 생성
        self.main_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        HOST = '127.0.0.1'
        PORT = 10319
        # 소켓 레벨과 데이터 설정
        self.main_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 소켓을 네트워크(주소, 포트)에 연결
        self.main_server_socket.bind((HOST, PORT))
        print("Listening for incoming messages..")
        # 최대 20명까지 listen
        self.main_server_socket.listen(20)
        self.receive_new_user()

    def receive_data(self, so, ip, port):
        while True:
            input_data = so.recv(256).decode('utf-8')
            # 닉네임 중복 확인
            if input_data[:10] == '/register/':
                user_name = input_data[10:]
                if user_name not in self.user_name_list:
                    self.user_name_list.append(user_name)
                    so.send('yes'.encode('utf-8'))
                    print('[IP: {}, PORT: {}] 닉네임 {} 등록 성공'.format(ip, port, user_name))
                print('user_name_list: {}'.format(self.user_name_list))
            elif input_data[:8] == '/refresh':
                # 현재 방 인원 리스트를 직렬화 후 전송
                so.send(pickle.dumps(self.current_room))
            # if input_data[:6] == '/room/':
            #     room_num = input_data[6]

    def receive_new_user(self):
        while True:
            so, (ip, port) = self.main_server_socket.accept()
            print('[IP: {}, PORT: {}] 접속'.format(ip, port))
            t = threading.Thread(target=self.receive_data, args=(so, ip, port,))
            t.start()


if __name__ == '__main__':
    main = Main()