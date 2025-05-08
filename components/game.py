from components.player import Player

class Game:
    def __init__(self):
        self.attacker = Player(True)
        self.defender = Player(False)

        self.activePlayer = ''
        self.activePlayerText = ''

        self.round = 1
        self.battleRoundText = 'Battle Round ' + str(self.round)

        self.gameComplete = False
        self.maxRounds = 5
    
    def setFaction(self, attacker, faction, imageFile):
        if attacker:
            self.attacker.setFaction(faction, imageFile)
        else:
            self.defender.setFaction(faction, imageFile)

    def setFirstPlayer(self,attacker):
        if attacker:
            self.firstPlayer = 'Attacker'
            self.activePlayer = 'Attacker'
            self.activePlayerText = self.activePlayer + '\'s Turn'
        else:
            self.firstPlayer = 'Defender'
            self.activePlayer = 'Defender'
            self.activePlayerText = self.activePlayer + '\'s Turn'

    def incrementTurn(self):
        self.round += 1
        self.battleRoundText = 'Battle Round ' + str(self.round)


    def changeActivePlayer(self):
        if self.gameComplete:
            return False
        
        self.activePlayer = 'Attacker' if self.activePlayer == 'Defender' else 'Defender'
        self.activePlayerText = self.activePlayer + '\'s Turn'
        
        self.attacker.modifyCP(1)
        self.defender.modifyCP(1)

        if self.activePlayer == self.firstPlayer:
            self.incrementTurn()
        
        elif self.round == self.maxRounds and self.activePlayer != self.firstPlayer:
            return False
        
        return True

    '''
    # TODO: Need's database of missions and objectives
    def modifyPoints(self, player, type, amount):
        if player == 'Attacker':
            if type == 'Primary':
                self.attacker.modifyPrimaryVP(amount)
            elif type == 'Seconday':
                self.attacker.modifySecondaryVP(amount)
            else:
                self.attacker.modifyCP(amount)
        else:
            if type == 'Primary':
                self.defender.modifyPrimaryVP(amount)
            elif type == 'Seconday':
                self.defender.modifySecondaryVP(amount)
            else:
                self.defender.modifyCP(amount)
    '''
    