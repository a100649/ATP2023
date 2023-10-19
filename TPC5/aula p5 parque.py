# Solução do exercício 3
# ----------------------
# Modelo:
#   Parques = [Parque]
#   Parque = [nlugares, ocupados, nome]
#   nlugares = Int
#   ocupados = [lugar]
#   nome = String
#   lugar = Int

# Modelo:
#   Parques = [[Int, [Int], String]]
#   Parque = [Int, [Int], String]
#   nlugares = Int
#   ocupados = [Int]
#   nome = String
#   lugar = Int

#listap = [[Int, [Int], String], [Int, [Int], String], [Int, [Int], String]]

import os
import time
 
global condconsulta
condconsulta = False
global listp
listp = []

def listar():
    print("\nNumero de parques existentes: "+str(len(listp)))
    if listp == []:
        print("[]")
    else:
        print(*listp,sep='\n')
    input("Enter to continue...")
    menu()

def reset():
    global listp
    global condconsulta
    os.system('cls')
    listp = []
    condconsulta = False
    symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
    for i in range (5):
        for ii in symbols:
            os.system('cls')
            print(ii," Reset...\n")
            time.sleep(0.03)
    input("Done!\nEnter to continue...")
    menu()

def estaciona():
    global condconsulta
    global list_lug_ocup
    condconsulta = True
    lugest = int(input("\nEm que lugar quer estacionar: "))
    try:
        for parque in listp:
            if parque[2] == nome_p:
                if lugest in parque[1]:
                    input("Lugar já está ocupado..")
                    consulta_parque()
                else:
                    input("Carro estacionado no lugar "+str(lugest))
                    parque[1].append(lugest)
                    consulta_parque()
    except ValueError:
        consulta_parque()

def liberta_lugar():
    global condconsulta
    global list_lug_ocup
    condconsulta = True
    luglib = int(input("\nQual lugar quer libertar: "))
    try:
        for parque in listp:
            if parque[2] == nome_p:
                if luglib in parque[1]:
                    input("Carro libertado no lugar "+str(luglib))
                    parque[1].remove(luglib)
                    consulta_parque()
                else:
                    input("Lugar já está livre..")
                    consulta_parque()
    except ValueError:
        consulta_parque()

def tamanho_parque():
    global condconsulta
    global listp
    global nome_p
    condconsulta = True
    size_num = int(input("\nNovo tamanho do parque: "))
    try:
        for parque in listp:
            if parque[2] == nome_p:
                parque[0] = size_num
                
                input("Tamanho do parque alterado")
                consulta_parque()
    except ValueError:
        consulta_parque()

def consulta_parque():
    global condconsulta
    global listp
    global list_lug_ocup
    global nome_p
    nn = 0
    n = 0
    if listp == []:
        input("\nNão existem parques para consultar\nEnter to continue...")
        menu()
    os.system('cls')
    if condconsulta == True:
        #show parque
        for parque in listp:
            if parque[2] == nome_p:
                condconsulta = True
                #val quadrado
                while parque[0] >= n*n:
                    n = n + 1
                n = n - 1
                #12 pq e o n maximo de largura do parque (linha)
                if n > 12:
                    n = 12
                    while parque[0] >= n*nn:
                        nn = nn + 1
                    nn = nn - 1
                else:
                    nn = n
                #exec quadrado
                countlug = 1
                nv = nn
                while nv > 0:
                    nh = n
                    while nh>0:
                        #ocup = y/n
                        if countlug in parque[1]:
                            print("| "+str(countlug)+"(ocup) ", end="")
                        else:
                            print("|    "+str(countlug)+"    ", end="")
                        countlug = countlug + 1
                        nh = nh - 1
                    nv = nv - 1
                    print("| \n \n")
                while countlug <= parque[0]:
                    if countlug in parque[1]:
                        print("| "+str(countlug)+"(ocup) ", end="")
                    else:
                        print("|    "+str(countlug)+"    ", end="")
                    countlug = countlug + 1
                print("|\n\nEste é o parque "+str(nome_p)+"\nTem "+str(parque[0])+" lugares")
                print("(1) Estacionar um carro\n(2) Libertar um lugar\n(3) Alterar tamanho do parque\n(0) Sair")
                x = input("Escolha uma opção: ").lower()
                if x == '1':
                    estaciona()
                elif x == '2':
                    liberta_lugar()
                elif x == '3':
                    tamanho_parque()
                elif x == '0':
                    condconsulta = False
                    menu()
                else:
                    consulta_parque()
    if condconsulta == False:
        nome_p = input("Nome do parque para consultar: ")
        for parque in listp:
            if parque[2] == nome_p:
                condconsulta = True
                consulta_parque()
        condconsulta = False
        consulta_parque()
        
def criaParque():
    cond = False
    global list_lug_ocup
    global listp
    while cond == False:
        os.system('cls')
        nome = input("Nome do parque: ")
        if listp == []:
            cond = True
        for parque in listp:
            if parque[2] == nome:
                cond = False
            else:
                cond = True           
    cond = False
    while cond == False: 
        os.system('cls')
        num_lug_str = input("Numero total de lugares do parque: ")
        try:
            num_lug = int(num_lug_str)
            cond = True
            if num_lug == 0:
                cond = False
        except ValueError:
            os.system('cls')
    w = 0    
    cond = False
    list_lug_ocup = []
    while cond == False:
        num_lug = w  
        time.sleep(0.1)
        os.system('cls')
        str = input("Insira um número dos lugares ocupados (p para parar): ") 
        if str == 'p': 
            cond = True
            for x in list_lug_ocup:
                if x > w:
                    list_lug_ocup.remove(x)
            time.sleep(0.1)
            list_lug_ocup = list(set(list_lug_ocup)) 
            list_lug_ocup = sorted(list_lug_ocup)
            parque = [num_lug,list_lug_ocup,nome]
            listp.append(parque)
            input("Parque adicionado!\nEnter to continue...")
            menu()
        try:
            num = int(str)
            if num > w:
                os.system('cls')
            if num == 0:
                os.system('cls')
            list_lug_ocup.append(num)
        except ValueError:
            os.system('cls')

def removeParque():
    global listp
    if listp == []:
        input("\nNão existem parques para remover\nEnter to continue...")
        menu()
    os.system('cls')
    cond = False
    while cond == False:
        nome = input("Nome do parque para remover: ")
        for parque in listp:
            if parque[2] == nome:
                cond = True
                yn = input("Deseja eliminar o parque "+str(nome)+"? (y/n) ").lower()
                if yn == "y":
                    listp.remove(parque)
                    input("Parque removido!\nEnter to continue...")
                else:
                    menu()
            else:
                os.system('cls')

def menu():
    while True:
        os.system('cls')
        print("███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗")
        print("████╗░████║██╔════╝████╗░██║██║░░░██║")
        print("██╔████╔██║█████╗░░██╔██╗██║██║░░░██║")
        print("██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║")
        print("██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝")
        print("╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░\n")
        print("(1) Reset\n(2) Criar Parque\n(3) Remover Parque\n(4) Listar Parques\n(5) Consulta Parque\n(6) \n(7) \n(8) \n(9) \n(0) Sair")
        x = input("Escolha uma opção: ").lower()
        if x == '1':
           reset()
        elif x == '2':
            criaParque()
        elif x == '3':
            removeParque()
        elif x == '4':
            listar()
        elif x == '5':
            consulta_parque()
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
        else:
            menu()
menu()


