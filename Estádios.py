# Faça um Crud das seleções de acordo com o pedido: id, país, grupo, confederação, treinador-[==[~-+-/*]]////324536789765432456
# Bem vindo ao meu código
'''
1 Create — Cadastrar
 Solicitar todos os campos da entidade ao usuário;
 Gerar ID único automaticamente;
 Validar campos obrigatórios (não aceitar valores vazios);
 Salvar o novo registro no arquivo de dados.

2 Read — Consultar
 Listar todos os registros cadastrados de forma organizada;
 Buscar registro por ID ou por nome/país (busca parcial aceita);
 Informar mensagem clara caso nenhum registro seja encontrado.

3 Update — Atualizar
 Localizar o registro pelo ID;
 Permitir atualização de qualquer campo individualmente;
 Salvar as alterações no arquivo após a edição.

4 Delete — Excluir
 Localizar o registro pelo ID;
 Exibir os dados do registro e solicitar confirmação do usuário antes de excluir;
 Atualizar o arquivo após a exclusão.

5 Persistência em Arquivo
 Utilizar arquivo .json ou .csv para armazenar os dados;
 Carregar os dados do arquivo ao iniciar o programa;
 Salvar os dados no arquivo a cada operação de escrita.
'''

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

# Hoje, 13/06/2026 já adicionei a função do menu principal e a de criar, amanhã irei adicionar o resto de acordo com o que o
# professor pediu

menu_selecoes()   