import random

bob = random.randint(1, 1000)

turn = 1
turnsleft = 4

name = input("Welcome to the game, what is your name? ")

while True:
    print(f'\n{name.title()}, this is turn {turn}, you have {turnsleft} turns left')
    turn += 1
    turnsleft -= 1
    player = ' '
    while player not in range(0, 1000):
        print('Invalid number!!!')
        player = input("Please pick a number from 1-1000 ")
        player = int(player)

    if bob == player:
        print("You guessed it! You win")
        break
    elif bob > player:
        print("Higher")
    else:
        print("Lower")

    if turn == 6:
        print("You ran out of turns!")
        break

print('''

   _____                         ____                 _ 
  / ____|                       / __ \               | |
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __| |
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__| |
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |  |_|
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|  (_)



''')

print(f'The winning number was {bob}')

# http://patorjk.com/software/taag/#p=display&f=Big&t=Game%20Over!