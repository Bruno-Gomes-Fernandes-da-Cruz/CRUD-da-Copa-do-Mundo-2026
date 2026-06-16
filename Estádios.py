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
    print("1 - Registre uma nova seleção\n2 - Liste todas as seleções\n3 - Busque uma seleção\n4 - Modifique uma seleção\n"
          "5 - Delete uma seleção\n6 - Sair do programa")
    print()
    opcao = int(input("Escolha uma das opções acima de 1 - 6: "))
    match opcao:
        case 1:
            criar_selecao()
        
        case 2:
            listar_selecao() 
        
        case 3:
            buscar_selecao()
                  
            
  

def criar_selecao():
    print()
    global id 
    id += 1
    pais = input("Digite o país da seleção: ")
    grupo = input("Digite o grupo da seleção: ")
    confederacao = input("Digite o nome da confederação: ")
    treinador = input("Digite o nome do treinador: ")
    selecao = {"ID":id,"País":pais,"Grupo":grupo,"Confederação:":confederacao,"Treinador":treinador}
    selecoes.append(selecao)
    print(f"A Seleção do(a) {pais} foi registrada!")
    print(selecao)
    carregamento()
    menu_selecoes()

# Hoje, 13/06/2026 já adicionei a função do menu principal e a de criar, amanhã irei adicionar o resto de acordo com o que o
# professor pediu


def listar_selecao():
    print("Listando todas as seleções da Copa do Mundo 2026: ")
    sleep(2)
    for i in selecoes:
        print("---"*35)
        print(i)
        sleep(2)
    
    carregamento()
    menu_selecoes()
    
def buscar_selecao():
    print("Aqui você pode achar a seleção a qual procura.")   
    print("1 - Buscar seleção pelo ID\n2 - Buscar seleção pelo nome") 
    opcao = int(input("Digite a sua escolha de 1-2: "))
    
    match opcao:
        
        case 1:
            id_selecao = int(input("Digite o ID da seleção que você quer achar: "))
            for i in selecoes:
                if i["ID"] == id_selecao:
                    sleep(1)
                    print("---"*35)
                    print(f"A seleção do(a) {i["País"]}:\n{i}")
                    print("---"*35)
            sleep(3)
            carregamento()
            menu_selecoes()        
        
        case 2:
            nome_selecao = input("Digite o nome da seleção que você quer achar: ").lower()
            for i in selecoes:
                if nome_selecao in i["País"].lower():
                    sleep(1)
                    print("---"*35)
                    print(f"A seleção do(a) {i["País"]}:\n{i}")
                    print("---"*35)
            sleep(3)
            carregamento()
            menu_selecoes()        
                    
# Hoje 14/06/2026 treinei bastante como usar o git. Além disso, criei as funções listar_selecao e buscar_selecao.
# Amanhã devo primeiramente dar add . e commit nesta branch master e depois avisar ao claude que eu quero testar o rebase
# transferindo as mudanças feitas no commit do master para a branch-3       
            
    
menu_selecoes()   