import React from 'react';

class App extends React.Component() {
    render() {
        return (
            <div className="App">
                <div class="scoreboard">
                    <div class="score1-container">
                        <div id="score1"></div>
                        <div class="turn-flag" id="turn-flag-1">
                            <img src="resources/flag.png" alt="" />
                        </div>
                    </div>
                    <div id="match-info">
                        <div id="match-id">Match ID: 123</div>
                        <div class="players-container">
                            <div class="player1">
                                <div id="player1-info">
                                    <div id="player1-id"></div>
                                    <div id="player1-time"></div>
                                </div>

                                <div class="player1-avatar">
                                    <img src="resources/player1avatar.png" alt="" />
                                </div>
                            </div>
                            <div class="player2">
                                <div id="player2-info">
                                    <div id="player2-id"></div>
                                    <div id="player2-time"></div>
                                </div>

                                <div class="player2-avatar">
                                    <img src="resources/player2avatar.png" alt="" />
                                </div>
                            </div>
                        </div>

                    </div>
                    <div class="score2-container">
                        <div id="score2"></div>
                        <div class="turn-flag" id="turn-flag-2" >
                            <img src="resources/flag.png" alt="" />
                        </div>
                    </div>
                </div>
                <div class="gameboard-container">
                    <div class="gameboard">

                    </div>
                </div>
            </div>
        )
    }
}

export default App;
