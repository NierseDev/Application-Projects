import time
import runpy

print("""
         Choose Game
==============================
 1: Snake           3: Sudoku
 2: BlackJack       4: Guess?

 0: Close Game
==============================
""")

while True:
    ChoiceOfGame = int(input('Enter Game Number: '))
    match ChoiceOfGame:
        case 1:
            print('Running Game, Please Wait!')
            time.sleep(.5)
            exec(open('data\SnakeModule.py').read())
        case 2:
            print('Running Game, Please Wait!')
            time.sleep(.5)
            exec(open('data\BlackJackModule.py').read())
            break
        case 3:
            print('Running Game, Please Wait!')
            time.sleep(.5)
            runpy.run_path('data\solver\solver.py')
            exec(open('data\SodokuModule.py').read())
        case 4:
            print('Running Game, Please Wait!')
            time.sleep(.5)
            exec(open('data\GuessModule.py').read())
        case 0:
            print("Exitting Program!")
            break
        case _:
            print('Error, Please Try Again!')