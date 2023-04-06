//TODO: Assign link of API here:
const api = 'http://localhost:3005/'

let game = {}
let roomId = undefined;

document.getElementById("roomIdSubmit").addEventListener('click', handleSubmitRoomId)

function handleSubmitRoomId(){
    const roomIdInput = document.getElementById("roomIdInput")
    roomId = roomIdInput.value;
}

function getJSON() {
    fetch(api)
        .then(response => response.json())
        .then(response => game = response)
        .catch(err => console.error(err));
    if(game.room_id===roomId && game.room_id !== undefined){
        drawBoard();
    } 
    render();
}

setInterval(getJSON, 1000);

function drawBoard() {
    document.getElementById("roomid-input-container").style.display="none";
    var size = game.size;
    var gameBoard = document.getElementsByClassName("gameboard");
    var gameBoardHTML = "<table cell-spacing = '0'>";
    for (var i = 0; i < size; i++) {
        gameBoardHTML += "<tr>"
        for (var j = 0; j < size; j++) {
            gameBoardHTML += `<td style='width:${600 / size}px; height:${600 / size}px; font-size:${400 / size}px; font-weight: 300'>`
                + game.board[size * i + j]
                + "</td>"
        }
        gameBoardHTML += "</tr>";
    }
    gameBoardHTML += "</table>";
    gameBoard[0].innerHTML = gameBoardHTML;

}

function render() {
    if (game.turn === game.team1_id) {
        document.getElementById('turn-flag-2').style.visibility = "hidden"
        document.getElementById('turn-flag-1').style.visibility = "visible"
    }
    else if (game.turn === game.team2_id) {
        document.getElementById('turn-flag-2').style.visibility = "visible"
        document.getElementById('turn-flag-1').style.visibility = "hidden"
    }
    document.getElementById("match-id").innerText = `Match ID: ${game.match_id}`
    document.getElementById("player1-id").innerText = game.team1_id != undefined ? game.team1_id : "ID1"
    document.getElementById("player2-id").innerText = game.team2_id != undefined ? game.team2_id : "ID2"
    document.getElementById('player1-time').innerHTML = game.time1
    document.getElementById('player2-time').innerHTML = game.time2
    document.getElementById('score1').innerHTML = game.score1
    document.getElementById('score2').innerHTML = game.score2
    document.getElementById('status').innerText = game.status == "None" ? "" : game.status

}






