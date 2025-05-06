from flask import Flask, render_template, request, redirect, url_for
from components.game import Game

import os


app = Flask(__name__, template_folder='templates')
app.config.from_mapping(TEMPLATES_AUTO_RELOAD = True)

activeGame = Game()
image_names = os.listdir('./static/logos/')


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        if request.form['setupAttackerButton'] == 'Begin Setup':
            return redirect(url_for('attacker_setup'))
    else:
        return render_template('main.html')

@app.route('/attacker_setup', methods=['POST', 'GET'])
def attacker_setup():
    global activeGame

    if request.method == 'POST': 
        for name in image_names:
            try:
                #try checking request.files or somethingelse from https://tedboy.github.io/flask/generated/generated/flask.Request.html
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
        #print(request.form)
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
   print('active game')
   print(activeGame.attacker.imageFile)
   print(activeGame.defender.imageFile)
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
    if request.method == 'POST':
        return 1
    else:
        return render_template('game_screen.html', attackerLogo=activeGame.attacker.imageFile, defenderLogo=activeGame.defender.imageFile)

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