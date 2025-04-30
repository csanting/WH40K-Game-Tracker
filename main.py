from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
   return render_template('main.html')

def mission():
   return render_template('mission_setup.html')

def attacker_setup():
   return render_template('attacker_setup.html')

def defender_setup():
   return render_template('attacker_setup.html')

def begin_game():
   return render_template('game_screen.html')


if __name__ == '__main__':
   print('Simple WH40K Game Tracker\n----------------------------')
   app.run()