import os
import random
import time
#lost game
def lost_game():
    tryagain = input("0.....\nYou lost\nTry again?(y/n) ").lower()
    if tryagain == "y":
        game()
    else:
        exit()
#game: player go first
def game_turn1():
    os.system('cls')
    global_num = 21
    print("You go first\n\nGood luck >:)\n"+str(global_num))
    while global_num > 1:
        player_num = int(input("Your turn: "))
        if player_num > 0 and player_num < 5:
            global_num = global_num - player_num
            machine_num = 5 - player_num
            print(str(global_num)+"\nMachine chose: "+str(machine_num))
            global_num = global_num - machine_num
            print(global_num)
        else:
            print("You can only use 1-4")
    while global_num == 1:
        player_num = int(input("Your turn: "))
        if player_num == 1:
            lost_game()
        else:
            print("You can only use 1")    
#game: player go second    
def game_turn2():
    os.system('cls')
    game_val = 1
    new_global_num = 0
    player_turn_yes = 1
    global_num = 21
    machine_num=random.randint(1,4)
    print("You go second\n"+str(global_num)+"\nMachine chose: "+str(machine_num))
    global_num = global_num - machine_num
    print(global_num)
    while game_val == 1:
        if global_num == 0:
            game_val = 0
            lost_game()
        if global_num == 1:
            while player_turn_yes == 1:
                player_num = int(input("Your turn: "))
                if player_num==1:
                    game_val = 0
                    lost_game()
                else:
                    print("You can only use 1") 
            if player_turn_yes == 0:
                tryagain = input("Machine chose: 1\n0.....\nMachine lost\nTry again?(y/n) ").lower()
                if tryagain == "y":
                    game_val = 0
                    game()
                else:
                    exit()
        if global_num >= 2 and global_num < 22:
            #player turn
            if player_turn_yes == 1:
                player_num = int(input("Your turn: "))
                #if globalnum = player num then lost_game()
                if player_num > 0 and player_num < 5:
                    if player_num > global_num:
                        print("You can only use 1-"+str(global_num)) 
                    else:
                        global_num = global_num - player_num
                        print(global_num)
                        #check if player win 
                        if machine_num + player_num == 5:
                            player_turn_yes = 0
                        #check if machine win
                        elif machine_num + player_num < 5:
                            if global_num == 0:
                                game_val = 0
                                lost_game()
                            else:
                                machine_ctrl_num = 5 - machine_num - player_num
                                new_global_num = global_num - machine_ctrl_num
                                global_num = 31
                                print("HAHA!! you made a mistake >:)\nMachine chose: "+str(machine_ctrl_num)+"\n"+str(new_global_num))
                        elif machine_num + player_num > 5:
                            if global_num == 0:
                                game_val = 0
                                lost_game()
                            else:
                                machine_ctrl_num = 10 - machine_num - player_num
                                new_global_num = global_num - machine_ctrl_num
                                global_num = 31
                                print("HAHA!! you made a mistake >:)\nMachine chose: "+str(machine_ctrl_num)+"\n"+str(new_global_num))
                else:
                    print("You can only use 1-4")
            #machine turn
            if player_turn_yes == 0:
                if global_num == 1:
                    if player_turn_yes == 0:
                        tryagain = input("Machine chose: 1\n0.....\nMachine lost\nTry again?(y/n) ").lower()
                        if tryagain == "y":
                            game_val = 0
                            game()
                        else:
                            exit()
                else:
                    machine_num = random.randint(1,4)
                    global_num = global_num - machine_num
                    print("Machine chose: "+str(machine_num)+"\n"+str(global_num))
                    player_turn_yes = 1
    #game machine in control
        while new_global_num>1:
            player_num = int(input("Your turn: "))
            if player_num > 0 and player_num < 5:
                new_global_num = new_global_num - player_num
                machine_num = 5 - player_num
                print(str(new_global_num)+"\nMachine chose: "+str(machine_num))
                new_global_num = new_global_num - machine_num
                print(new_global_num)
            else:
                print("You can only use 1-4")
        while new_global_num == 1:
            player_num = int(input("Your turn: "))
            if player_num == 1:
                game_val = 0
                lost_game()
            else:
                print("You can only use 1")    
def game():
    os.system('cls')
    game_turn = int(input("----------\n 21 game\n----------\nChoose your turn\ntype '1' to go first\ntype '2' to go second\ntype '0' to see how to play the game\nEnter number: "))
    if game_turn == 1:
        #game: player go first
        game_turn1()
    elif game_turn == 2:
        #game: player go second
        game_turn2()
    elif game_turn == 0:
        #help page
        os.system('cls')
        input("----------\nHow to play\n----------\nChose your turn if you want to go first or second\nTo play chose a number between 1-4\nThe objective is to not to be the first to reach '0'\nIf you reach '0' first you lose the game\nGood luck beating the machine >:)\nPress Enter to continue...")
        game()
    else:
        game()
game()
