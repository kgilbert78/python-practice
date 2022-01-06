class FootballPlayer:
    def __init__(self, name, team, years_in_league):
        self.name = name
        self.team = team
        self.years_in_league = years_in_league

    def printPlayer(self):
        print(self.name+" playing for the "+self.team+":")
    def isGood(self):
        print("Error! isGood is not defined!")
        return False

# pass name of parent class as parameter so it inherits the parent's attributes
class Quarterback(FootballPlayer):
    def __init__(self, name, team, years_in_league, pass_attempts, completions, pass_yards):
        super().__init__(name, team, years_in_league)
        self.pass_attempts = pass_attempts
        self.completions = completions
        self.pass_yards = pass_yards
    def completionRate(self):
        return self.completions/self.pass_attempts
    def yardsPerAttempt(self):
        return self.pass_yards/self.pass_attempts
    def isGood(self):
        return (self.yardsPerAttempt() > 7)

class RunningBack(FootballPlayer):
    def __init__(self, name, team, years_in_league, rushes, rush_yards):
        super().__init__(name, team, years_in_league)
        self.rushes = rushes
        self.rush_yards = rush_yards
    def yardsPerRush(self):
        return self.rush_yards/self.rushes
    def isGood(self):
        return (self.yardsPerRush() > 4)

player1 = Quarterback("John", "Cowboys", 2, 10, 6, 57)

player2 = RunningBack("Joe", "Eagles", 3, 12, 73)

player2.rush_yards = 73
playerlist = []
playerlist.append(player1)
playerlist.append(player2)
for player in playerlist:
    player.printPlayer()
    if (player.isGood()):
        print("  is a GOOD player")
    else:
        print("  is NOT a good player")

        # When the Python compiler sees the call to isGood, it first looks at the definition of isGood in the child class. If there’s not a definition of that method there, it will look at the parent to see if the method is defined there.

# player1.printPlayer()
# print(player1.yardsPerAttempt())
# player2.printPlayer()
# print(player2.yardsPerRush())

# print(player1.years_in_league)