

class Player:
    def __init__(self, attacker):
        self.attacker = attacker
        self.commandPoints = 1
        self.primaryVictoryPoints = 0
        self.secondaryVictoryPoints = 0
        self.imageFile = ''

    def setFaction(self, faction, imageFile):
        self.faction = faction
        self.imageFile = imageFile

    def loadFactionImage(self):
        return

    def modifyCP(self, amount):
        self.commandPoints += amount

    def modifyPrimaryVP(self, amount):
        self.primaryVictoryPoints += amount

    def modifySecondaryVP(self, amount):
        self.secondaryVictoryPoints += amount