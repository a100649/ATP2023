import os
import random
import time

global lista_num
global lista_num_undo
lista_num = []
lista_num_undo = []

def lista_random():
    global lista_num
    global lista_num_undo
    os.system('cls')
    t = int(input("Indique o tamanho da lista que quer: "))
    v = int(input("Indique o valor maximo de um elemento: "))
    lista_num = [random.randint(1, v) for _ in range(t)]
    print("Compilando...")
    time.sleep(0.5)
    print("Lista criada!")
    lista_num_undo = lista_num
    input("Enter to continue...")
    menu()
        
def lista_user():
    global lista_num
    global lista_num_undo
    lista_num = []
    while True:
        os.system('cls')
        str = input("Insira um número (p para parar): ")
        if str == 'p':
            print("Compilando...")
            time.sleep(0.5)
            print("Lista criada!")
            lista_num_undo = lista_num
            input("Enter to continue...")
            menu()
        try:
            num = int(str)
            lista_num.append(num)
        except ValueError:
            os.system('cls')

def calc_soma():
    global lista_num
    os.system('cls')
    print("A soma da lista é: ", sum(lista_num))
    input("Enter to continue...")
    menu()
    
def calc_media():
    global lista_num
    os.system('cls')
    print("A media da lista é: ", (sum(lista_num) / len(lista_num)))
    input("Enter to continue...")
    menu()

def maior_lista():
    global lista_num
    os.system('cls')
    print("O valor maior da lista é: ", max(lista_num))
    input("Enter to continue...")
    menu()

def menor_lista():
    global lista_num
    os.system('cls')
    print("O valor menor da lista é: ", min(lista_num))
    input("Enter to continue...")
    menu()

def ord_cres():
    global lista_num
    os.system('cls')
    print("Lista por ordem crescente:")
    print(sorted(lista_num))
    y = input("Quer editar a lista para crescente? (y/n) ").lower()
    if y == "y":
        lista_num = sorted(lista_num)
    else:
        menu()
    
def ord_decres():
    global lista_num
    os.system('cls')
    print("Lista por ordem decrescente:")
    print(sorted(lista_num, reverse=True))
    y = input("Quer editar a lista para decrescente? (y/n) ").lower()
    if y == "y":
        lista_num = sorted(lista_num, reverse=True)
    else:
        menu()

def find_elem():
    global lista_num
    os.system('cls')
    elem = int(input("Indique o elemento que quer procurar: "))
    if elem in lista_num:
        tryagn = input("A lista contem o elemento "+str(elem)+" na posição "+str(lista_num.index(elem))+". Quer procurar outro? (y/n) ").lower()
        if tryagn == "y":
            find_elem()
        else:
            menu()
    else:
        tryagn = input("A lista não contem o elemento "+str(elem)+". Quer procurar outro? (y/n) ").lower()
        if tryagn == "y":
            find_elem()
        else:
            menu()

def menu():
    global lista_num
    global lista_num_undo
    while True:
        os.system('cls')
        print("███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗")
        print("████╗░████║██╔════╝████╗░██║██║░░░██║")
        print("██╔████╔██║█████╗░░██╔██╗██║██║░░░██║")
        print("██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║")
        print("██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝")
        print("╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░\n")
        print("(1) Criar Lista Aleatória\n(2) Criar Lista do Usuário\n(3) Soma\n(4) Média\n(5) Maior\n(6) Menor\n(7) Está Ordenada por Ordem Crescente\n(8) Está Ordenada por Ordem Decrescente\n(9) Procurar um Elemento\n(0) Sair\n(p) Print Lista atual\n(u) Voltar a lista anterior")
        x = input("Escolha uma opção: ").lower()
        if x == '1':
           lista_random()
        elif x == '2':
            lista_user()
        elif x == '3':
            calc_soma()
        elif x == '4':
            calc_media()
        elif x == '5':
            maior_lista()
        elif x == '6':
            menor_lista()
        elif x == '7':
            ord_cres()
        elif x == '8':
            ord_decres()
        elif x == '9':
            find_elem()
        elif x == '0':
            os.system('cls')
            print("░██████╗░░█████╗░░█████╗░██████╗░██████╗░██╗░░░██╗███████╗")
            print("██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝██╔════╝")
            print("██║░░██╗░██║░░██║██║░░██║██║░░██║██████╦╝░╚████╔╝░█████╗░░")
            print("██║░░╚██╗██║░░██║██║░░██║██║░░██║██╔══██╗░░╚██╔╝░░██╔══╝░░")
            print("╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝██████╦╝░░░██║░░░███████╗")
            print("░╚═════╝░░╚════╝░░╚════╝░╚═════╝░╚═════╝░░░░╚═╝░░░╚══════╝")
            time.sleep(1)
            exit()
        elif x == 'p':
            os.system('cls')
            print("Lista atual:")
            print(lista_num)
            input("Enter to continue...")
        elif x == 'u':
            lista_num = lista_num_undo
        else:
            menu()
menu()