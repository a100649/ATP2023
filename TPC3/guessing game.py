import os
import random
import time

max_val = 1000

def choose_max_num():
    global max_val
    os.system('cls')
    max_val=int(input("----------\n Change max number \n----------\nChoose the max number to guess (current max number is "+ str(max_val)+"): "))
    menu()
    
def you_guess():
    os.system('cls')
    print("Guess the number (1-"+str(max_val)+")\nMachine is choosing the number...")
    machine_num=random.randint(1,max_val)
    your_num = 0
    attempt = 1
    time.sleep(1.5)
    while your_num != machine_num:
        your_num=int(input("(Attempt "+ str(attempt)+") - Guess the number (1-"+str(max_val)+"): "))
        if your_num > max_val:
            your_num = 0
        if your_num > machine_num:
            print ("Machine - Smaller...")
            attempt = attempt + 1
        elif your_num < machine_num: 
            print ("Machine - Bigger...")
            attempt = attempt + 1
    input("Machine - Congrats you guessed the number "+ str(machine_num)+" in "+ str(attempt)+" attempts\nPress Enter to continue...")
    menu()
        
def machine_guess():
    os.system('cls')
    your_num=int(input("Machine guess the number (1-"+str(max_val)+")\nChoose your number (max number is "+ str(max_val)+"): "))
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
            print ("(Attempt "+ str(attempt)+"): "+str(machine_num)+"\nYou - Smaller...")
            time.sleep(1 - attempt/((9.5 + attempt/2)*1.5))
            max_machine = machine_num - 1
            attempt = attempt + 1
        elif machine_num < your_num: 
            print ("(Attempt "+ str(attempt)+"): "+str(machine_num)+"\nYou - Bigger...")
            time.sleep(1 - attempt/((9.5 + attempt/2)*1.5))
            min_machine = machine_num + 1
            attempt = attempt + 1
    input("(Attempt "+ str(attempt)+"): "+str(machine_num)+"\nYou - Machine guessed the number "+ str(your_num)+" in "+ str(attempt)+" attempts\nPress Enter to continue...")
    menu()
    
def menu():
    os.system('cls')
    game_turn = int(input("----------\n guessing game \n----------\nChoose your turn:\ntype '1' to guess\ntype '2' to let the machine guess\ntype '0' to change the max value (current max value is "+ str(max_val)+")\nEnter number: "))
    if game_turn==1:
        #game: you guess
        you_guess()
    elif game_turn==2:
        #game: machine guess
        machine_guess()
    elif game_turn==0:
        #change name
        choose_max_num()
    else:
        menu()

menu()
