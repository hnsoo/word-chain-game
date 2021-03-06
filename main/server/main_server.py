import socket
import threading
import pickle
import time
from kr_dict_api import *
from datetime import datetime, timedelta


class Main_server:
    # clients_list = []
    user_name_list = []
    current_room: list[list[socket.socket, "player name"]] = [[], [], [], []]  # 예시 [[(so, khs)], [], []]
    state_room: list[True, False] = []  # 게임이 시작중인지 아닌지 여부
    now_player: list["player name"] = []  # 방마다 단어를 입력해야되는 플레이어 닉네임
    remain_time_room = []
    last_word_room: list["last word"] = []  # 방마다 마지막 단어
    score = []
    order = []

    def __init__(self):
        # self.create_rooms()
        self.main_server_socket = None
        # init state_room (룸 갯수만큼 False을 집어넣어줌)
        [self.state_room.append(False) for room in self.current_room]
        # init last_word_room (룸 갯수만큼 ""을 집어넣어줌)
        [self.last_word_room.append("") for room in self.current_room]
        # init now_player (룸 갯수만큼 ""을 집어넣어줌)
        [self.now_player.append("") for room in self.current_room]
        [self.score.append([]) for room in self.current_room]
        [self.remain_time_room.append(None) for room in self.current_room]
        # 게임 순서
        self.order = [0, 0, 0, 0]
        # bind and listen
        self.create_listening_server()

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
        self.set_interval(self.end_game(), 0.2)
        self.main_server_socket.listen(20)
        self.receive_new_user()

    def receive_data(self, so, ip, port):
        print('start receive')
        while True:
            input_data = so.recv(256).decode('utf-8')
            print('serv')
            # 닉네임 중복 확인
            if input_data.startswith('/register/'):
                user_name = input_data[10:]
                if user_name not in self.user_name_list:
                    self.user_name_list.append(user_name)
                    so.send('yes'.encode('utf-8'))
                    print('[IP: {}, PORT: {}] 닉네임 {} 등록 성공'.format(ip, port, user_name))
                else:
                    so.send('no'.encode('utf-8'))
                print('user_name_list: {}'.format(self.user_name_list))
            # 방 인원 상황 새로고침
            elif input_data.startswith('/refresh'):
                # 현재 방 인원 리스트를 직렬화 후 전송
                so.send(pickle.dumps([len(i) for i in self.current_room]))
            # 게임방 접속
            elif input_data.startswith('/room/'):
                room_num = int(input_data[6])
                if len(self.current_room[room_num - 1]) == 4:
                    so.send('no'.encode('utf-8'))
                else:
                    so.send('yes'.encode('utf-8'))
                    user_name = input_data[7:]
                    self.current_room[room_num - 1].append((so, user_name))  # 첫번째 소켓, 두번째 닉네임
                    self.enter_room(room_num, so, user_name)

    def receive_new_user(self):
        while True:
            so, (ip, port) = self.main_server_socket.accept()
            print('[IP: {}, PORT: {}] 접속'.format(ip, port))
            t = threading.Thread(target=self.receive_data, args=(so, ip, port,))
            t.start()

    def enter_room(self, room_num, so, user_name):
        kr_dict = kr_dict_api()
        users = self.current_room[room_num - 1]
        print(users)
        self.send_all(room_number=room_num, msg='join:{}'.format(user_name))

        if self.state_room[room_num - 1] is False and len(self.current_room[room_num - 1]) >= 2:
            if len(self.current_room[room_num - 1]) >= 2:
                time.sleep(0.5)  # 방에서 제일 마지막으로 들어온 인원도 시작 메세지를 받을 수 있도록 sleep을 씀.
                print("게임이 시작됩니다.")
                self.state_room[room_num - 1] = True
                self.last_word_room[room_num - 1] = kr_dict_api.get_start_word()
                self.now_player[room_num - 1] = self.current_room[room_num - 1][self.order[room_num - 1]][1]
                self.score[room_num - 1] = []
                self.score[room_num - 1] = [1000 for i in self.current_room[room_num - 1] ]
                users_name_word = ",".join([name[1] for name in self.current_room[room_num - 1]])
                # print("유저 리스트 문자열", users_name_word)
                # start:{start_word}:{who_is_first_player}
                timer = datetime.now() + timedelta(seconds=50)
                str_timer = timer.strftime("%d/%m/%Y/%H/%M/%S")
                self.remain_time_room[room_num - 1] = timer
                self.send_all(room_number=room_num, msg='start:{}:{}:{}:{}:'.format(
                    self.last_word_room[room_num - 1], self.now_player[room_num - 1], users_name_word, str_timer))

        while True:
            uid = self.find_by_username(room_num, user_name)
            print(self.state_room[room_num - 1], self.now_player[room_num - 1], user_name)
            if self.state_room[room_num - 1] is True and self.now_player[room_num - 1] == user_name:
                input_data = so.recv(256).decode('utf-8')
                print('success recv Word')
                if not input_data:
                    continue
                print(input_data)
                input_word = input_data.split(":")[1]
                print("last word room ", self.last_word_room[room_num - 1])
                last_word_tmp = self.last_word_room[room_num - 1]
                last_word_tmp = last_word_tmp[len(last_word_tmp) - 1:len(last_word_tmp)]
                first_word = input_word[0]
                print("퍼스트 {}, 라스트 {}".format(first_word, last_word_tmp))

                if first_word != last_word_tmp or kr_dict.find_word(input_word) == '':
                    self.send_all(room_number=room_num, msg='attempt:{}:{}:{}'.format(user_name, input_word,
                                                                                      False))
                    self.score[room_num - 1][uid] -= 50
                    print(self.score)
                else:
                    self.send_all(room_number=room_num, msg='attempt:{}:{}:{}'.format(user_name, input_word,
                                                                                      True))
                    self.last_word_room[room_num - 1] = input_word
                    self.score[room_num - 1][uid] += 100
                    print(self.score)
                    if self.order[room_num - 1] < 1:
                        self.order[room_num - 1] += 1
                    else:
                        self.order[room_num - 1] = 0
                    self.now_player[room_num - 1] = self.current_room[room_num - 1][self.order[room_num - 1]][1]
                    self.send_all(room_number=room_num,
                                  msg="change_turn:{}:{}".format(self.now_player[room_num - 1], input_word
                                                                    ))
            else:
                # just chat
                input_data = so.recv(256).decode('utf-8')
                print('success recv Chat')
                if not input_data:
                    continue
                print(input_data)
                for user in users:
                    user[0].sendall(input_data.encode('utf-8'))

    def end_game(self):
        for room_idx, finish_time in enumerate(self.remain_time_room):
            now = datetime.now()
            if finish_time is not None:
                if finish_time < now:
                    msg = ",".join(
                        ["{}님 {}점".format(self.current_room[room_idx][uid][1], player) for uid, player in
                         enumerate(self.score[room_idx])])
                    data = "finish:{}".format(msg)
                    print(room_idx, "   ", finish_time, "     ", finish_time < now,  "     ", data)
                    self.send_all(room_idx + 1, data)
                    self.remain_time_room[room_idx] = None

    def send_all(self, room_number=0, msg=""):
        msg_enc = msg.encode('utf-8')
        for user in self.current_room[room_number - 1]:
            user[0].send(msg_enc)

    def set_interval(self, func, sec):
        def func_wrapper():
            self.set_interval(self.end_game(), sec)
            self.end_game()

        t = threading.Timer(sec, func_wrapper)
        t.start()
        return t

    def find_by_username(self, room_num, name):
        for idx, user in enumerate(self.current_room[room_num - 1]):
            if user[1] == name:
                return idx
        return -1


if __name__ == '__main__':
    main = Main_server()
