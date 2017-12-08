from flask import Flask, render_template, request, session
import wordgame
app = Flask(__name__)
import time

## guitarist = 'unknown'
## why = 'unknown'

@app.route('/getform')
def get_and_display_form():
    return render_template('index.html',
                           the_title="This is the index page", )

@app.route('/processform', methods=['POST'])
def process_the_form():
    wordgame.clearUsedWords()
    wordgame.clearInvalidWords()
    wordgame.clearShortWords()
    wordgame.clearLongWords()
    session['sourceWord'] = wordgame.getSourceWord()
    session['startTime']= time.time()
    stopTheTime= True
    return render_template('game.html',
                           the_title="The Game",
                           the_word = session['sourceWord'])

@app.route('/gameover', methods=['POST'])
def process_the_name():
    session['WordList'] = request.form['answer']
    isAcceptable = wordgame.checkWords(session['sourceWord'] , session['WordList'].split())

    if isAcceptable == True:
        session['timeTaken']= round(time.time()- session.get("startTime"),2)
        return render_template('name.html',the_title="Enter Name",the_answers=session['WordList'].split(), the_time= session['timeTaken'])
    else:
        invalid=[]
        used=[]
        theShortWords=[]
        theLongWords=[]
        invalid= wordgame.getInvalidWords().copy()
        used = wordgame.getUsedWords().copy()
        theShortWords = wordgame.getShortWords().copy()
        theLongWords = wordgame.getLongWords().copy()
        return render_template('invalid.html', the_title="Loser", the_invalid= invalid, the_used=used,
                                the_short= theShortWords, the_long= theLongWords)


@app.route('/leaderboard', methods=['POST'])
def process_the_board():
    if request.method == 'POST':
        session['username'] = request.form['username']
    wordgame.updateLeaderboard(session['username'], session['timeTaken'])
    position = wordgame.getLeaderboardPosition(session['username'])
    players = wordgame.getLeaderBoardList()
    dictionary = wordgame.getPlayerDict()

    for x in players:
        dictionary[x] = round(dictionary[x], 2)

    return render_template('leaderboard.html',
                           the_title="Leaderboard",
                           the_players= players,
                           the_dict= dictionary,
                           the_name = session['username'],
                           the_pos = position)


if __name__ == '__main__':
    app.secret_key = "lfvDLFKgDFKGdfgadfLKhndFjAgdaFAHdfgj:DFAjhhjhjhdfLJ"
    app.run(debug=True)
