#JN: Perfect!
#And thanks for making it fun.
#100/100 (Koy)

from cs1graphics import *
import random


class Hangman:
    def __init__(self):
        self.wordOptions = ['COOKIES', 'WILDERNESS', 'WASTEFUL', 'BREAKFAST', 'VORACIOUS', 'NOTEBOOK']
        self.secretWord = random.choice(self.wordOptions)  # random word choice
        self.underScores = list()  # variables for underscores
        self.uncoveredLtr = list()  # variable for uncovered letter to keep track of them as we go.
        self.guesses = list()  # empty list containing all failed guesses
        self.correctGuesses = list()  # empty list containing the correct guesses which is to be used later
        self.tries = 6  # predetermined set of tries before hanged man is completely drawn
        self.ptsToWin = 0  # predetermined variable used to keep track of the points needed to win
        self.display = Canvas(500, 500, 'skyblue', 'Hangman')  # designs for the hanged man... boring stuff under lol
        self.winningText = Text('YOU WIN, \nGRAB A DRINK')
        self.losingMessage = Text('You Lose, Loser!\nNO DRINK FOR YOU')
        self.rope = Path(Point(247, 97), Point(247, 150))
        self.rope.setBorderWidth(7)

        self.topHat = Path(Point(97, 100), Point(250, 100))
        self.topHat.setBorderWidth(7)
        self.display.add(self.topHat)

        self.poleBase = Path(Point(97, 475), Point(300, 475))
        self.poleBase.setBorderWidth(7)
        self.display.add(self.poleBase)

        self.hangingPole = Path(Point(100, 475), Point(100, 100))
        self.hangingPole.setBorderWidth(6)
        self.display.add(self.hangingPole)

        self.head = Circle(50, Point(250, 200))
        self.head.setBorderColor('Black')
        self.head.setBorderWidth(2)

        self.body = Path(Point(250, 250), Point(250, 400))
        self.body.setBorderWidth(2)

        self.leftArm = Path(Point(250, 300), Point(150, 260))
        self.leftArm.setBorderWidth(2)

        self.rightArm = Path(Point(250, 300), Point(350, 260))
        self.rightArm.setBorderWidth(2)

        self.leftLeg = Path(Point(250, 400), Point(150, 460))
        self.leftLeg.setBorderWidth(2)

        self.rightLeg = Path(Point(250, 400), Point(350, 460))
        self.rightLeg.setBorderWidth(2)

    def playHangman(self):
        winningAnswer = int(
            len(self.secretWord))  # variable contains the length of secret word which is used to create underscores
        for x in range(winningAnswer):
            self.underScores.insert(x, '_')
        print(self.underScores)
        while self.tries > 0:  # while the tries remaining is greater than 0, game will continue
            if self.ptsToWin >= winningAnswer:  # base for winning the game... if you reach x amount of point = you win
                print('YOU WIN, \nGRAB A DRINK')
                self.winningText.move(250, 250)
                self.winningText.setFontSize(40)
                self.display.add(self.winningText)
                break  # breaks the loops and continues
            self.letter = (input('Guess one letter from A-Z?'))  # requires an input
            self.upperLtr = self.letter.upper()  # converts input into cap letter

            if len(self.letter) > 1 or len(
                    self.letter) <= 0:  # if the input from user is less greater than 1 or empty, asks for reinput
                print('Read the instructions! ONE LETTER!')
                continue  # restarts the loop, fake end point

            if self.upperLtr in self.correctGuesses:  # if the input is in list, asks user for reentry
                print('Already entered. Enter another.')
                continue  # restarts the loop, fake end point

            if self.upperLtr not in self.secretWord:  # if input is not in the secret word...
                self.tries -= 1  # lose a try...
                self.drawHangman(self.tries)  # draws a piece of the hangedman based on tries left
                print('Guess was not within the hidden word. You have ' + str(
                    self.tries) + 'tries left')  # print tries remaining
                if self.upperLtr not in self.guesses:  # nested loop that checks if input is or is not inside list of
                    # guesses
                    self.guesses.append(
                        self.upperLtr)  # if it is not in list, appends(adds) it to end of list. If it is, skips.
                print(self.guesses)
            else:
                print(
                    'Correct!')  # if input in variable, prints corrects and appends input into the correct guesses list
                self.correctGuesses.append(self.upperLtr)

            self.uncoveredLtr += self.upperLtr  # if input is in secret word, grabs it and displays it which shows it
            # to user
            self.correctLetters = 0  # predetermined variable and integer which used to count correct letters/guesses

            for y in self.secretWord:  # for every entry/input in the secretWord...
                if y in self.uncoveredLtr:  # if the entry/input is in the uncovered letters, print that letter and
                    # add 1 to correct letters
                    print(y)
                    self.correctLetters += 1
                else:
                    print('_')  # prints underscore if otherwise
            self.ptsToWin = self.correctLetters  # assigns ptsToWin to the correct letters which if greater than or
            # equal to winning answer is whats needed to win

            if self.tries == 0:  # if the amount of tries is equivalent to 0, meaning no more tries... print such.
                print('YOU LOSE, LOSER \nGET OUT OF MY FACE!')

    def drawHangman(self, tries):  # function needed to draw hanged man which is dependent on tries left
        if tries == 5:  # if amount of tries reaches 5, adds to the canvas (rope and the head)
            self.display.add(self.rope)
            self.display.add(self.head)
        elif tries == 4:  # if amount of tries reaches 4, adds to the canvas (body)
            self.display.add(self.body)
        elif tries == 3:  # if amount of tries reaches 3, adds to the canvas (left arm)
            self.display.add(self.leftArm)
        elif tries == 2:  # if amount of tries reaches 2, adds to the canvas (right arm)
            self.display.add(self.rightArm)
        elif tries == 1:  # if amount of tries reaches 1, adds to the canvas (left leg)
            self.display.add(self.leftLeg)
        elif tries == 0:  # if amount of tries reaches 0, adds the last piece to the puzzles and ends the game
            self.display.add(self.rightLeg)
            self.losingMessage.move(245, 250)
            self.losingMessage.setFontSize(40)
            self.display.add(self.losingMessage)  # the losing text is displayed


player = Hangman()  # assigns the hangman class to the player
player.playHangman(
)  # calls the function playHangman() and takes the secret word as parameters secret.
