"""
Zach Miller
Final project: Rock, Paper, Scissors
11/25/13
"""
import random
def main():
    print('Rock Paper Scissors Game!')
    print('Rock crushes Scissors!')
    print('Scissors cuts Paper!')
    print('Paper covers Rock!')
    playAgain='y'
    while (playAgain=='y' or playAgain=='Y'):
        computerChoice=random.randint(1,3)
        playerChoice=int(input('Enter 1 for rock, 2 for scissors, and 3 for paper: '))
        print (playerChoice)
        print (computerChoice)
        if(playerChoice==computerChoice):
            print('You made the same choice as the computer. starting over...')
        if(playerChoice==1 and computerChoice==2):
            print('Computer chose scissors')
            print('Player chose Rock')
            print('Player wins!')
        if(playerChoice==2 and computerChoice==3):
            print('Computer chose Paper')
            print('Player chose Scissors')
            print('Player wins!')
        if(playerChoice==3 and computerChoice==1):
            print('Computer chose Rock')
            print('Player chose Paper')
            print('Player wins!')
        if(playerChoice==1 and computerChoice==3):
            print('Computer chose Paper')
            print('Player chose Rock')
            print('Computer wins!')
        if(playerChoice==2 and computerChoice==1):
            print('Computer chose Rock')
            print('Player chose Scissors')
            print('Computer wins!')
        if(playerChoice==3 and computerChoice==2):
            print('Computer chose Scissors')
            print('Player chose Paper')
            print('Computer wins!')
        if(playerChoice!=computerChoice):
            playAgain=input('Do you want to continue? (y for yes, n for no)')
            
        
main()            
