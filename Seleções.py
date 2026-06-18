# Bem vindo ao CRUD das seleções da Copa do Mundo 2026!


'''
1 Create — Cadastrar [V]
 Solicitar todos os campos da entidade ao usuário;
 Gerar ID único automaticamente;
 Validar campos obrigatórios (não aceitar valores vazios);
 Salvar o novo registro no arquivo de dados.

2 Read — Consultar [V]
 Listar todos os registros cadastrados de forma organizada;
 Buscar registro por ID ou por nome/país (busca parcial aceita);
 Informar mensagem clara caso nenhum registro seja encontrado.

3 Update — Atualizar [V]
 Localizar o registro pelo ID;
 Permitir atualização de qualquer campo individualmente;
 Salvar as alterações no arquivo após a edição.

4 Delete — Excluir [V]
 Localizar o registro pelo ID;
 Exibir os dados do registro e solicitar confirmação do usuário antes de excluir;
 Atualizar o arquivo após a exclusão.

5 Persistência em Arquivo
 Utilizar arquivo .json ou .csv para armazenar os dados;
 Carregar os dados do arquivo ao iniciar o programa;
 Salvar os dados no arquivo a cada operação de escrita.
'''

import json

from time import sleep





def salvar_selecoes(selecoes):
    with open ("lista_das_selecoes.json","w") as file: # O w sobrescreve tudo quando salva
        json.dump(selecoes, file)
        
        
def carregar_selecoes():
    try:
        with open ("lista_das_selecoes.json","r") as file: # O r apenas lê
            return json.load(file)
    
    except FileNotFoundError: # Esse except é para impedir que dê um erro caso ocorra que o programa não ache o arquivo
        return[]
        

selecoes = carregar_selecoes()        # Esse selecoes depois do if serve para identificar se o selecoes está vazio ou nnão
id = selecoes[-1]["ID"] + 1 if  selecoes else 1





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
        try:    
            selecoes
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
                
                case 4:
                    modificar_selecao()   
                
                case 5:
                    excluir_selecao()     
                
                case 6:
                    print("Saindo do programa.")    
                    carregamento()
                    exit
                    return
            
            if opcao not in [1,2,3,4,5,6]:
                print("Comando desconhecido. Voltando à tela principal.")
                carregamento()
                menu_selecoes()       
        except ValueError:
            print("Erro! Voltando à tela principal.")     
            carregamento()
            menu_selecoes()             
                    
        

  


def criar_selecao(): # Essa função serve para registrar novas seleções dentro do banco de dados
        try:    
            print()
            global id 


            pais = input("Digite o país da seleção: ")
            grupo = input("Digite o grupo da seleção: ")
            confederacao = input("Digite o nome da confederação: ")
            treinador = input("Digite o nome do treinador: ")
            if "" in [pais,grupo,confederacao,treinador]:
                print("Erro! Preencha corretamente os campos e não deixe áreas vazias!")
                carregamento()
                menu_selecoes()
                return
            
            id += 1
            selecao = {"ID":id,"País":pais,"Grupo":grupo,"Confederação:":confederacao,"Treinador":treinador}
            selecoes.append(selecao)
            salvar_selecoes(selecoes)
            print(f"A Seleção do(a) {pais} foi registrada!")
            print(selecao)
            carregamento()
            menu_selecoes()
        
        except ValueError:
            print("Erro! Voltando à tela principal.")     
            carregamento()
            menu_selecoes()     
            





def listar_selecao(): # Essa função lista todas as seleções registradas
        try:    
            if not selecoes: # O not serve para perguntar se não tem nada em selecoes. Se não tiver retorna o valor TRUE 
                print("Nenhuma seleção foi registrada.") 
                carregamento()
                menu_selecoes()   
                return
            print("Listando todas as seleções da Copa do Mundo 2026: ")
            sleep(2)
            for i in selecoes:
                print("---"*35)
                print(i)
                sleep(2)
            
            carregamento()
            menu_selecoes()
        
        except ValueError:
            print("Erro! Voltando à tela principal.")     
            carregamento()
            menu_selecoes()   
  
    
        

def buscar_selecao(): # Essa função serve para buscar uma seleção em específico
    try:    
        if not selecoes: # O not serve para perguntar se não tem nada em selecoes. Se não tiver retorna o valor TRUE 
            print("Nenhuma seleção foi registrada.") 
            carregamento()
            menu_selecoes()   
            return
        
        print("Aqui você pode achar a seleção a qual procura.")   
        print("1 - Buscar seleção pelo ID\n2 - Buscar seleção pelo nome") 
        opcao = int(input("Digite a sua escolha de 1-2: "))
        
        match opcao:
            
            case 1: # Esse case procura a seleção pelo ID
                id_selecao = int(input("Digite o ID da seleção que você quer achar: "))
                contador = 0 # Essa variaveĺ existe para contar se uma seleção existe ou não
                for i in selecoes:
                    if i["ID"] == id_selecao:
                        contador += 1
                        sleep(1)
                        print("---"*35)
                        print(f"A seleção do(a) {i["País"]}:\n{i}")
                        print("---"*35)
                        
                    elif contador == 0 and i == selecoes[-1]:
                        print("Esta seleção não está registrada em nosso sistema!")                     
                        
                sleep(3)
                carregamento()
                menu_selecoes()        
            
            case 2: # Esse case procura a seleção pelo nome
                nome_selecao = input("Digite o nome da seleção que você quer achar: ").lower()
                contador = 0 # Essa variaveĺ existe para contar se uma seleção existe ou não
                for i in selecoes:
                    if nome_selecao in i["País"].lower():
                        contador += 1
                        sleep(1)
                        print("---"*35)
                        print(f"A seleção do(a) {i["País"]}:\n{i}")
                        print("---"*35)
                    
                    elif contador == 0 and i == selecoes[-1] :
                        print("Esta seleção não está registrada em nosso sistema!") 
                
                sleep(3)
                carregamento()
                menu_selecoes()  
                
                      
    except ValueError:
        print("Erro! Voltando à tela principal.")     
        carregamento()
        menu_selecoes()     
                            



def modificar_selecao():
    try:    
        id_selecao = int(input("Digite o ID da seleção a qual você quer modificar: "))
        indice = -1 # Essa variável foi criada para identificar a posição da seleção dentro da lista de seleções
        contador = 0 # Essa variavel serve para identificar se o ID procurado existe ou não através do elif contador >= len(selecoes):
        for i in selecoes:
            contador += 1
            indice += 1 
            if i["ID"] == id_selecao:
                print(f"Você quer modificar a seleção:\n{i}")
                print(f"Você tem certeza que quer modificar a seleção do(a) {i["País"]}? ")
                opcao = input("Digite (S) para sim ou (N) para não: ").lower()
                if opcao == "s":
                    pais = input("Digite o país da seleção: ")
                    grupo = input("Digite o grupo da seleção: ")
                    confederacao = input("Digite o nome da confederação: ")
                    treinador = input("Digite o nome do treinador: ")
                    if "" in [pais,grupo,confederacao,treinador]:
                        print("Erro! Preencha corretamente os campos e não deixe áreas vazias!")
                        carregamento()
                        menu_selecoes()
                        
                    i = {"ID":i["ID"],"País":pais,"Grupo":grupo,"Confederação:":confederacao,"Treinador":treinador}  
                    selecoes[indice] = i
                    salvar_selecoes(selecoes)
                    sleep(1)
                    print(f"A seleção do(a) {i["País"]} foi modificada:\n{selecoes[indice]}")
                    carregamento()
                    menu_selecoes()

                elif opcao == "n":
                    print("Voltando para a tela principal.")
                    carregamento()
                    menu_selecoes()
                    
                
            elif contador >= len(selecoes):
                print("O ID inserido não existe.")
                carregamento()
                menu_selecoes()
    except ValueError:
        print("Erro! Voltando a tela principal.")     
        carregamento()
        menu_selecoes()             





def excluir_selecao():
    try:   
        id_selecao = int(input("Digite o ID da seleção a qual você quer deletar: "))        
        indice = -1 # De forma semelhante ao da função modificar, esta var foi criada para encontra a posição da seleção na lista seleções
        contador = 0
        for i in selecoes:
            contador += 1
            indice += 1
            if i["ID"] == id_selecao:  
                print(f"Você quer deletar a seleção:\n{i}")
                print(f"Você tem certeza que quer deletar a seleção do(a) {i["País"]}? ")
                opcao = input("Digite (S) para sim ou (N) para não: ").lower()
                if opcao == "s":
                    del selecoes[indice]
                    salvar_selecoes(selecoes)
                    print(f"A seleção do(a) {i["País"]} foi deletada com sucesso!")
                    carregamento()
                    menu_selecoes()
                
                elif opcao == "n":
                    print("Voltando ao menu principal.")    
                    carregamento()
                    menu_selecoes()    
                
                else:
                    print("Comando desconhecido.")
                    print("Voltando ao menu principal.")    
                    carregamento()
                    menu_selecoes()  
                            
            elif contador >= len(selecoes):
                print("O ID inserido não existe.")
                carregamento()
                menu_selecoes()
    
    
    except ValueError:
        print("Erro! Voltando à tela principal.")     
        carregamento()
        menu_selecoes()      
    
            
    
menu_selecoes()   