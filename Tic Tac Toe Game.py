"""A Classic Tic Tac Toe game implemented using python"""
# gameDic Will hold key and values for our game board that will be displayed to the players.
gameDic = {'7':' ', '8':' ', '9':' ', '4':' ', '5':' ', '6':' ', '1':' ', '2':' ', '3':' '}

# keys from the gameDic saved separately to reset our gameDic to default if players want to play again
gamekeys = []

for key in gameDic:
    gamekeys.append(key)

# printGameBox function allows to print empty game Box to the players to take their input


def printGameBox(gameDic):
    print(gameDic['7'] + '|' + gameDic['8'] + '|' + gameDic['9'])
    print('-+-+-')
    print(gameDic['4'] + '|' + gameDic['5'] + '|' + gameDic['6'])
    print('-+-+-')
    print(gameDic['1'] + '|' + gameDic['2'] + '|' + gameDic['3'])
    print('-+-+-')


def game():
    turn = 'X'
    counter = 0
    for i in range(10):  # range(10) because our max game board values will be 9.( from 1 to 9)
        print('Its< ' + turn + ' >turn. Let\'s Play')
        printGameBox(gameDic)
        user_move = input()
        if gameDic[user_move] == ' ':
            gameDic[user_move] = turn
            counter += 1
        else:
            print('Position Already Filled!!!')
            continue
        if counter >= 5:  # 5 because min turns to win by both players is 5
            if gameDic['7'] == gameDic['8'] == gameDic['9'] != ' ':
                printGameBox(gameDic)
                print("Game Over")
                print("Player " + turn + " Won")
                break
            elif gameDic['4'] == gameDic['5'] == gameDic['6'] != ' ':
                printGameBox(gameDic)
                print("Game Over")
                print("Player " + turn + " Won")
                break
            elif gameDic['1'] == gameDic['2'] == gameDic['3'] != ' ':
                printGameBox(gameDic)
                print("Game Over")
                print("Player " + turn + " Won")
                break
            elif gameDic['1'] == gameDic['4'] == gameDic['7'] != ' ':
                printGameBox(gameDic)
                print("Game Over")
                print("Player " + turn + " Won")
                break
            elif gameDic['2'] == gameDic['5'] == gameDic['8'] != ' ':
                printGameBox(gameDic)
                print("Game Over")
                print("Player " + turn + " Won")
                break
            elif gameDic['3'] == gameDic['6'] == gameDic['9'] != ' ':
                printGameBox(gameDic)
                print("Game Over")
                print("Player " + turn + " Won")
                break
            elif gameDic['3'] == gameDic['5'] == gameDic['7'] != ' ':
                printGameBox(gameDic)
                print("Game Over")
                print("Player " + turn + " Won")
                break
            elif gameDic['1'] == gameDic['5'] == gameDic['9'] != ' ':
                printGameBox(gameDic)
                print("Game Over")
                print("Player " + turn + " Won")
                break
        if counter == 9:
            print("Its A Tie")
            print("Game Over")
        # change the player after every move
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    play_again = input("Do You Want to Play Again.(y/n)\n")
    if play_again == 'y' or play_again == 'Y':
        for i in gamekeys:
            gameDic[i] = ' '
        game()


if __name__ == '__main__':
    game()








