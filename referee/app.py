from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify, make_response
import json
from Board import BoardGame

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Global variance
PORT=1724
team1_id = "xx1"
team2_id = "xx2"
room_id = "123"
match_id = "321"
size = 5

board_game = BoardGame(size, room_id, match_id, team1_id, team2_id)

@app.route('/init', methods=['POST'])
@cross_origin()
def get_data():
    data  = request.data
    info = json.loads(data.decode('utf-8'))
    # if game_info["team1_id"] is None:
    #     game_info["team1_id"] = info["team_id"]
    # else:
    #     game_info["team2_id"] = info["team_id"]
    return {
        "room_id": board_game.game_info["room_id"],
        "match_id": board_game.game_info["match_id"],
        "init": True, 
        }


@app.route('/', methods=['POST'])
@cross_origin()
def render_board():
    response = make_response(jsonify(board_game.game_info))
    # print("Render: ", game_info)
    return board_game.game_info

@app.route('/')
@cross_origin()
def fe_render_board():
    print(board_game.game_info)
    response = make_response(jsonify(board_game.game_info))
    print(board_game.game_info)
    return response


@app.route('/move', methods=['POST'])
@cross_origin()
def handle_move():
    data = request.data

    team_1_time = 0
    team_2_time = 0
    data = json.loads(data.decode('utf-8'))
    print("Move", data)
    if data["turn"] == board_game.game_info["turn"]:
        board_game.game_info.update(data)
        if data["turn"] == team1_id:
            board_game.game_info["turn"] = team2_id
        else:
            board_game.game_info["turn"] = team1_id
    print(board_game.game_info)

    board_game.convert_board(board_game.game_info["board"])
    
    return 'ok'


if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)