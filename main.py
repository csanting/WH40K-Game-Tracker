from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

import os, pickle

from components.game import Game

UPLOAD_FOLDER = '.'
ALLOWED_EXTENSION = {'obj'}


app = Flask(__name__, template_folder='templates')
app.config.from_mapping(TEMPLATES_AUTO_RELOAD = True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = '1'
                                         

activeGame = Game()
image_names = os.listdir('./static/logos/')


@app.route('/', methods=['POST', 'GET'])
def home():
    global activeGame

    if request.method == 'POST':
        if 'setupAttackerButton' in request.form and request.form['setupAttackerButton'] == 'Begin Setup':
            return redirect(url_for('attacker_setup'))
        else:
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            
            file = request.files['file']
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
            
            readGameFile(file)
            return redirect(url_for('game_screen'))
    else:
        return render_template('main.html')

@app.route('/attacker_setup', methods=['POST', 'GET'])
def attacker_setup():
    global activeGame

    if request.method == 'POST': 
        for name in image_names:
            try:
                activeGame.setFaction(True, faction_button_LUT(request.form[name + '.x']), name)
                break
            except KeyError:
                continue
        render_template('defender_setup.html', image_names=image_names)
        return redirect(url_for('defender_setup'))

    else:
        return render_template('attacker_setup.html', image_names=image_names)
        
@app.route('/defender_setup', methods=['POST', 'GET'])
def defender_setup():
    global activeGame
   
    if request.method == 'POST':        
        for name in image_names:
            try:
                activeGame.setFaction(False, faction_button_LUT(request.form[name + '.x']), name)
                break
            except KeyError:
                continue
        return redirect(url_for('choose_first')) 
    else:
        return render_template('defender_setup.html', image_names=image_names)

@app.route('/choose_first', methods=['POST', 'GET'])
def choose_first():
   global activeGame

   if request.method == 'POST':
        try:
            if request.form['firstButtonA.x']:
                activeGame.setFirstPlayer(True)
        except KeyError:
                activeGame.setFirstPlayer(False)

        return redirect(url_for('game_screen')) 
   
   else:
       return render_template('choose_first.html', attacker=activeGame.attacker.imageFile, defender=activeGame.defender.imageFile)

@app.route('/game_screen', methods=['POST', 'GET'])
def game_screen():
    global activeGame

    if request.method == 'POST':
        if 'progressTurnButton' in request.form and request.form['progressTurnButton'] == 'Progress Turn':
            activeGame.attacker.primaryVictoryPoints = int(request.form['aPVP'])
            activeGame.attacker.secondaryVictoryPoints = int(request.form['aSVP'])
            activeGame.attacker.commandPoints = int(request.form['aCP'])

            activeGame.defender.primaryVictoryPoints = int(request.form['dPVP'])
            activeGame.defender.secondaryVictoryPoints = int(request.form['dSVP'])
            activeGame.defender.commandPoints = int(request.form['dCP'])

            # TODO: Save to File results per round

            if not activeGame.gameComplete:
                activeGame.changeActivePlayer()
                                
        if 'endGameButton' in request.form and request.form['endGameButton'] == 'End Game' or activeGame.gameComplete:
            del activeGame
            activeGame = Game()
            return redirect(url_for('home')) 
        
        if 'saveGameButton' in request.form and request.form['saveGameButton'] == 'Save Game':
            activeGame.attacker.primaryVictoryPoints = int(request.form['aPVP'])
            activeGame.attacker.secondaryVictoryPoints = int(request.form['aSVP'])
            activeGame.attacker.commandPoints = int(request.form['aCP'])

            activeGame.defender.primaryVictoryPoints = int(request.form['dPVP'])
            activeGame.defender.secondaryVictoryPoints = int(request.form['dSVP'])
            activeGame.defender.commandPoints = int(request.form['dCP'])
        
            fileName = request.form['saveFileName']
            if fileName != '':
                writeGameFile(fileName)
        
        return render_template('game_screen.html', attackerLogo=activeGame.attacker.imageFile, 
                            defenderLogo=activeGame.defender.imageFile, aPVP=activeGame.attacker.primaryVictoryPoints, 
                            aSVP=activeGame.attacker.secondaryVictoryPoints, aCP=activeGame.attacker.commandPoints,
                            dPVP=activeGame.defender.primaryVictoryPoints, dSVP=activeGame.defender.secondaryVictoryPoints, 
                            dCP=activeGame.defender.commandPoints, battleRoundText=activeGame.battleRoundText, activePlayerText=activeGame.activePlayerText)
    else:
        return render_template('game_screen.html', attackerLogo=activeGame.attacker.imageFile, 
                            defenderLogo=activeGame.defender.imageFile, aPVP=activeGame.attacker.primaryVictoryPoints, 
                            aSVP=activeGame.attacker.secondaryVictoryPoints, aCP=activeGame.attacker.commandPoints,
                            dPVP=activeGame.defender.primaryVictoryPoints, dSVP=activeGame.defender.secondaryVictoryPoints, 
                            dCP=activeGame.defender.commandPoints, battleRoundText=activeGame.battleRoundText, activePlayerText=activeGame.activePlayerText)
## Helper Functions ##
def readGameFile(file):
    global activeGame

    readFile = open(file.filename, 'rb')

    del activeGame
    activeGame, attacker, defender = pickle.load(readFile, fix_imports=True, errors='strict', buffers=None)
    activeGame.attacker = attacker
    activeGame.defender = defender

    readFile.close()
    
def writeGameFile(fileName):
    writeFile = open(fileName + '.obj','wb')
    pickle.dump([activeGame, activeGame.attacker, activeGame.defender], writeFile, protocol=None, fix_imports=True, buffer_callback=None)
    writeFile.close()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION

def faction_button_LUT(imageName):
   endIndex = imageName.find('symbol') - 1
   imageName[0:endIndex]

   return imageName[0:endIndex]

'''
#TODO: Create Database of all missions, objectives, etc...
def mission():
   return render_template('mission_setup.html')
'''

if __name__ == '__main__':
   print('Simple WH40K Game Tracker\n----------------------------')
   app.run(debug=True, host="0.0.0.0")