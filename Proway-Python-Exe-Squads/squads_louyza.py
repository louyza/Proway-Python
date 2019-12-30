squads = 0

def regras(respostas):
    global squads
    if(respostas[0]==1 and respostas[1]==1 and respostas[2]==1 and respostas[3]==1): 
        print('\033[33m Nicole está apta a entrar no SQUAD!!!!!!!!! \033[0;0m')
        squads+=1
    elif (respostas[0]==2 and respostas[1]==2 and respostas[2]==2 and respostas[3]==2 ):
        print('\033[33m Mateus está apto a entrar no SQUAD!!!!!!!!! \033[0;0m')
        squads+=1
    elif (respostas[0]==3 and respostas[1]==3 and respostas[2]==3 and respostas[3]==3 ):
        print('\033[33m Tiago está apto a entrar no SQUAD!!!!!!!!! \033[0;0m')
        squads+=1
    else:
        print('\033[31m A combinação não deu certo! \033[0;0m')

pessoas = [
    ['Nicole', 'React', 'PHP', 'MySql'],
    ['Mateus', 'Angular', 'Python', 'MongoDB'],
    ['Tiago', 'Vue', 'Java', 'Postgre']
]


while True:

    func = 999
    front = 999
    back = 999
    bd = 999

    while func <= 0 or func > 3:
        try:
            func = int(input ("""
            1 Nicole
            2 Mateus
            3 Tiago
            Escolha um funcionário: 
            """))
        except:
            print('Digite um número!')
    
    while front  <= 0 or front > 3:
        try:
            front = int(input ("""
            1 React
            2 Angular
            3 Vue
            Escolha um framework:
            """))
        except:
            print('Digite um número!')

    while back  <= 0 or back > 3:
        try:
            back = int(input ("""
            1 PHP
            2 Python
            3 Java
            Escolha a linguagem:
            """))
        except:
            print('Digite um número!')

    while bd  <= 0 or bd > 3:
        try:
            bd = int(input ("""
            1 MyQSL
            2 MongoDB
            3 Postgre
            Escolha o banco de d1ados:
            """))
        except:
            print('Digite um número!')

    respostas = [
        func, front, back, bd
    ]

    regras(respostas)

    if squads == 3:
        print('O squad está formado!')
        break
