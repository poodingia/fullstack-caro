from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify, make_response
from flask_socketio import SocketIO, emit, send
import json
import time
from Board import BoardGame

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
socketio = SocketIO(app)

# Global variance
PORT=1724
team1_id = "xx1"
team2_id = "xx2"
team1_role = "x"
team2_role = "o"
room_id = "123"
match_id = "321"
size = 7
#################

time_list = [time.time()] * 2
start_game = False

board = []
for i in range(size):
    board.append([])
    for j in range(size):
        board[i].append(' ')


team1_id_full = team1_id + "+" + team1_role
team2_id_full = team2_id + "+" + team2_role

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('init')
def handle_init(dataJson):
    data = dataJson
    jsonReponse = {
        "room_id": board_game.game_info["room_id"],
        "match_id": board_game.game_info["match_id"],
        "init": True, 
    }
    print('init', jsonReponse)
    emit('init', jsonReponse)

@socketio.on('move')
def handle_move(dataJson):
    data = dataJson
    data = json.loads(data)
    print("Move:",  data)
    log_game_info(board_game.game_info)
    if str(data["turn"]) == str(board_game.game_info["turn"]):
        board_game.game_info.update(data)
        if data["turn"] == team1_id_full:
            board_game.game_info["time1"] += time.time() - time_list[0]
            board_game.game_info["turn"] = team2_id_full
            time_list[1] = time.time()
        else:
            board_game.game_info["time2"] += time.time() - time_list[1]
            board_game.game_info["turn"] = team1_id_full
            time_list[0] = time.time()
        emit('game_info', board_game.game_info)

@socketio.on('game_info')
def handle_board(dataJson):
    data = dataJson
    print("Game_info: ", data)
    global start_game
    if data["team_id"] == team1_id_full and not start_game:
        time_list[0] = time.time()
        start_game = True
    emit('game_info', board_game.game_info)


def log_game_info(game_info):

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

# @app.route('/init', methods=['POST'])
# @cross_origin()
# def get_data():
#     data  = request.data
#     info = json.loads(data.decode('utf-8'))
#     return {
#         "room_id": board_game.game_info["room_id"],
#         "match_id": board_game.game_info["match_id"],
#         "init": True, 
#         }


# @app.route('/', methods=['POST'])
# @cross_origin()
# def render_board():
#     data  = request.data
#     info = json.loads(data.decode('utf-8'))
#     # print(info['team_id'])
#     global start_game
#     if(info["team_id"] == team1_id_full and not start_game):
#         time_list[0] = time.time()
#         start_game = True
#     # print(f'Board: {board_game.game_info["board"]}')
#     response = make_response(jsonify(board_game.game_info))
#     return board_game.game_info

# @app.route('/')
# @cross_origin()
# def fe_render_board():
#     print(board_game.game_info)
#     response = make_response(jsonify(board_game.game_info))
#     print(board_game.game_info)
#     return response


# @app.route('/move', methods=['POST'])
# @cross_origin()
# def handle_move():
#     data = request.data

#     data = json.loads(data.decode('utf-8'))
#     print(f'Board: {board_game.board}')
#     if data["turn"] == board_game.game_info["turn"]:
#         board_game.game_info.update(data)
#         if data["turn"] == team1_id_full:
#             board_game.game_info["time1"] += time.time() - time_list[0]
#             board_game.game_info["turn"] = team2_id_full
#             time_list[1] = time.time()
#         else:
#             board_game.game_info["time2"] += time.time() - time_list[1]
#             board_game.game_info["turn"] = team1_id_full
#             time_list[0] = time.time()
#     print(board_game.game_info)

#     # board_game.convert_board(board_game.game_info["board"])
    
#     return 'ok'


if __name__=="__main__":
    board_game = BoardGame(size, board, room_id, match_id, team1_id_full, team2_id_full)

    socketio.run(app, port=PORT, debug=True)