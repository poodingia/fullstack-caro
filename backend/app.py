import copy
import json
import time
from threading import Thread
import socketio

import requests
from flask import Flask, jsonify, make_response, request
from flask_cors import CORS, cross_origin

from TicTacToeAi import TicTacToeAI

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

host = 'http://localhost:1724'  # Địa chỉ server trọng tài mặc định
team_id = 'xx1' # team_id mặc định
game_info = {}  # Thông tin trò chơi để hiển thị trên giao diện
stop_thread = False  # Biến dùng để dừng thread lắng nghe

ai = TicTacToeAI('X')  # Khởi tạo AI chạy mặc định với đội X


# Giao tiếp với trọng tài qua API:
# nghe trọng tài trả về thông tin hiển thị ở '/', gửi yêu cầu khởi tại qua '/init/' và gửi nước đi qua '/move'
class GameClient:
    def __init__(self, server_url, your_team_id, your_team_roles):
        self.server_url = server_url
        self.team_id = f'{your_team_id}+{your_team_roles}'
        self.team_roles = your_team_roles
        self.match_id = None
        self.board = None
        self.init = None
        self.size = None
        self.ai = None
        self.room_id = None

        self.sio = socketio.Client()
        self.sio.connect(self.server_url)
        
        @self.sio.on('connect')
        def handle_connect():
            print('Client connected')

        @self.sio.on('init')
        def handle_init(dataJson):
            global game_info
            data = dataJson
            game_info = data.copy()
            if game_info.get("init"):
                print("Connection established")
                self.init = True
                self.room_id = game_info["room_id"]

        @self.sio.on('game_info')
        def handle_game_info(dataJson):
            global game_info
            data = dataJson
            game_info = data.copy()
    
    def listen(self):


        while True:
            time.sleep(1)
            
            if not self.init:
                self.send_init()
                continue
            else:
                self.fetch_game_info()

            if game_info.get("room_id") is None:
                # print(game_info)
                continue
                            
            if game_info.get("board"):
                # log_game_info(game_info=game_info)
                if game_info.get("turn") == self.team_id:
                    self.size = game_info["size"]
                    self.board = copy.deepcopy(game_info["board"])
                    move = ai.get_move(game_info["board"], game_info["size"])
                    valid_move = self.check_valid_move(move)
                    print("Move: ", move)
                    if valid_move:
                        self.board[int(move[0])][int(move[1])] = self.team_roles
                        game_info["board"] = self.board
                        self.send_move()
                    else:
                        print("Invalid move")
            
            elif game_info.get("status"):
                print("Game over")
                break

    def send_move(self):
        json_data = json.dumps(game_info)
        self.sio.emit('move', json_data)

    def send_init(self):
        # Gửi yêu cầu kết nối đến server trọng tài
        init_info = {
            "team_id": self.team_id,
            "init": True
        }
        self.sio.emit('init', init_info)

    def fetch_game_info(self):
        # Lấy thông tin trò chơi từ server trọng tài
        time.sleep(1)
        request_info = {
            "room_id": self.room_id,
            "team_id": self.team_id,
            "match_id": self.match_id
        }
        self.sio.emit('game_info', request_info)

    def check_valid_move(self, new_move_pos):
        # Kiểm tra nước đi hợp lệ
        # Điều kiện đơn giản là ô trống mới có thể đánh vào
        if new_move_pos is None:
            return False
        i, j = int(new_move_pos[0]), int(new_move_pos[1])
        if self.board[i][j] == " ":
            return True
        return False

def log_game_info(game_info = game_info):
    while True:
        # time.sleep(2)
    # Ghi thông tin trò chơi vào file log
        print("Match id: ", game_info["match_id"])
        print("Room id: ", game_info["room_id"])
        print("Turn: ", game_info["turn"])
        print("Status: ", game_info["status"])
        print("Size: ", game_info["size"])
        print("Board: ")
        for i in range(int(game_info["size"])):
            for j in range(int(game_info["size"])):
                print(f'{game_info["board"][i][j]},', end=" ")
            print()
        print("time1: ", game_info["time1"])
        print("time2: ", game_info["time2"])
        print("team1_id:", game_info["team1_id"])
        print("team2_id:", game_info["team2_id"])


# API trả về thông tin trò chơi cho frontend
# @app.route('/')
# @cross_origin()
# def get_data():
#     print(game_info)
#     response = make_response(jsonify(game_info))
#     return response


if __name__ == "__main__":
    # Lấy địa chỉ server trọng tài từ người dùng
    host = input("Enter server url: ")
    team_id = input("Enter team id: ")
    team_roles = input("Enter team role (x/o): ").lower()
    # Khởi tạo game client
    gameClient = GameClient(host, team_id, team_roles)
    # gameClient.listen()
    game_thread = Thread(target=gameClient.listen)
    game_thread.start()
    # app.run(host="0.0.0.0", port=3005)
    try:
        while game_thread.is_alive():
            game_thread.join(1)
    except KeyboardInterrupt:
        stop_thread = True
        game_thread.join()
        print("Game client stopped")
