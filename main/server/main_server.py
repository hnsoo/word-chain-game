import socket
import room_server


class Main:
    # clients_list = []
    user_name_list = []

    def __init__(self):
        # self.create_rooms()
        self.main_server_socket = None
        # bind and listen
        self.create_listening_server()

    def create_rooms(self):
        for i in range(4):
            title = "Room {}".format(i)
            t = room_server.Room_thread(title)
            t.start()

    def check_user_duplication(self, name):
        if name in self.user_name_list:
            return False
        else:
            # accept
            self.receive_new_user()
            return True

    def create_listening_server(self):
        # 소켓 생성
        self.main_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        HOST = '127.0.0.1'
        PORT = 55555
        # 소켓 레벨과 데이터 설정
        self.main_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 소켓을 네트워크(주소, 포트)에 연결
        self.main_server_socket.bind((HOST, PORT))
        print("Listening for incoming messages..")
        # 최대 20명까지 listen
        self.main_server_socket.listen(20)
        self.receive_new_user()

    def receive_new_user(self):
        while True:
            so, (ip, port) = self.main_server_socket.accept()
            input_name = so.recv(256).decode('utf-8')
            if input_name in self.user_name_list:
                so.send("no".encode('utf-8'))
                print('IP: {}, PORT: {} 접속 | no 응답'.format(ip, port))
            else:
                so.send("yes".encode('utf-8'))
                print('IP: {}, PORT: {} 접속 | yes 응답'.format(ip, port))
                self.user_name_list.append(input_name)
            print('user_name_list: {}'.format(self.user_name_list))


if __name__ == '__main__':
    main = Main()