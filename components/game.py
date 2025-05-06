from components.player import Player

class Game:
    def __init__(self):
        self.attacker = Player(True)
        self.defender = Player(False)
        self.round = 0
    
    def setFaction(self, attacker, faction, imageFile):
        if attacker:
            self.attacker.setFaction(faction, imageFile)
        else:
            self.defender.setFaction(faction, imageFile)

    def setFirstPlayer(self,attacker):
        if attacker:
            self.firstPlayer = 'Attacker'
            self.activePlayer = 'Attacker'
        else:
            self.firstPlayer = 'Defender'
            self.activePlayer = 'Defender'

    def incrementTurn(self):
        self.round += 1

    def changeActivePlayer(self):
        self.activePlayer = 'Attacker' if self.activePlayer == 'Defender' else 'Defender'
        
        self.attacker.modifyCP(1)
        self.defender.modifyCP(1)

        if self.activePlayer == self.firstPlayer:
            self.incrementTurn

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
    