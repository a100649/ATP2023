import os
import random
import time

max_val = 1000

def choose_max_num():
    global max_val
    os.system('cls')
    print("----------\n Change max number \n----------")
    max_val=int(input("Choose the max number to guess (current max value is "+ str(max_val)+"): "))
    menu()
    
def you_guess():
    machine_num=random.randint(1,max_val)
    your_num = 0
    attempt = 1
    while your_num != machine_num:
        your_num=int(input("(Attempt "+ str(attempt)+") - Guess the number: "))
        if your_num > max_val:
            your_num = 0
        if your_num > machine_num:
            print ("Smaller")
            attempt = attempt + 1
        elif your_num < machine_num: 
            print ("Bigger")
            attempt = attempt + 1
    print ("Congrats you guessed the number "+ str(machine_num)+" in "+ str(attempt)+" attempts")
    input("Press Enter to continue...")
    menu()
        
def machine_guess():
    os.system('cls')
    print("Machine guess the number")
    your_num=int(input("Choose your number: "))
    machine_num = 0
    attempt = 1
    min_machine = 1
    max_machine = max_val
    if your_num > max_val:
        machine_guess()
    while machine_num != your_num:
        machine_num=random.randint(min_machine,max_machine)
        if attempt <= round(10 +(max_machine / 1000)):
            if machine_num != your_num:
                machine_num = round((max_machine + min_machine -1) / 2)
        if machine_num > your_num:
            print ("(Attempt "+ str(attempt)+") - Smaller...")
            time.sleep(1 - attempt/((9.5 + attempt/2)*1.5))
            max_machine = machine_num - 1
            attempt = attempt + 1
        elif machine_num < your_num: 
            print ("(Attempt "+ str(attempt)+") - Bigger...")
            time.sleep(1 - attempt/((9.5 + attempt/2)*1.5))
            min_machine = machine_num + 1
            attempt = attempt + 1
    print ("Machine guessed your number "+ str(your_num)+" in "+ str(attempt)+" attempts")
    input("Press Enter to continue...")
    menu()
    
def menu():
    global x
    x = 0
    os.system('cls')
    print("----------\n guessing game \n----------")
    print("Choose your turn:\ntype '1' to guess\ntype '2' to let the machine guess\ntype '0' to change the max value (current max value is "+ str(max_val)+")")
    game_turn = int(input("Enter number: "))
    if game_turn==1:
        #game: you guess
        os.system('cls')
        print("Guess the number")
        you_guess()
    elif game_turn==2:
        x = 0
        #game: machine guess
        os.system('cls')
        machine_guess()
    elif game_turn==0:
        # change name
        choose_max_num()
    else:
        menu()
menu()