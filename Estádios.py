# Faça um Crud das seleções de acordo com o pedido: id, país, grupo, confederação, treinador
# Boa tarde galera
from time import sleep

selecoes = []
id = 0

def separar(item):
    print("-"*30)
    print(item) 
    print("-"*30)


def carregamento():
    sleep(1)
    print("Carregando.")
    sleep(1)
    print("Carregando..")
    sleep(1)
    print("Carregando...")
    sleep(1)
    

def menu_selecoes():
    print("-"*53)
    print("Bem vindo ao menu das Seleções da Copa do Mundo 2026!")
    print("-"*53)   
    print("Escolha uma das opções abaixo para continuar:")
    print()
    print("1 - Registre um novo estádio\n2 - Liste todos os estádios\n3 - Busque um estádio\n4 - Modifique um estádio\n"
          "5 - Delete um estádio\n6 - Sair do programa")
    print()
    opcao = int(input("Escolha uma das opções acima de 1 - 6: "))
    match opcao:
        case 1:
            criar_selecao()
            
  

def criar_selecao():
    print()
    global id 
    id += 1
    pais = input("Digite o país da seleção: ")
    grupo = input("Digite o grupo da seleção:")
    confederacao = input("Digite o nome da confederação: ")
    treinador = input("Digite o nome do treinador: ")
    selecao = {"ID":id,"País":pais,"Grupo":grupo,"Confederação:":confederacao,"Treinador":treinador}
    selecoes.append(selecao)
    print(f"A Seleção do(a) {pais} foi registrada!")
    print(selecoes)



menu_selecoes()   