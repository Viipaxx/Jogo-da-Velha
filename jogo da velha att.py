from random import randint
from os import system
from time import sleep


op = ['1','2','3','4','5','6','7','8','9']
jogadas = []
fim = [0]

def ganhador():
    system('cls')
    jogo = f'''
               \033[32m### RESULTADO ###\033[m
                |         |
          {op[0]}     |    {op[1]}    |     {op[2]}
                |         |
     -----------|---------|-----------
                |         |  
          {op[3]}     |    {op[4]}    |     {op[5]}   
                |         |
     -----------|---------|-----------
                |         |
          {op[6]}     |    {op[7]}    |     {op[8]}   
                |         |'''
    print(jogo)

    
    print('\n' + ' ' * 15, end='')
    if fim[0] == 1:
        print('Jogador 1 Ganhou!')
    elif fim[0] == 2:
        print('Jogador 2 Ganhou!')
    elif fim[0] == 3:
        print('EMPATE!')
    input("Aperte 'Enter' para sair!")
    exit()

def jogo():
    system('cls')
    jogo = f'''
            \033[32m ### JOGO\033[m\033[31m DA\033[m\033[33m VELHA ###\033[m
                |         |
          {op[0]}     |    {op[1]}    |     {op[2]}
                |         |
     -----------|---------|-----------
                |         |  
          {op[3]}     |    {op[4]}    |     {op[5]}   
                |         |
     -----------|---------|-----------
                |         |
          {op[6]}     |    {op[7]}    |     {op[8]}   
                |         |
                '''
    print(jogo)
    if len(jogadas) % 2 == 0:
        jogar()
    else:
        jogada_pc()

def jogada(opc):

    op[opc - 1] = '\033[33mX\033[m'
    jogadas.append('+ 1 jogada')
    if len(jogadas) == 9:
        analise2()
    else:
        teste()
        jogo()

def teste():
    if len(jogadas) >= 3:
        analise()
    else:
        jogo()

def jogada_pc(): # Modifique para jogar 

    sleep(0.7)
    pc = randint(1, 9)
    # pc = int(input('Escolha uma opção: '))
    while op[pc - 1] == '\033[33mX\033[m' or op[pc - 1] == '\033[32mO\033[m' :
        pc = randint(1, 9)
        # pc = int(input('Erro! Esolha uma opção: '))
    jogadas.append('+ 1 jogada')
    op[pc - 1] = '\033[32mO\033[m'
    teste()
    jogo()

def jogar(): # Modifique para o robô começar

        # sleep(0.7)
        opc = int(input('Escolha uma opção: '))
        # opc = randint(1, 9)
        while op[opc - 1] == '\033[33mX\033[m' or op[opc - 1] == '\033[32mO\033[m' or opc < 1 or opc > 9:
            opc = int(input('Erro! Escolha outra opção: '))
            # opc = randint(1, 9)
        jogada(opc)

def analise():
    
    if op[0] == '\033[33mX\033[m' and op[1] == '\033[33mX\033[m' and op[2]  == '\033[33mX\033[m': # Horizontal 1
        fim[0] = 1
        ganhador()

    elif op[3] == '\033[33mX\033[m' and op[4] == '\033[33mX\033[m' and op[5] == '\033[33mX\033[m': # Horizontal 2
        fim[0] = 1
        ganhador()

    elif op[6] == '\033[33mX\033[m' and op[7] == '\033[33mX\033[m' and op[8] == '\033[33mX\033[m': # Horizontal 3
        fim[0] = 1
        ganhador()

    elif op[0] == '\033[33mX\033[m' and op[3] == '\033[33mX\033[m' and op[6] == '\033[33mX\033[m': # Vertical 1
        fim[0] = 1
        ganhador()

    elif op[1] == '\033[33mX\033[m' and op[4] == '\033[33mX\033[m' and op[7] == '\033[33mX\033[m': # Vertical 2
        fim[0] = 1
        ganhador()

    elif op[2] == '\033[33mX\033[m' and op[5] == '\033[33mX\033[m' and op[8] == '\033[33mX\033[m': # Vertical 3
        fim[0] = 1
        ganhador()

    elif op[0] == '\033[33mX\033[m' and op[4] == '\033[33mX\033[m' and op[8] == '\033[33mX\033[m': # Diagonal 1
        fim[0] = 1
        ganhador()

    elif op[2] == '\033[33mX\033[m' and op[4] == '\033[33mX\033[m' and op[6] == '\033[33mX\033[m': # Digonal 2
        fim[0] = 1
        ganhador()

    elif op[0] == '\033[32mO\033[m' and op[1] == '\033[32mO\033[m' and op[2] == '\033[32mO\033[m': # Horizontal 1
        fim[0] = 2
        ganhador()
    
    elif op[3] == '\033[32mO\033[m' and op[4] == '\033[32mO\033[m' and op[5] == '\033[32mO\033[m': # Horizontal 2
        fim[0] = 2
        ganhador()
    
    elif op[6] == '\033[32mO\033[m' and op[7] == '\033[32mO\033[m' and op[8] == '\033[32mO\033[m': # Horizontal 3
        fim[0] = 2
        ganhador()
    
    elif op[0] == '\033[32mO\033[m' and op[3] == '\033[32mO\033[m' and op[6] == '\033[32mO\033[m': # Vertical 1
        fim[0] = 2
        ganhador()
    
    elif op[1] == '\033[32mO\033[m' and op[4] == '\033[32mO\033[m' and op[7] == '\033[32mO\033[m': # Vertical 2
        fim[0] = 2
        ganhador()
    
    elif op[2] == '\033[32mO\033[m' and op[5] == '\033[32mO\033[m' and op[8] == '\033[32mO\033[m': # Vertical 3
        fim[0] = 2
        ganhador()
    
    elif op[0] == '\033[32mO\033[m' and op[4] == '\033[32mO\033[m' and op[8] == '\033[32mO\033[m': # Diagonal 1
        fim[0] = 2
        ganhador()
    
    elif op[2] == '\033[32mO\033[m' and op[4] == '\033[32mO\033[m' and op[6] == '\033[32mO\033[m': # Diagonal 2
        fim[0] = 2
        ganhador()
    
    else:
        jogo()

def analise2():

    if op[0] == '\033[33mX\033[m' and op[1] == '\033[33mX\033[m' and op[2]  == '\033[33mX\033[m': # Horizontal 1
        fim[0] = 1
        ganhador()

    elif op[3] == '\033[33mX\033[m' and op[4] == '\033[33mX\033[m' and op[5] == '\033[33mX\033[m': # Horizontal 2
        fim[0] = 1
        ganhador()

    elif op[6] == '\033[33mX\033[m' and op[7] == '\033[33mX\033[m' and op[8] == '\033[33mX\033[m': # Horizontal 3
        fim[0] = 1
        ganhador()

    elif op[0] == '\033[33mX\033[m' and op[3] == '\033[33mX\033[m' and op[6] == '\033[33mX\033[m': # Vertical 1
        fim[0] = 1
        ganhador()

    elif op[1] == '\033[33mX\033[m' and op[4] == '\033[33mX\033[m' and op[7] == '\033[33mX\033[m': # Vertical 2
        fim[0] = 1
        ganhador()

    elif op[2] == '\033[33mX\033[m' and op[5] == '\033[33mX\033[m' and op[8] == '\033[33mX\033[m': # Vertical 3
        fim[0] = 1
        ganhador()

    elif op[0] == '\033[33mX\033[m' and op[4] == '\033[33mX\033[m' and op[8] == '\033[33mX\033[m': # Diagonal 1
        fim[0] = 1
        ganhador()

    elif op[2] == '\033[33mX\033[m' and op[4] == '\033[33mX\033[m' and op[6] == '\033[33mX\033[m': # Digonal 2
        fim[0] = 1
        ganhador()

    elif op[0] == '\033[32mO\033[m' and op[1] == '\033[32mO\033[m' and op[2] == '\033[32mO\033[m': # Horizontal 1
        fim[0] = 2
        ganhador()
    
    elif op[3] == '\033[32mO\033[m' and op[4] == '\033[32mO\033[m' and op[5] == '\033[32mO\033[m': # Horizontal 2
        fim[0] = 2
        ganhador()
    
    elif op[6] == '\033[32mO\033[m' and op[7] == '\033[32mO\033[m' and op[8] == '\033[32mO\033[m': # Horizontal 3
        fim[0] = 2
        ganhador()
    
    elif op[0] == '\033[32mO\033[m' and op[3] == '\033[32mO\033[m' and op[6] == '\033[32mO\033[m': # Vertical 1
        fim[0] = 2
        ganhador()
    
    elif op[1] == '\033[32mO\033[m' and op[4] == '\033[32mO\033[m' and op[7] == '\033[32mO\033[m': # Vertical 2
        fim[0] = 2
        ganhador()
    
    elif op[2] == '\033[32mO\033[m' and op[5] == '\033[32mO\033[m' and op[8] == '\033[32mO\033[m': # Vertical 3
        fim[0] = 2
        ganhador()
    
    elif op[0] == '\033[32mO\033[m' and op[4] == '\033[32mO\033[m' and op[8] == '\033[32mO\033[m': # Diagonal 1
        fim[0] = 2
        ganhador()
    
    elif op[2] == '\033[32mO\033[m' and op[4] == '\033[32mO\033[m' and op[6] == '\033[32mO\033[m': # Diagonal 2
        fim[0] = 2
        ganhador()
    
    else:
        fim[0] = 3
        ganhador()
        exit()

jogo()