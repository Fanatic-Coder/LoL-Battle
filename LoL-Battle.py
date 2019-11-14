from time import sleep
import msvcrt as m


# Defining first the game characters/champions
# with their statistics individually, each game character having his/her function
# into one class called Champion.
# Also, in Champion Class there is the battle function
# and the choosingpl function

class Champion():

    def akali(self, playername):
        self.playername = playername
        self.champname = "Akali"
        self.health = 2033
        self.armor = 85.9
        self.attackdmg = 113
        self.abbpower = 8
        self.mgresist = 53.4

    def braum(self, playername):
        self.playername = playername
        self.champname = "Braum"
        self.health = 2055
        self.armor = 103
        self.attackdmg = 110
        self.abbpower = 4
        self.mgresist = 53.4

    def amumu(self, playername):
        self.playername = playername
        self.champname = "Amumu"
        self.health = 2041
        self.armor = 88.1
        self.attackdmg = 118
        self.abbpower = 8
        self.mgresist = 53.4

    def caitlyn(self, playername):
        self.playername = playername
        self.champname = "Caitlyn"
        self.health = 1884
        self.armor = 82.4
        self.attackdmg = 90.7
        self.abbpower = 2
        self.mgresist = 30

    def ivern(self, playername):
        self.playername = playername
        self.champname = "Ivern"
        self.health = 2110
        self.armor = 81.5
        self.attackdmg = 101
        self.abbpower = 7
        self.mgresist = 53.4

    def fiddlesticks(self, playername):
        self.playername = playername
        self.champname = "Fiddlesticks"
        self.health = 1884
        self.armor = 80.4
        self.attackdmg = 93
        self.abbpower = 9
        self.mgresist = 30

    def choosingpl(self):
        # The name of Player1
        playername = input("Tell me your name Player! ")
        # Player chooses the game character

        print(playername + " Choose Your Champion! \n")
        print("1 for -Akali- \n")
        print("2 for -Braum- \n")
        print("3 for -Amumu- \n")
        print("4 for -Caitlyn- \n")
        print("5 for -Ivern- \n")
        print("6 for -Fiddlesticks- \n")

        # Choicevar is a variable for selecting with a number,
        # the game character/champion of his choice

        choicevar = "a"
        while choicevar != "1" or choicevar != "2" or choicevar != "3" or choicevar != "4" or choicevar != "5" or choicevar != "6":
            choicevar = input("")
            if (choicevar == "1"):
                self.akali(playername)
                print(self.playername + " You Chose " + self.champname + "!")
                break
            elif (choicevar == "2"):
                self.braum(playername)
                print(self.playername + " You Chose " + self.champname + "!")
                break
            elif (choicevar == "3"):
                self.amumu(playername)
                print(self.playername + " You Chose " + self.champname + "!")
                break
            elif (choicevar == "4"):
                self.caitlyn(playername)
                print(self.playername + " You Chose " + self.champname + "!")
                break
            elif (choicevar == "5"):
                self.ivern(playername)
                print(self.playername + " You Chose " + self.champname + "!")
                break
            elif (choicevar == "6"):
                self.fiddlesticks(playername)
                print(self.playername + " You Chose " + self.champname + "!")
                break
            else:
                print("I Didn't recognize your choice! Try Again!")

        return self

    # battle function executes the main battle calculation math
    # and returning/finding the winner

    def battle(self, player1, player2):
        win = ""
        for i in range(1, 5):
            if player1.health > 0 and player2.health > 0:
                # Attack of Player1
                aa1 = input(player1.playername + " " + player1.champname + ", Attack now! Press X! ")
                if aa1 == 'x' or 'X':
                    player1.attackdmg = player1.attackdmg * (100 / (100 + player2.armor))
                    player2.health -= player1.attackdmg
                    print(player2.playername + " " + player2.champname + " Health: %s " % int(player2.health))

                # Attack of Player2
                aa2 = input(player2.playername + " " + player2.champname + ", Attack now! Press M! ")
                if aa2 == 'm' or 'M':
                    player2.attackdmg = player2.attackdmg * (100 / (100 + player1.armor))
                    player1.health -= player2.attackdmg
                    print(player1.playername + " " + player1.champname + " Health: %s " % int(player1.health))
            else:
                print("")
                print(str(player1.playername) + " " + str(player1.champname) + " Health: " + str(int(player1.health)))
                print(str(player2.playername) + " " + str(player2.champname) + " Health: " + str(int(player2.health)))
                if player1.health == player2.health:
                    print("We have A Tie! Well done to you both!")
                elif player1.health > player2.health:
                    win = player1.playername
                else:
                    win = player2.playername
                break
        else:
            print("")
            print(str(player1.playername) + " " + str(player1.champname) + " Health: " + str(int(player1.health)))
            print(str(player2.playername) + " " + str(player2.champname) + " Health: " + str(int(player2.health)))
            if player1.health == player2.health:
                print("We have A Tie! Well done to you both!")
                win = ""
            elif player1.health > player2.health:
                win = player1.playername
                print("And the Winner Is: " + str(win))
            else:
                win = player2.playername
                print("And the Winner Is: " + str(win))
        return win


player1 = Champion().choosingpl()
player2 = Champion().choosingpl()
for i in range(10):
    seconds = 10 - i
    print("Battle starts in: " + str(int(seconds)))
    sleep(1)

winner = Champion().battle(player1, player2)
def wait():
    m.getch()

wait()